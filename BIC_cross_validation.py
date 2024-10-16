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
from pgmpy.global_vars import logger
logger.setLevel(logging.ERROR)

config.set_dtype(dtype=np.float32)

loaded_data: pd.DataFrame = DataPreprocessing.load_data()
data: pd.DataFrame = DataPreprocessing.preprocess_data(loaded_data)
feature_states = DataPreprocessing.get_feature_states(data)
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

train_data, test_data = DataPreprocessing.split_data(data, num_rows = 10000)

folds = CrossValidation.kfold_indices(data = train_data, k = 5 )
log_likelihood = CrossValidation.perfrom_KfoldCrossValidation(folds = folds, data=train_data, Model = BICBayesianNetwork, feature_states=feature_states, evidence_features=evidence_features, target_features=target_features, prior_type = "dirichlet", pseudo_counts = 1)
print(log_likelihood)
