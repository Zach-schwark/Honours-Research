from Models import RandomBayesianNetwork,  BICBayesianNetwork, BDeuBayesianNetwork, BDsBayesianNetwork, k2BayesianNetwork
from Data.DataPreprocessing import DataPreprocessing


loaded_data = DataPreprocessing.load_data()
data = DataPreprocessing.preprocess_data(loaded_data)
feature_states = DataPreprocessing.get_feature_states(data)

print("#############\n")
print("Data loaded\n")

def return_evidence_features(list_description: str, inc_loan_amnt: bool):

    very_basic_evidence_features = ["annual_inc","emp_length", "grade", "verification_status","fico_range_high","purpose","dti", "home_ownership", "tot_cur_bal", "pub_rec_bankruptcies"]
    basic_evidence_features = ["annual_inc", "emp_length", "grade", "home_ownership", "verification_status", "last_fico_range_high", "fico_range_high", "purpose", "dti", "application_type", "delinq_2yrs", "avg_cur_bal", "tot_cur_bal", "pub_rec_bankruptcies", "mort_acc", "num_il_tl", "num_rev_accts", "total_bal_ex_mort"]
    more_detailed_evidence_features = ["annual_inc", "emp_length", "grade", "home_ownership", "verification_status", "last_fico_range_high", "fico_range_high", "purpose", "dti", "application_type", "delinq_2yrs", "avg_cur_bal", "tot_cur_bal", "pub_rec_bankruptcies", "mort_acc", "num_il_tl", "num_rev_accts", "total_bal_ex_mort", "revol_bal", "num_actv_rev_tl","num_op_rev_tl","max_bal_bc","total_rev_hi_lim","total_bal_il","open_acc","total_acc","tax_liens","pub_rec","num_bc_tl","earliest_cr_line","pct_tl_nvr_dlq","acc_now_delinq"]
    advanced_evidence_features =  ["annual_inc", "emp_length", "grade", "home_ownership", "verification_status", "last_fico_range_high", "fico_range_high", "purpose", "dti", "application_type", "delinq_2yrs", "avg_cur_bal", "tot_cur_bal", "pub_rec_bankruptcies", "mort_acc", "num_il_tl", "num_rev_accts", "total_bal_ex_mort", "revol_bal", "num_actv_rev_tl","num_op_rev_tl","max_bal_bc","total_rev_hi_lim","total_bal_il","open_acc","total_acc","tax_liens","pub_rec","num_bc_tl","earliest_cr_line","pct_tl_nvr_dlq","acc_now_delinq","revol_util","all_util","bc_util","total_cu_tl","total_bc_limit","num_actv_bc_tl","num_bc_sats","percent_bc_gt_75","num_tl_30dpd","num_tl_90g_dpd_24m","num_tl_120dpd_2m","num_accts_ever_120_pd"]
    all_customer_info_evidence_features =  ["annual_inc", "emp_length", "grade", "home_ownership", "verification_status", "last_fico_range_high", "fico_range_high", "purpose", "dti", "application_type", "delinq_2yrs", "avg_cur_bal", "tot_cur_bal", "pub_rec_bankruptcies", "mort_acc", "num_il_tl", "num_rev_accts", "total_bal_ex_mort", "revol_bal", "num_actv_rev_tl","num_op_rev_tl","max_bal_bc","total_rev_hi_lim","total_bal_il","open_acc","total_acc","tax_liens","pub_rec","num_bc_tl","earliest_cr_line","pct_tl_nvr_dlq","acc_now_delinq","revol_util","all_util","bc_util","total_cu_tl","total_bc_limit","num_actv_bc_tl","num_bc_sats","percent_bc_gt_75","num_tl_30dpd","num_tl_90g_dpd_24m","num_tl_120dpd_2m","num_accts_ever_120_pd","open_il_12m","open_il_24m","num_tl_op_past_12m","open_acc_6m","acc_open_past_24mths","open_rv_12m","open_rv_24m","mo_sin_rcnt_tl","mths_since_recent_bc","mo_sin_rcnt_rev_tl_op","mo_sin_old_rev_tl_op","mo_sin_old_il_acct","mths_since_recent_inq","inq_fi","inq_last_6mths","inq_last_12m","title","bc_open_to_buy"]
    
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


Random_full_distribution_log_liklihood_list = []
Random_desired_distribution_log_liklihood_list = []

BIC_full_distribution_log_liklihood_list = []
BIC_desired_distribution_log_liklihood_list = []

BDeu_full_distribution_log_liklihood_list = []
BDeu_desired_distribution_log_liklihood_list = []

BDs_full_distribution_log_liklihood_list = []
BDs_desired_distribution_log_liklihood_list = []

K2_full_distribution_log_liklihood_list = []
K2_desired_distribution_log_liklihood_list = []


for num_rows in range(1000,5000,1000):
    percent_complete = (num_rows/1000)*100
    print("#############\n")
    print("percent_complete: "+str(percent_complete)+"%\n")
    train_data, validation_data, test_data = DataPreprocessing.split_data(data,num_rows = num_rows)

    #Random_BN = RandomBayesianNetwork(train_data=train_data, test_data=validation_data, feature_states=feature_states)
    BIC_BN = BICBayesianNetwork(train_data=train_data, test_data=validation_data, feature_states=feature_states)
    BDeu_BN = BDeuBayesianNetwork(train_data=train_data, test_data=validation_data, feature_states=feature_states)
    BDs_BN = BDsBayesianNetwork(train_data=train_data, test_data=validation_data, feature_states=feature_states)
   #K2_BN = k2BayesianNetwork(train_data=train_data, test_data=validation_data, feature_states=feature_states)
    
    #Random_BN.set_evidence_features(evidence_features)
    BIC_BN.set_evidence_features(evidence_features)
    BDeu_BN.set_evidence_features(evidence_features)
    BDs_BN.set_evidence_features(evidence_features)
    #K2_BN.set_evidence_features(evidence_features)
    
    #Random_BN.set_target_list(target_features)
    BIC_BN.set_target_list(target_features)
    BDeu_BN.set_target_list(target_features)
    BDs_BN.set_target_list(target_features)
    #K2_BN.set_target_list(target_features)
    
    #Random_BN.structure_learning()
    BIC_BN.structure_learning()
    BDeu_BN.structure_learning()
    BDs_BN.structure_learning()
    #K2_BN.structure_learning()
    
    #Random_BN.parameter_estimator()
    BIC_BN.parameter_estimator()
    BDeu_BN.parameter_estimator()
    BDs_BN.parameter_estimator()
    #K2_BN.parameter_estimator()
    
    #Random_full_distribution_log_liklihood_list.append(Random_BN.evaluate(distribution="full"))
    BIC_full_distribution_log_liklihood_list.append(BIC_BN.evaluate(distribution="full"))
    BDeu_full_distribution_log_liklihood_list.append(BDeu_BN.evaluate(distribution="full"))
    BDs_full_distribution_log_liklihood_list.append(BDs_BN.evaluate(distribution="full"))
    #K2_full_distribution_log_liklihood_list.append(K2_BN.evaluate(distribution="full"))
    
    #Random_desired_distribution_log_liklihood_list.append(Random_BN.evaluate(distribution="desired"))
    BIC_desired_distribution_log_liklihood_list.append(BIC_BN.evaluate(distribution="desired"))
    BDeu_desired_distribution_log_liklihood_list.append(BDeu_BN.evaluate(distribution="desired"))
    BDs_desired_distribution_log_liklihood_list.append(BDs_BN.evaluate(distribution="desired"))
    #K2_desired_distribution_log_liklihood_list.append(K2_BN.evaluate(distribution="desired"))
    
print("Random_full_distribution_log_liklihood_list:", Random_full_distribution_log_liklihood_list)
print("Random_desired_distribution_log_liklihood_list:", Random_desired_distribution_log_liklihood_list)

print("BIC_full_distribution_log_liklihood_list:", BIC_full_distribution_log_liklihood_list)
print("BIC_desired_distribution_log_liklihood_list:", BIC_desired_distribution_log_liklihood_list)

print("BDeu_full_distribution_log_liklihood_list:", BDeu_full_distribution_log_liklihood_list)
print("BDeu_desired_distribution_log_liklihood_list:", BDeu_desired_distribution_log_liklihood_list)

print("BDs_full_distribution_log_liklihood_list:", BDs_full_distribution_log_liklihood_list)
print("BDs_desired_distribution_log_liklihood_list:", BDs_desired_distribution_log_liklihood_list)

print("K2_full_distribution_log_liklihood_list:", K2_full_distribution_log_liklihood_list)
print("K2_desired_distribution_log_liklihood_list:", K2_desired_distribution_log_liklihood_list)