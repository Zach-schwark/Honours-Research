import sys
sys.path.insert(0,"./")
from Models import BICBayesianNetwork, k2BayesianNetwork, Chow_Liu_Tree, RandomBayesianNetwork
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
 
 
def perfrom_KfoldCrossValidation(folds: list, data: pd.DataFrame, Model: Models, feature_states, evidence_features, target_features, desired: bool, **kwargs):

    full_logLikelihood_list = []
    desired_log_likelihood_list = []
    
    # Iterate through each fold
    for train_indices, test_indices in tqdm(folds):
        training_data = data.iloc[train_indices]
        testing_data = data.iloc[test_indices]
        
        
        # Train the model on the training data
        model = Model(train_data=training_data, test_data=testing_data, feature_states=feature_states)
        model.set_evidence_features(evidence_features)
        model.set_target_list(target_features)
        if type(model) == BICBayesianNetwork or k2BayesianNetwork or Chow_Liu_Tree or RandomBayesianNetwork:
            model.structure_learning()
        else:
            model.structure_learning(equivalent_sample_size = kwargs.get("SL_equivalent_sample_size"))
        #model.draw_graph(name="Random", file_name= "Random_graph",save = True, show = False)
        if type(model) == Chow_Liu_Tree:
            model.parameter_estimator()
        else:
            model.parameter_estimator(prior_type = kwargs.get("prior_type"), pseudo_counts=kwargs.get('pseudo_counts'), equivalent_sample_size = kwargs.get('PE_equivalent_sample_size') )
        
        # evaluate of the testing data
        full_log_likelihood = model.evaluate(distribution="full")
        full_logLikelihood_list.append(full_log_likelihood)
        if desired == True:
            desired_log_likelihood = model.evaluate(distribution="desired")
            desired_log_likelihood_list.append(desired_log_likelihood)
        
        
    mean_full_loglikelihood = np.mean(full_logLikelihood_list)    
    if desired == True:
        mean_desired_loglikelihood = np.mean(desired_log_likelihood_list)
        return mean_full_loglikelihood, mean_desired_loglikelihood
    else:
        return mean_full_loglikelihood