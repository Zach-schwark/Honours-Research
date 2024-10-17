import sys
sys.path.insert(0,"./")
from Models import BICBayesianNetwork
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




full_filename = "Cross_Validation_outputs/Full_Log_Likelihoods/BIC_full.csv"
desired_filename = "Cross_Validation_outputs/Desired_Log_Likelihoods/BIC_desired_basic.csv"


header = ['dataset_size','full_log_likelihood']
with open(full_filename, 'w', newline="") as file:
    csvwriter = csv.writer(file) 
    csvwriter.writerow(header)
    
    
header_desired = ['dataset_size','desired_log_likelihood']
with open(desired_filename, 'w', newline="") as file:
    csvwriter = csv.writer(file) 
    csvwriter.writerow(header_desired)


wandb.init(
    project="Honours-Research",
    name = "BIC",
    config={
        "prior_type": "dirichlet",
        "pseudo_counts": 1,
    }
)


config.set_dtype(dtype=np.float64)

loaded_data: pd.DataFrame = DataPreprocessing.load_data()
data: pd.DataFrame = DataPreprocessing.preprocess_data(loaded_data)
feature_states = DataPreprocessing.get_feature_states(data)
print("#############")
print("Data loaded")
print("#############\n")


evidence_features = DataPreprocessing.return_evidence_features(list_description="basic", inc_loan_amnt=False)
target_features = DataPreprocessing.return_target_features(inc_loan_amnt=True)


def variable_step_loop(start, end):
    current = start
    while current < end:
        yield current
        
        if current < 1000:
            step = 100
        elif current < 10000:
            step = 1000
        else:
            step = 10000
        
        current = min(current + step, end)


for num_rows in variable_step_loop(100, 250000):
    train_data, test_data = DataPreprocessing.split_data(data, num_rows = num_rows)
    folds = CrossValidation.kfold_indices(data = train_data, k = 5 )
    #, desired_log_likelihood
    log_likelihood = CrossValidation.perfrom_KfoldCrossValidation(folds = folds,
                                                                  data=train_data,
                                                                  Model = BICBayesianNetwork,
                                                                  feature_states=feature_states,
                                                                  evidence_features=evidence_features,
                                                                  target_features=target_features,
                                                                  desired=False,
                                                                  prior_type = "dirichlet",
                                                                  pseudo_counts = 1)
    row_full = [num_rows, log_likelihood]
    #row_desired = [num_rows, desired_log_likelihood]
    with open(full_filename, 'a', newline="") as file:
        csvwriter = csv.writer(file) 
        csvwriter.writerow(row_full)
    #with open(desired_filename, 'a', newline="") as file:
    #    csvwriter = csv.writer(file) 
    #    csvwriter.writerow(row_desired) 
    wandb.log({"dataset size":num_rows,"log_likelihood": log_likelihood})

wandb.finish()