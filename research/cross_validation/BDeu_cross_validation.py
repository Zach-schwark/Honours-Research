import sys
sys.path.insert(0,"./")
from Models import BDeuBayesianNetwork
from Data.DataPreprocessing import DataPreprocessing
import CrossValidation
from pgmpy import config
import numpy as np
import pandas as pd
import torch
import logging
from tqdm import tqdm
import wandb
import csv
from pgmpy.global_vars import logger
logger.setLevel(logging.ERROR)

if len(sys.argv) != 5:
    exit()
    
ess = sys.argv[1]
prior_type = sys.argv[2]
pseudo_count = sys.argv[3]
evidence_list_type = sys.argv[4]


full_evaluation = False
desired_evaluation = False

if evidence_list_type == "none":
    full_evaluation = True
    full_filename = "Cross_Validation_outputs/Full_Log_Likelihoods/BDeu_full.csv"
    header = ['dataset_size','full_log_likelihood']
    try:
        with open(full_filename, 'x', newline="") as file:
            csvwriter = csv.writer(file) 
            csvwriter.writerow(header)
    except FileExistsError:
        with open(full_filename, 'w', newline="") as file:
            csvwriter = csv.writer(file) 
            csvwriter.writerow(header)
else:
    desired_evaluation = True
    desired_filename = "Cross_Validation_outputs/Desired_Log_Likelihoods/BDeu_desired_"+str(evidence_list_type)+".csv"
    header_desired = ['dataset_size','desired_log_likelihood']
    try:
        with open(desired_filename, 'x', newline="") as file:
            csvwriter = csv.writer(file) 
            csvwriter.writerow(header_desired)
    except FileExistsError:
        with open(desired_filename, 'w', newline="") as file:
            csvwriter = csv.writer(file) 
            csvwriter.writerow(header_desired)
            
if full_evaluation == True:
    wandb_run_name = "BDeu"
elif desired_evaluation == True:
    wandb_run_name = "BDeu_"+str(evidence_list_type)

wandb.init(
    project="Honours-Research",
    name = wandb_run_name,
    config={
        "prior_type": prior_type,
        "pseudo_counts": int(pseudo_count),
        "SL_equivalent_sample_size": int(ess),
    }
)


config.set_dtype(dtype=np.float32)

loaded_data: pd.DataFrame = DataPreprocessing.load_data()
data: pd.DataFrame = DataPreprocessing.preprocess_data(loaded_data)
feature_states = DataPreprocessing.get_feature_states(data)
print("#############")
print("Data loaded")
print("#############\n")


if desired_evaluation == True:
    evidence_features = DataPreprocessing.return_evidence_features(list_description= str(evidence_list_type), inc_loan_amnt=False)
else:
    # this is just to set the evidence list to some evidence to prevent errors since the Model class needs the evidence list set.
    evidence_features = DataPreprocessing.return_evidence_features(list_description= "basic", inc_loan_amnt=False)
    
target_features = DataPreprocessing.return_target_features(inc_loan_amnt=True)


def variable_step_loop(start, end):
    current = start
    while current < end:
        yield current
        
        if current < 1000:
            step = 50
        elif current < 10000:
            step = 500
        else:
            step = 5000
        
        current = min(current + step, end)


for num_rows in variable_step_loop(50, 110000):
    train_data, test_data = DataPreprocessing.split_data(data, num_rows = num_rows)
    folds = CrossValidation.kfold_indices(data = train_data, k = 5 )
    log_likelihood, desired_log_likelihood = CrossValidation.perfrom_KfoldCrossValidation(folds = folds,
                                                                  data=train_data,
                                                                  Model = BDeuBayesianNetwork,
                                                                  feature_states=feature_states,
                                                                  evidence_features=evidence_features,
                                                                  target_features=target_features,
                                                                  desired=desired_evaluation,
                                                                  SL_equivalent_sample_size = ess,
                                                                  prior_type = prior_type,
                                                                  pseudo_counts = int(pseudo_count))
    if full_evaluation == True:
        row_full = [num_rows, log_likelihood]
        with open(full_filename, 'a', newline="") as file:
            csvwriter = csv.writer(file) 
            csvwriter.writerow(row_full)
    if desired_evaluation == True:
        row_desired = [num_rows, desired_log_likelihood]
        with open(desired_filename, 'a', newline="") as file:
            csvwriter = csv.writer(file) 
            csvwriter.writerow(row_desired) 
            
    if full_evaluation == True:
        wandb.log({"dataset size":num_rows,"log_likelihood": log_likelihood})
    if desired_evaluation == True:               
        wandb.log({"dataset size":num_rows, str(evidence_list_type)+"_log_likelihood": desired_log_likelihood})

wandb.finish()