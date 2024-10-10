import sys
sys.path.insert(0,"./")
from Models import RandomBayesianNetwork,  BICBayesianNetwork, BDeuBayesianNetwork, BDsBayesianNetwork, k2BayesianNetwork
from Data.DataPreprocessing import DataPreprocessing
from pgmpy import config
import numpy as np
import pandas as pd
import torch
import logging
from tqdm import tqdm
from pgmpy.global_vars import logger
logger.setLevel(logging.ERROR)

#device = "cuda" if torch.cuda.is_available() else "cpu"

#config.set_dtype(dtype=torch.float16)
#config.set_backend("torch", device=device, dtype=torch.float32)

config.set_dtype(dtype=np.float32)

with open("Fine_Tuning/bic_finetune_dirichlet.txt", "w") as file:
    file.write("")

with open("LogLikelihood_outputs/BIC_full_distribution.txt", "w") as file:
    file.write("")
    
with open("LogLikelihood_outputs/BIC_desired_distribution.txt", "w") as file:
    file.write("")
    
with open("Correlation_outputs/BIC_correlation_accuracy.txt", "w") as file:
    file.write("")

with open("Correlation_outputs/BIC_correlation_f1.txt", "w") as file:
    file.write("")

loaded_data: pd.DataFrame = DataPreprocessing.load_data()
data: pd.DataFrame = DataPreprocessing.preprocess_data(loaded_data)
feature_states = DataPreprocessing.get_feature_states(data)
#print(feature_states)

print("#############")
print("Data loaded")
print("#############\n")

def return_evidence_features(list_description: str, inc_loan_amnt: bool):

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


BIC_full_distribution_log_liklihood_list = []
BIC_desired_distribution_log_liklihood_list = []
BIC_correlation_accuracy_list = []
BIC_correlation_f1_list = []

num_datapoints = []
num_rows = int(50000)

pseudo_counts = [1,2,4,6,7,8,9,10,11,12]



for num_row in tqdm(range(1000,150000,10000)):
    with open("Fine_Tuning/bic_finetune_dirichlet.txt", "a") as file:
        file.write("\n"+str(num_row)+" Lines:\n")
    for pseudo_count in pseudo_counts:
        print("pseudo count: "+str(pseudo_count))
        train_data, validation_data, test_data = DataPreprocessing.split_data(data,num_rows = num_row)
        BIC_BN = BICBayesianNetwork(train_data=train_data, test_data=validation_data, feature_states=feature_states)
        BIC_BN.set_evidence_features(evidence_features)
        BIC_BN.set_target_list(target_features)
        BIC_BN.structure_learning()
        BIC_BN.parameter_estimator(prior_type = "Dirichlet", pseudo_counts=pseudo_count)
        with open("Fine_Tuning/bic_finetune_dirichlet.txt", "a") as file:
            file.write("pseudo count=" + str(pseudo_count)+"\n")
        full_log_likelihood = BIC_BN.evaluate(distribution="full")
        correlation_accuracy = BIC_BN.evaluate(score="correlation", classification_metric="accuracy") 
        with open("Fine_Tuning/bic_finetune_dirichlet.txt", "a") as file:
            file.write("full LL: "+str(full_log_likelihood)+"\t Correlation accuracy: "+str(correlation_accuracy)+"\n")

#full_log_likelihood = BIC_BN.evaluate(distribution="full")
#BIC_full_distribution_log_liklihood_list.append(full_log_likelihood)
#with open("LogLikelihood_outputs/BIC_full_distribution.txt", "a") as file:
#    file.write(str(full_log_likelihood)+",")
#    
#desired_log_likelihood = BIC_BN.evaluate(distribution="desired")
#BIC_desired_distribution_log_liklihood_list.append(desired_log_likelihood)
#with open("LogLikelihood_outputs/BIC_desired_distribution.txt", "a") as file:
#    file.write(str(desired_log_likelihood)+",")
#    
#correlation_accuracy = BIC_BN.evaluate(score="correlation", classification_metric="accuracy")    
#BIC_correlation_accuracy_list.append(correlation_accuracy)
#with open("Correlation_outputs/BIC_correlation_accuracy.txt", "a") as file:
#    file.write(str(correlation_accuracy)+",")
#
#correlation_f1 = BIC_BN.evaluate(score="correlation", classification_metric="f1")
#BIC_correlation_f1_list.append(correlation_f1)
#with open("Correlation_outputs/BIC_correlation_f1.txt", "a") as file:
#    file.write(str(correlation_f1)+",")
    
    
#BIC_BN.draw_graph(name= "Bayesian Network with BIC score",file_name="BIC_graph", save=True, show=False)
 