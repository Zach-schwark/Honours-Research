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
import warnings 
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
 
 
def perfrom_KfoldCrossValidation(folds: list, data: pd.DataFrame, Model: Models, feature_states, evidence_features, target_features, desired: bool, draw: bool = False, learn_parmeters: bool = True, evaluate: bool = True,  **kwargs) -> tuple | None:

    full_logLikelihood_list = []
    desired_log_likelihood_list = []
    graph_num = 0
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
        
        if draw == True:
            model.draw_graph(name=kwargs.get('graph_name')+"_"+str(graph_num), file_name= kwargs.get('graph_file_name')+"_"+str(graph_num), save = kwargs.get('graph_save'), show = kwargs.get('graph_show'))
            graph_num +=1
            
        if learn_parmeters:
            if type(model) == Chow_Liu_Tree:
                model.parameter_estimator()
            else:
                model.parameter_estimator(prior_type = kwargs.get("prior_type"), pseudo_counts=kwargs.get('pseudo_counts'), equivalent_sample_size = kwargs.get('PE_equivalent_sample_size') )
        
        if evaluate:
            # evaluate of the testing data
            full_log_likelihood = model.evaluate(distribution="full")
            full_logLikelihood_list.append(full_log_likelihood)
            if desired == True:
                try:
                    #print("her")
                    desired_log_likelihood = model.evaluate(distribution="desired")
                    #print(desired_log_likelihood)
                    if np.isnan(desired_log_likelihood) == False:
                        print(desired_log_likelihood)
                        desired_log_likelihood_list.append(desired_log_likelihood)
                except:
                    warnings.warn('Could not evaluate desired distribution. Problem could be in Variable Elimination where a certain node was not in the graph.') 
                    continue
    
    if evaluate:          
        mean_full_loglikelihood = np.mean(full_logLikelihood_list)    
        if desired == True:
            mean_desired_loglikelihood = np.mean(desired_log_likelihood_list)
            return mean_full_loglikelihood, mean_desired_loglikelihood
        else:
            return mean_full_loglikelihood, None
    else:
        return None, None