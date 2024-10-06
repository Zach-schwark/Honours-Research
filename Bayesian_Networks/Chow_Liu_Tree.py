import sys
sys.path.insert(0,"./")
from Models import Chow_Liu_Tree
from Data.DataPreprocessing import DataPreprocessing
from pgmpy import config
import numpy as np
import pandas as pd
import torch
import logging
from pgmpy.global_vars import logger
logger.setLevel(logging.ERROR)

#device = "cuda" if torch.cuda.is_available() else "cpu"

#config.set_dtype(dtype=torch.float16)
#config.set_backend("torch", device=device, dtype=torch.float32)

config.set_dtype(dtype=np.float32)

with open("LogLikelihood_outputs/Chow_Liu_full_distribution.txt", "w") as file:
    file.write("")

with open("LogLikelihood_outputs/Chow_Liu_desired_distribution.txt", "w") as file:
    file.write("")
    
with open("Correlation_outputs/Chow_Liu_correlation_accuracy.txt", "w") as file:
    file.write("")

with open("Correlation_outputs/Chow_Liu_correlation_f1.txt", "w") as file:
    file.write("")
    

loaded_data: pd.DataFrame = DataPreprocessing.load_data()
data: pd.DataFrame = DataPreprocessing.preprocess_data(loaded_data)
feature_states = DataPreprocessing.get_feature_states(data)
#print(feature_states)

print("#############")
print("Data loaded")
print("#############\n")

def return_evidence_features(list_description: str, inc_loan_amnt: bool):

    credit_score = ["fico_range_high"]
    very_basic_evidence_features = ["annual_inc","emp_length", "grade", "verification_status","fico_range_high","purpose","dti", "home_ownership", "tot_cur_bal", "pub_rec_bankruptcies"]
    basic_evidence_features = ["annual_inc", "emp_length", "grade", "home_ownership", "verification_status", "last_fico_range_high", "fico_range_high", "purpose", "dti", "application_type", "delinq_2yrs", "avg_cur_bal", "tot_cur_bal", "pub_rec_bankruptcies", "mort_acc", "num_il_tl", "num_rev_accts", "total_bal_ex_mort"]
    more_detailed_evidence_features = ["annual_inc", "emp_length", "grade", "home_ownership", "verification_status", "last_fico_range_high", "fico_range_high", "purpose", "dti", "application_type", "delinq_2yrs", "avg_cur_bal", "tot_cur_bal", "pub_rec_bankruptcies", "mort_acc", "num_il_tl", "num_rev_accts", "total_bal_ex_mort", "revol_bal", "num_actv_rev_tl","num_op_rev_tl","max_bal_bc","total_rev_hi_lim","total_bal_il","open_acc","total_acc","tax_liens","pub_rec","num_bc_tl","earliest_cr_line","pct_tl_nvr_dlq","acc_now_delinq"]
    advanced_evidence_features =  ["annual_inc", "emp_length", "grade", "home_ownership", "verification_status", "last_fico_range_high", "fico_range_high", "purpose", "dti", "application_type", "delinq_2yrs", "avg_cur_bal", "tot_cur_bal", "pub_rec_bankruptcies", "mort_acc", "num_il_tl", "num_rev_accts", "total_bal_ex_mort", "revol_bal", "num_actv_rev_tl","num_op_rev_tl","max_bal_bc","total_rev_hi_lim","total_bal_il","open_acc","total_acc","tax_liens","pub_rec","num_bc_tl","earliest_cr_line","pct_tl_nvr_dlq","acc_now_delinq","revol_util","all_util","bc_util","total_cu_tl","total_bc_limit","num_actv_bc_tl","num_bc_sats","percent_bc_gt_75","num_tl_30dpd","num_tl_90g_dpd_24m","num_tl_120dpd_2m","num_accts_ever_120_pd"]
    all_customer_info_evidence_features =  ["annual_inc", "emp_length", "grade", "home_ownership", "verification_status", "last_fico_range_high", "fico_range_high", "purpose", "dti", "application_type", "delinq_2yrs", "avg_cur_bal", "tot_cur_bal", "pub_rec_bankruptcies", "mort_acc", "num_il_tl", "num_rev_accts", "total_bal_ex_mort", "revol_bal", "num_actv_rev_tl","num_op_rev_tl","max_bal_bc","total_rev_hi_lim","total_bal_il","open_acc","total_acc","tax_liens","pub_rec","num_bc_tl","earliest_cr_line","pct_tl_nvr_dlq","acc_now_delinq","revol_util","all_util","bc_util","total_cu_tl","total_bc_limit","num_actv_bc_tl","num_bc_sats","percent_bc_gt_75","num_tl_30dpd","num_tl_90g_dpd_24m","num_tl_120dpd_2m","num_accts_ever_120_pd","open_il_12m","open_il_24m","num_tl_op_past_12m","open_acc_6m","acc_open_past_24mths","open_rv_12m","open_rv_24m","mo_sin_rcnt_tl","mths_since_recent_bc","mo_sin_rcnt_rev_tl_op","mo_sin_old_rev_tl_op","mo_sin_old_il_acct","mths_since_recent_inq","inq_fi","inq_last_6mths","inq_last_12m","bc_open_to_buy"]
    
    evidence_features = []
    
    if list_description == "very basic":
        evidence_features = very_basic_evidence_features
    elif list_description == "basic":
        evidence_features = basic_evidence_features
    elif list_description == "detailed":
        evidence_features = more_detailed_evidence_features
    elif list_description == "advanced":
        evidence_features = advanced_evidence_features
    elif list_description == "all info":
        evidence_features = all_customer_info_evidence_features
    elif list_description == "credit score":
        evidence_features = credit_score

    # this will result in the loan amount being the original loan amount for each data point
    if inc_loan_amnt == True:
        evidence_features.append('loan_amnt')
   
    return evidence_features
 
 
def return_target_features(inc_loan_amnt: bool, add_targets: str| list | None = None):
    loan_structure_target_list = ["int_rate","term","installment"] 
    
    # this will result in the model predicting the most likely loan amount for the borrower
    if inc_loan_amnt == True:
        loan_structure_target_list.append('loan_amnt')

    if add_targets != None:
        if type(add_targets) == list:
            loan_structure_target_list.extend(add_targets)
        elif type(add_targets) == str:
            loan_structure_target_list.append(add_targets)
        
    return loan_structure_target_list


evidence_features = return_evidence_features(list_description="basic", inc_loan_amnt=False)
target_features = return_target_features(inc_loan_amnt=True)


Tree_full_distribution_log_liklihood_list = []
Tree_desired_distribution_log_liklihood_list = []
Tree_correlation_accuracy_list = []
Tree_correlation_f1_list = []

num_datapoints = []
num_rows = int(10000)

#for num_rows in range(1000,2000,500):
#num_datapoints.append(num_rows)
#percent_complete = (num_rows/3000)*100
#print("#############\n")
#print("percent_complete: "+str(percent_complete)+"%\n")
train_data, validation_data, test_data = DataPreprocessing.split_data(data,num_rows = num_rows)
Tree = Chow_Liu_Tree(train_data=train_data, test_data=validation_data, feature_states=feature_states)
Tree.set_evidence_features(evidence_features)
Tree.set_target_list(target_features)
Tree.structure_learning()
Tree.parameter_estimator()


full_log_likelihood = Tree.evaluate(distribution="full")
Tree_full_distribution_log_liklihood_list.append(full_log_likelihood)
with open("LogLikelihood_outputs/Chow_Liu_full_distribution.txt", "a") as file:
    file.write(str(full_log_likelihood)+",")
    
desired_log_likelihood = Tree.evaluate(distribution="desired")
Tree_desired_distribution_log_liklihood_list.append(desired_log_likelihood)
with open("LogLikelihood_outputs/Chow_Liu_desired_distribution.txt", "a") as file:
    file.write(str(desired_log_likelihood)+",")
    
correlation_accuracy = Tree.evaluate(score="correlation", classification_metric="accuracy")    
Tree_correlation_accuracy_list.append(correlation_accuracy)
with open("Correlation_outputs/Chow_Liu_correlation_accuracy.txt", "a") as file:
    file.write(str(correlation_accuracy)+",")

correlation_f1 = Tree.evaluate(score="correlation", classification_metric="f1")
Tree_correlation_f1_list.append(correlation_f1)
with open("Correlation_outputs/Chow_Liu_correlation_f1.txt", "a") as file:
    file.write(str(correlation_f1)+",")

    
Tree.draw_graph(name= "Chow-Liu Tree",file_name="Tree_graph", save=True, show=False)
 
    