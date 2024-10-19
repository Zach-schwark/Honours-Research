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


full_filename = "Cross_Validation_outputs/Full_Log_Likelihoods/BDeu_full.csv"
desired_filename = "Cross_Validation_outputs/Desired_Log_Likelihoods/BDeu_desired_"+str(evidence_list_type)+".csv"

header = ['dataset_size','full_log_likelihood']
try:
    with open(full_filename, 'x', newline="") as file:
        csvwriter = csv.writer(file) 
        csvwriter.writerow(header)
except FileExistsError:
    with open(full_filename, 'w', newline="") as file:
        csvwriter = csv.writer(file) 
        csvwriter.writerow(header)
    
    
header_desired = ['dataset_size','desired_log_likelihood']
try:
    with open(desired_filename, 'x', newline="") as file:
        csvwriter = csv.writer(file) 
        csvwriter.writerow(header_desired)
except FileExistsError:
    with open(desired_filename, 'w', newline="") as file:
        csvwriter = csv.writer(file) 
        csvwriter.writerow(header_desired)

wandb.init(
    project="Honours-Research",
    name = "BDeu_"+str(evidence_list_type),
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


evidence_features = DataPreprocessing.return_evidence_features(list_description=str(evidence_list_type), inc_loan_amnt=False)
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
                                                                  desired=True,
                                                                  SL_equivalent_sample_size = ess,
                                                                  prior_type = prior_type,
                                                                  pseudo_counts = int(pseudo_count))
    row_full = [num_rows, log_likelihood]
    row_desired = [num_rows, desired_log_likelihood]
    with open(full_filename, 'a', newline="") as file:
        csvwriter = csv.writer(file) 
        csvwriter.writerow(row_full)
    with open(desired_filename, 'a', newline="") as file:
        csvwriter = csv.writer(file) 
        csvwriter.writerow(row_desired)   
    wandb.log({"dataset size":num_rows,"log_likelihood": log_likelihood, str(evidence_list_type)+"_log_likelihood": desired_log_likelihood})

wandb.finish()