import numpy as np
import pandas as pd
import networkx as nx
from matplotlib import pyplot as plt
from pgmpy.models import BayesianNetwork
from pgmpy.base import DAG
from pgmpy.metrics import log_likelihood_score
from pgmpy.inference import VariableElimination
from pgmpy import estimators
from Data.DataPreprocessing import DataPreprocessing
from pgmpy.utils import compat_fns
from abc import ABC, abstractmethod
from pgmpy import config
import torch
from tqdm import tqdm
#device = "cuda" if torch.cuda.is_available() else "cpu"

#config.set_dtype(dtype=torch.float16)
#config.set_backend("torch", device=device, dtype=torch.float32)#

config.set_dtype(dtype=np.float16)

class Models(ABC):
    
    def __init__(self, train_data, test_data, feature_states) -> None:
        self.model: BayesianNetwork
        self.target_list: list = ["int_rate","term","installment","loan_amnt"]
        self.evidence_features: list = ["annual_inc", "emp_length", "grade", "home_ownership", "verification_status", "last_fico_range_high", "fico_range_high", "purpose", "dti", "application_type", "delinq_2yrs", "avg_cur_bal", "tot_cur_bal", "pub_rec_bankruptcies", "mort_acc", "num_il_tl", "num_rev_accts", "total_bal_ex_mort"]
        self.train_data = train_data
        self.test_data = test_data
        self.feature_states = feature_states

    def set_target_list(self, target_list: list):
        self.target_list = target_list
        
    def set_evidence_features(self, evidence_features: list):
        self.evidence_features = evidence_features
    
    @abstractmethod
    def structure_learning(self):
        active_trail_nodes = self.model.active_trail_nodes('loan_status')['loan_status']
        active_trail_nodes_list = list(active_trail_nodes)
        original_nodes = list(self.model.nodes())
        for node in original_nodes:
            if node not in active_trail_nodes_list:
                self.model.remove_node(node)
    
    def draw_graph(self, name: str, file_name: str, save: bool, show: bool):
        active_trail_nodes = self.model.active_trail_nodes('loan_status')['loan_status']
        active_trail_nodes_list = list(active_trail_nodes)
        original_nodes = list(self.model.nodes())
        for node in original_nodes:
            if node not in active_trail_nodes_list:
                self.model.remove_node(node)
        
        
        nx_graph = nx.DiGraph(self.model.edges())
        pos = nx.spring_layout(nx_graph,2)
        fig, ax = plt.subplots(ncols=1, figsize=(20, 20))
        nx.draw(nx_graph, pos, with_labels=True, node_size=1000, node_color = 'skyblue', edge_color='#424242',font_size=15,font_color='black')
        ax.set_title(name)
        if save == True:
            plt.savefig("Graphics/BN_graphs/"+file_name)
        if show == True:
            plt.show()
    
    def parameter_estimator(self, prior_type: str = "BDeu", equivalent_sample_size: int = 5, pseudo_counts: dict | int = None):
        if prior_type == "dirichlet" and pseudo_counts == None:
            raise ValueError("pseudo_counts needs to be given if prior_type == 'dirichlet'.")
        
        if prior_type == 'BDeu' and equivalent_sample_size == None:
            raise ValueError("equivalent_sample_size needs to be given if prior_type == 'BDeu'.")
        
        parameter_estimator = estimators.BayesianEstimator(self.model, self.train_data, state_names = self.feature_states)
        parameters = parameter_estimator.get_parameters(prior_type=prior_type,equivalent_sample_size = equivalent_sample_size, pseudo_counts = pseudo_counts,  n_jobs=6)
 
        for i in range(len(parameters)):
            self.model.add_cpds(parameters[i])
    
    def __perform_inference_probability(self, target_list: list, evidence_list: list):
        predicted_max_probabilities = []
        print("Performing Variable Elimination...")
        inference = VariableElimination(self.model)
        for i in tqdm(range(len(evidence_list))):
            posterior_distribution = inference.query(variables = target_list, evidence=evidence_list[i], elimination_order="MinFill", joint=True, show_progress= False )
            #argmax = compat_fns.argmax(posterior_distribution.values)
            #assignment = posterior_distribution.assignment([argmax])[0]
            max = compat_fns.max(posterior_distribution.values)
            predicted_max_probabilities.append(max)
        return predicted_max_probabilities

    def __perform_inference_assignment(self, target_list: list, evidence_list: list):
        predicted_values = []
        print("Performing Variable Elimination...")
        inference = VariableElimination(self.model)
        for i in tqdm(range(len(evidence_list))):        
            target_variables_result = inference.map_query(target_list, evidence = evidence_list[i], elimination_order="MinFill", show_progress= False) 
            predicted_values.append(target_variables_result)
        return predicted_values
    
    def inference(self, return_type: str):
        removed_attributes = set()
        # get datapoints for the evidence
        validation_evidence_list = DataPreprocessing.get_evidence_list(test_data = self.test_data, target_label_list=self.target_list, evidence_features=self.evidence_features)
        # clean the evidence:
        # remove evidence features that are not in the Bayesian Network
        for i in range(len(validation_evidence_list)):
            for attribute in list(validation_evidence_list[i].keys()):
                if attribute not in self.model.nodes():
                    removed_attributes.add(attribute)
                    del validation_evidence_list[i][attribute]
        
        if return_type == "probability":
            return self.__perform_inference_probability(target_list=self.target_list, evidence_list=validation_evidence_list)
        elif return_type == "assignment":
            return self.__perform_inference_assignment(target_list=self.target_list, evidence_list=validation_evidence_list)
        else:
            raise ValueError('invalid argument for return_type, must be either "probability" or "assignment".')
        
    def __evaluate_full_distribution(self):
        difference = list(set(self.test_data.columns) - set(self.model.nodes()))
        missing_features = []
        for missing_feature in difference:
            missing_features.append(missing_feature)
            
        data_removed_missing_features = self.test_data.drop(missing_features, axis=1, inplace=False)
        
        log_likelihood = log_likelihood_score(self.model, data_removed_missing_features)
        
        return log_likelihood
    
    def __evaluate_desired_distribution(self):
        map_probabilities = self.inference(return_type = "probability")  
        map_probabilities = np.array(map_probabilities)
        log_probabilities = np.log(map_probabilities)

        log_likelihood = np.sum(log_probabilities)
        
        return log_likelihood
    
    def evaluate(self, distribution:str):
        if distribution == "full":
            return self.__evaluate_full_distribution()
        elif distribution == "desired":
            return self.__evaluate_desired_distribution()
        else:
            raise ValueError('invalid argument for distribution, must be either "full" or "desired".')
        
    def train(self):
        self.structure_learning()
        self.parameter_estimator()
        

class RandomBayesianNetwork(Models):
    
    def __init__(self, train_data, test_data, feature_states) -> None:
        super().__init__(train_data, test_data, feature_states)
        
    def set_target_list(self, target_list: list):
        return super().set_target_list(target_list)

    def set_evidence_features(self, evidence_features: list):
        return super().set_evidence_features(evidence_features)

    def draw_graph(self,name:str, file_name: str, save: bool, show: bool):
        return super().draw_graph(name, file_name, save, show)
    
    def inference(self, return_type: str):
        return super().inference(return_type)
    
    def evaluate(self, distribution: str):
        return super().evaluate(distribution)

    def structure_learning(self):
        self.model = BayesianNetwork()
        Random_Dag = DAG.get_random(n_nodes = len(self.train_data.columns.to_list()), node_names=self.train_data.columns.to_list(), edge_prob=0.05)
        self.model.add_nodes_from(self.train_data.columns.to_list())
        self.model.add_edges_from(Random_Dag.edges())

        active_trail_nodes = self.model.active_trail_nodes(['loan_status',"int_rate","term","installment", "loan_amnt"])
        active_trail_nodes_list = list(active_trail_nodes['loan_status'])
        active_trail_nodes_list.extend(active_trail_nodes['int_rate'])
        active_trail_nodes_list.extend(active_trail_nodes['term'])
        active_trail_nodes_list.extend(active_trail_nodes['installment'])
        active_trail_nodes_list.extend(active_trail_nodes['loan_amnt'])
        original_nodes = list(self.model.nodes())
        for node in original_nodes:
            if node not in active_trail_nodes_list:
                self.model.remove_node(node)
    
    def parameter_estimator(self, prior_type: str= "BDeu", equivalent_sample_size: int = 5, pseudo_counts: dict | int = None):
        return super().parameter_estimator(prior_type, equivalent_sample_size, pseudo_counts)

class BICBayesianNetwork(Models):
    
    def __init__(self, train_data, test_data, feature_states) -> None:
        super().__init__(train_data, test_data, feature_states)
        pass
    
    def set_target_list(self, target_list: list):
        return super().set_target_list(target_list)

    def set_evidence_features(self, evidence_features: list):
        return super().set_evidence_features(evidence_features)

    def draw_graph(self,name:str, file_name: str, save: bool, show: bool):
        return super().draw_graph(name, file_name, save, show)
    
    def inference(self, return_type: str):
        return super().inference(return_type)
    
    def evaluate(self, distribution: str):
        return super().evaluate(distribution)
    
    def structure_learning(self):
        scoring_method = estimators.BicScore(data=self.train_data)
        est = estimators.HillClimbSearch(data=self.train_data, use_cache = True)
        estimated_model = est.estimate(scoring_method=scoring_method, max_iter=int(1e3))
        self.model = BayesianNetwork(estimated_model.edges())
        self.model.add_nodes_from(estimated_model.nodes())
        super().structure_learning()
        
    def parameter_estimator(self, prior_type: str= "BDeu", equivalent_sample_size: int = 5, pseudo_counts: dict | int = None):
        return super().parameter_estimator(prior_type, equivalent_sample_size, pseudo_counts)
            
class BDeuBayesianNetwork(Models):
        
    def __init__(self, train_data, test_data, feature_states) -> None:
        super().__init__(train_data, test_data, feature_states)
        pass
    
    def set_target_list(self, target_list: list):
        return super().set_target_list(target_list)

    def set_evidence_features(self, evidence_features: list):
        return super().set_evidence_features(evidence_features)

    def draw_graph(self,name:str, file_name: str, save: bool, show: bool):
        return super().draw_graph(name, file_name, save, show)
    
    def inference(self, return_type: str):
        return super().inference(return_type)
    
    def evaluate(self, distribution: str):
        return super().evaluate(distribution)
    
    def structure_learning(self, equivalent_sample_size = 10):
        scoring_method = estimators.BDeuScore(data=self.train_data, equivalent_sample_size=equivalent_sample_size)  # TODO change sample size hyperparameter
        est = estimators.HillClimbSearch(data=self.train_data, use_cache = True)
        estimated_model = est.estimate(
            scoring_method=scoring_method, max_iter=int(1e2), max_indegree=3)

        self.model = BayesianNetwork(estimated_model.edges())
        self.model.add_nodes_from(estimated_model.nodes())
        super().structure_learning()
        
    def parameter_estimator(self, prior_type: str= "BDeu", equivalent_sample_size: int = 5, pseudo_counts: dict | int = None):
        return super().parameter_estimator(prior_type, equivalent_sample_size, pseudo_counts)
        
class BDsBayesianNetwork(Models):
    
    def __init__(self, train_data, test_data, feature_states) -> None:
        super().__init__(train_data, test_data, feature_states)
        pass

    def set_target_list(self, target_list: list):
        return super().set_target_list(target_list)

    def set_evidence_features(self, evidence_features: list):
        return super().set_evidence_features(evidence_features)

    def draw_graph(self,name:str, file_name: str, save: bool, show: bool):
        return super().draw_graph(name, file_name, save, show)
    
    def inference(self, return_type: str):
        return super().inference(return_type)
    
    def evaluate(self, distribution: str):
        return super().evaluate(distribution)

    def structure_learning(self, equivalent_sample_size=10):
        scoring_method = estimators.BDsScore(data=self.train_data,equivalent_sample_size=equivalent_sample_size) # TODO change sample size hyperparameter
        est = estimators.HillClimbSearch(data=self.train_data, use_cache = True)
        estimated_model = est.estimate(scoring_method=scoring_method, max_iter=int(1e3),  max_indegree=3)
        self.model = BayesianNetwork(estimated_model.edges())
        self.model.add_nodes_from(estimated_model.nodes())
        super().structure_learning()
        
    def parameter_estimator(self, prior_type: str= "BDeu", equivalent_sample_size: int = 5, pseudo_counts: dict | int = None):
        return super().parameter_estimator(prior_type, equivalent_sample_size, pseudo_counts)
    
class k2BayesianNetwork(Models):
    
    def __init__(self, train_data, test_data, feature_states) -> None:
        super().__init__(train_data, test_data, feature_states)
        pass
    
    def set_target_list(self, target_list: list):
        return super().set_target_list(target_list)

    def set_evidence_features(self, evidence_features: list):
        return super().set_evidence_features(evidence_features)

    def draw_graph(self,name:str, file_name: str, save: bool, show: bool):
        return super().draw_graph(name, file_name, save, show)
    
    def inference(self, return_type: str):
        return super().inference(return_type)
    
    def evaluate(self, distribution: str):
        return super().evaluate(distribution)
    
    def structure_learning(self):
        scoring_method = estimators.K2Score(data=self.train_data)
        est = estimators.HillClimbSearch(data=self.train_data, use_cache = True)
        estimated_model = est.estimate(
            scoring_method=scoring_method, max_iter=int(1e3), max_indegree=3)
        self.model = BayesianNetwork(estimated_model.edges())
        self.model.add_nodes_from(estimated_model.nodes())
        super().structure_learning()
        
    def parameter_estimator(self, prior_type: str= "BDeu", equivalent_sample_size: int = 5, pseudo_counts: dict | int = None):
        return super().parameter_estimator(prior_type, equivalent_sample_size, pseudo_counts)