import sys
sys.path.insert(0,"./")
from Models import BICBayesianNetwork
import Models
from Data.DataPreprocessing import DataPreprocessing
from pgmpy import config
import numpy as np
import pandas as pd
import torch
import logging
from tqdm import tqdm
from pgmpy.global_vars import logger
logger.setLevel(logging.ERROR)


def kfold_indices(data: pd.DataFrame, k: int):
     fold_size = len(data) // k
     indices = np.arange(len(data))
     folds = []
     for i in range(k):
         test_indices = indices[i * fold_size: (i + 1) * fold_size]
         train_indices = np.concatenate([indices[:i * fold_size], indices[(i + 1) * fold_size:]])
         folds.append((train_indices, test_indices))
     return folds
 
 
def perfrom_KfoldCrossValidation(folds: list, data: pd.DataFrame, Model: Models, feature_states, evidence_features, target_features, **kwargs):

    full_logLikelihood_list = []
    correlation_accuracy_list = []
    
    # Iterate through each fold
    for train_indices, test_indices in tqdm(folds):
        training_data = data.iloc[train_indices]
        testing_data = data.iloc[test_indices]
        
        
        # Train the model on the training data
        model = Model(train_data=training_data, test_data=testing_data, feature_states=feature_states)
        model.set_evidence_features(evidence_features)
        model.set_target_list(target_features)
        if type(model) == BICBayesianNetwork:
            model.structure_learning()
        else:
            model.structure_learning(equivalent_sample_size = kwargs.get("SL_equivalent_sample_size"))
        model.parameter_estimator(prior_type = kwargs.get("prior_type"), pseudo_counts=kwargs.get('pseudo_counts'), equivalent_sample_size = kwargs.get('PE_equivalent_sample_size') )
        
        # evaluate of the testing data
        full_log_likelihood = model.evaluate(distribution="full")
        correlation_accuracy = model.evaluate(score="correlation", classification_metric="accuracy") 
        
        # Append the fold score to the list of scores
        full_logLikelihood_list.append(full_log_likelihood)
        
    mean_full_loglikelihood = np.mean(full_logLikelihood_list)
    return mean_full_loglikelihood