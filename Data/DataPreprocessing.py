# imports
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import math


class DataPreprocessing:
    
    def load_data(num_rows: int)-> pd.DataFrame:
        # reads from CS, removes rows with null/missing values and automatically infers and converts datatypes for the data.
        
        data = pd.read_csv("Data/accepted_2007_to_2018Q4.csv", engine='c', nrows = num_rows)
        data = data.drop(['id', 'member_id', 'settlement_term','settlement_percentage', 'settlement_amount', 'settlement_date','settlement_status', 'debt_settlement_flag_date', 'hardship_last_payment_amount', 'hardship_payoff_balance_amount', 'orig_projected_additional_accrued_interest',
               'hardship_loan_status', 'hardship_dpd', 'hardship_length','payment_plan_start_date','hardship_end_date', 'hardship_start_date', 'hardship_amount', 'deferral_term', 'hardship_status', 'hardship_reason', 'hardship_type',
               'sec_app_mths_since_last_major_derog', 'sec_app_collections_12_mths_ex_med', 'sec_app_chargeoff_within_12_mths', 'sec_app_num_rev_accts', 'sec_app_open_act_il', 'sec_app_revol_util', 'sec_app_open_acc', 'sec_app_mort_acc',
               'sec_app_inq_last_6mths', 'sec_app_earliest_cr_line', 'sec_app_fico_range_high', 'sec_app_fico_range_low', 'verification_status_joint', 'dti_joint', 'annual_inc_joint', 'desc', 'url', 'revol_bal_joint','mths_since_last_record', 'mths_since_recent_bc_dlq', 'mths_since_last_major_derog', 'mths_since_recent_revol_delinq', 'next_pymnt_d',
               'il_util', 'mths_since_rcnt_il' ], axis=1)
        data = data.dropna()
        data.convert_dtypes()
        return data
        
        
    def normalize_data(data: pd.DataFrame):
        print(type(data))
        normalized_data = data.copy()
        for column  in normalized_data.columns:
            if normalized_data[column].dtype == np.float64:
                normalized_data[column] = MinMaxScaler().fit_transform(np.array(normalized_data[column]).reshape(-1,1)) 
        return normalized_data
    
    def discretise_data(data: pd.DataFrame):
        discretised_data = data.copy()
        for column  in discretised_data.columns:
            if discretised_data[column].dtype == np.float64:
                discretised_data[column] = pd.cut(discretised_data[column], bins= 10, labels= [0,1,2,3,4,5,6,7,8,9])
        return discretised_data
    
    def preprocess_data(data: pd.DataFrame):
        #normalizes and discretises data
        normalized_data = DataPreprocessing.normalize_data(data)
        discretised_data = DataPreprocessing.discretise_data(normalized_data)
        return discretised_data
    
    def split_data(data: pd.DataFrame):
        # splits data into 75% train and 25% test
        train = data[0:(math.floor(0.75*data.shape[0]))]
        test = data[(math.floor(0.75*data.shape[0]))+1:data.shape[0]]
        
        return train, test
    
    def get_evidence_list(test_data, target_label):
        # gets the evidence list of the testing data to use as evidence when classifying loan status
        test_temp_df = test_data.copy()
        del test_temp_df[target_label]
        testing_evidence_list = []
        for i in range(len(test_temp_df)):
            testing_evidence_dict = {}
            for z in range(len(test_temp_df.columns.values.tolist())):
                testing_evidence_dict[test_temp_df.columns.values.tolist()[z]] = test_temp_df[test_temp_df.columns.values.tolist()[z]].iloc[i]
            testing_evidence_list.append(testing_evidence_dict)
        
        return testing_evidence_list