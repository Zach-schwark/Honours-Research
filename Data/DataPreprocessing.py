# imports
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, KBinsDiscretizer
from sklearn.model_selection import train_test_split
import math


class DataPreprocessing:
    
    def load_data()-> pd.DataFrame:
        # reads from CS, removes rows with null/missing values and automatically infers and converts datatypes for the data.
        
        data = pd.read_csv("Data/accepted_2007_to_2018Q4.csv", engine='c')
        data = data.drop(['id', 'member_id', 'settlement_term','settlement_percentage', 'settlement_amount', 'settlement_date','settlement_status', 'debt_settlement_flag_date', 'hardship_last_payment_amount', 'hardship_payoff_balance_amount', 'orig_projected_additional_accrued_interest',
           'hardship_loan_status', 'hardship_dpd', 'hardship_length','payment_plan_start_date','hardship_end_date', 'hardship_start_date', 'hardship_amount', 'deferral_term', 'hardship_status', 'hardship_reason', 'hardship_type',
           'sec_app_mths_since_last_major_derog', 'sec_app_collections_12_mths_ex_med', 'sec_app_chargeoff_within_12_mths', 'sec_app_num_rev_accts', 'sec_app_open_act_il', 'sec_app_revol_util', 'sec_app_open_acc', 'sec_app_mort_acc',
           'sec_app_inq_last_6mths', 'sec_app_earliest_cr_line', 'sec_app_fico_range_high', 'sec_app_fico_range_low', 'verification_status_joint', 'dti_joint', 'annual_inc_joint', 'desc', 'url', 'revol_bal_joint','mths_since_last_record', 'mths_since_recent_bc_dlq', 'mths_since_last_major_derog', 'mths_since_recent_revol_delinq', 'next_pymnt_d',
           'il_util', 'mths_since_rcnt_il','mths_since_last_delinq', 'zip_code', 'last_pymnt_d','emp_title', 'funded_amnt', 'funded_amnt_inv', 'sub_grade', 'collection_recovery_fee', 'fico_range_low', 'num_sats', 'total_pymnt_inv', 'total_rec_prncp', 'tot_hi_cred_lim', 'total_il_high_credit_limit', 'num_rev_tl_bal_gt_0',
           'last_fico_range_low'], axis=1)


        # drop rows that had more than 12 or more missing values
        data_droppedna = data.dropna(thresh=83)
        data_droppedna.convert_dtypes()
        return data_droppedna
        
        
    
    def discretise_data(data: pd.DataFrame):

        discretise_data = data.copy() 

        standard_num_bins = 5

        discretized = pd.cut(discretise_data['loan_amnt'].dropna(), bins= standard_num_bins)
        discretized = pd.Series(discretized, index= discretise_data['loan_amnt'].dropna().index)
        discretized_full = pd.Series('NaN', index= discretise_data['loan_amnt'].index)
        discretized_full.update(discretized)
        discretise_data['loan_amnt'] = discretized_full


        discretized = pd.cut(discretise_data['int_rate'].dropna(), bins= standard_num_bins)
        discretized = pd.Series(discretized, index=discretise_data['int_rate'].dropna().index)
        discretized_full = pd.Series('NaN', index= discretise_data['int_rate'].index)
        discretized_full.update(discretized)
        discretise_data['int_rate'] = discretized_full

        discretized = pd.cut(discretise_data['installment'].dropna(), bins= standard_num_bins)
        discretized = pd.Series(discretized, index=discretise_data['installment'].dropna().index)
        discretized_full = pd.Series('NaN', index= discretise_data['installment'].index)
        discretized_full.update(discretized)
        discretise_data['installment'] = discretized_full

        discretized = discretise_data['emp_length'].dropna()
        discretized = pd.Series(discretized, index=discretise_data['emp_length'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['emp_length'].index)
        discretized_full.update(discretized)
        discretise_data['emp_length'] = discretized_full

        discretized = discretise_data['home_ownership'].dropna()
        discretized = pd.Series(discretized, index=discretise_data['home_ownership'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['home_ownership'].index)
        discretized_full.update(discretized)
        discretise_data['home_ownership'] = discretized_full

        est = KBinsDiscretizer(n_bins= standard_num_bins, encode='ordinal', strategy='kmeans',subsample=200_000)
        annual_inc_dataframe =  np.array([discretise_data['annual_inc'].dropna().to_numpy()]).transpose()
        est.fit(annual_inc_dataframe)
        annual_inc_dataframe = est.transform(annual_inc_dataframe)
        discretized = pd.Series(annual_inc_dataframe.reshape(-1), index=discretise_data['annual_inc'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['annual_inc'].index)
        discretized_full.update(discretized)
        discretise_data['annual_inc'] = discretized_full

        discretized = discretise_data['verification_status'].dropna()
        discretized = pd.Series(discretized, index=discretise_data['verification_status'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['verification_status'].index)
        discretized_full.update(discretized)
        discretise_data['verification_status'] = discretized_full


        discretise_data['issue_d'] = pd.to_datetime(discretise_data['issue_d'], format='%b-%Y')
        discretise_data['issue_d'] = discretise_data['issue_d'].dt.year.astype(int)
        discretized = discretise_data['issue_d'].dropna()
        discretized = pd.Series(discretized, index=discretise_data['issue_d'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['issue_d'].index)
        discretized_full.update(discretized)
        discretise_data['issue_d'] = discretized_full

        discretise_data['loan_status'] = discretise_data['loan_status'].apply(lambda x: 'Fully Paid' if 'Fully Paid' in x else x)

        values_to_keep = ['Fully Paid', 'Charged Off']
        pattern = '|'.join(values_to_keep)
        discretise_data = discretise_data[discretise_data['loan_status'].str.contains(pattern)]

        discretized = discretise_data['pymnt_plan'].dropna()
        discretized = pd.Series(discretized, index=discretise_data['pymnt_plan'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['pymnt_plan'].index)
        discretized_full.update(discretized)
        discretise_data['pymnt_plan'] = discretized_full

        discretized = discretise_data['purpose'].dropna()
        discretized = pd.Series(discretized, index=discretise_data['purpose'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['purpose'].index)
        discretized_full.update(discretized)
        discretise_data['purpose'] = discretized_full

        discretized = discretise_data['title'].dropna()
        discretized = pd.Series(discretized, index=discretise_data['title'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['title'].index)
        discretized_full.update(discretized)
        discretise_data['title'] = discretized_full
        discretized = discretise_data['addr_state'].dropna()
        discretized = pd.Series(discretized, index=discretise_data['addr_state'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['addr_state'].index)
        discretized_full.update(discretized)
        discretise_data['addr_state'] = discretized_full

        est = KBinsDiscretizer(n_bins = standard_num_bins, encode='ordinal', strategy='kmeans',subsample=200_000)
        dti_dataframe = np.array([discretise_data['dti'].dropna().to_numpy()]).transpose()
        est.fit(dti_dataframe)
        dti_dataframe = est.transform(dti_dataframe)
        discretized = pd.Series(dti_dataframe.reshape(-1), index=discretise_data['dti'].dropna().index)

        discretized_full = pd.Series('N/A', index= discretise_data['dti'].index)
        discretized_full.update(discretized)
        discretise_data['dti'] = discretized_full
        #
        est = KBinsDiscretizer(n_bins = standard_num_bins, encode='ordinal', strategy='kmeans',subsample=200_000)
        delinq_2yrs_dataframe = np.array([discretise_data['delinq_2yrs'].dropna().to_numpy()]).transpose()
        est.fit(delinq_2yrs_dataframe)
        delinq_2yrs_dataframe = est.transform(delinq_2yrs_dataframe)
        discretized = pd.Series(delinq_2yrs_dataframe.reshape(-1), index=discretise_data['delinq_2yrs'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['delinq_2yrs'].index)
        discretized_full.update(discretized)
        discretise_data['delinq_2yrs'] = discretized_full
        #
        #
        discretise_data['earliest_cr_line'] = pd.to_datetime(discretise_data['earliest_cr_line'].apply(lambda x: x.split('-')[1]))
        discretized = pd.cut(discretise_data['earliest_cr_line'].dropna(), bins = standard_num_bins)
        discretized = pd.Series(discretized, index=discretise_data['earliest_cr_line'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['earliest_cr_line'].index)
        discretized_full.update(discretized)
        discretise_data['earliest_cr_line'] = discretized_full
        #
        discretise_data['fico_range_high'] = pd.cut(discretise_data['fico_range_high'], bins= standard_num_bins)
        #
        est = KBinsDiscretizer(n_bins= standard_num_bins, encode='ordinal', strategy='kmeans',subsample=200_000)
        inq_last_6mths_dataframe = np.array([discretise_data['inq_last_6mths'].dropna().to_numpy()]).transpose()
        est.fit(inq_last_6mths_dataframe)
        inq_last_6mths_dataframe = est.transform(inq_last_6mths_dataframe)
        discretized = pd.Series(inq_last_6mths_dataframe.reshape(-1), index=discretise_data['inq_last_6mths'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['inq_last_6mths'].index)
        discretized_full.update(discretized)
        discretise_data['inq_last_6mths'] = discretized_full
        #
        est = KBinsDiscretizer(n_bins= standard_num_bins, encode='ordinal', strategy='kmeans',subsample=200_000)
        open_acc_dataframe = pd.DataFrame(discretise_data['open_acc'])
        est.fit(open_acc_dataframe)
        open_acc_dataframe = est.transform(open_acc_dataframe)
        discretise_data['open_acc'] = open_acc_dataframe

        est = KBinsDiscretizer(n_bins= standard_num_bins, encode='ordinal', strategy='kmeans',subsample=200_000)
        pub_rec_dataframe = pd.DataFrame(discretise_data['pub_rec'])
        est.fit(pub_rec_dataframe)
        pub_rec_dataframe = est.transform(pub_rec_dataframe)
        discretise_data['pub_rec'] = pub_rec_dataframe

        est = KBinsDiscretizer(n_bins= standard_num_bins, encode='ordinal', strategy='kmeans',subsample=200_000)
        revol_bal_dataframe = pd.DataFrame(discretise_data['revol_bal'])
        est.fit(revol_bal_dataframe)
        revol_bal_dataframe = est.transform(revol_bal_dataframe)
        discretise_data['revol_bal'] = revol_bal_dataframe
        #
        est = KBinsDiscretizer(n_bins= standard_num_bins, encode='ordinal', strategy='kmeans',subsample=200_000)
        revol_util_dataframe = np.array([discretise_data['revol_util'].dropna().to_numpy()]).transpose()
        est.fit(revol_util_dataframe)
        revol_util_dataframe = est.transform(revol_util_dataframe)
        discretized = pd.Series(revol_util_dataframe.reshape(-1), index=discretise_data['revol_util'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['revol_util'].index)
        discretized_full.update(discretized)
        discretise_data['revol_util'] = discretized_full
        #
        est = KBinsDiscretizer(n_bins= standard_num_bins, encode='ordinal', strategy='kmeans',subsample=200_000)
        total_acc_dataframe = pd.DataFrame(discretise_data['total_acc'])
        est.fit(total_acc_dataframe)
        total_acc_dataframe = est.transform(total_acc_dataframe)
        discretise_data['total_acc'] = total_acc_dataframe

        discretized = discretise_data['initial_list_status'].dropna()
        discretized = pd.Series(discretized, index=discretise_data['initial_list_status'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['initial_list_status'].index)
        discretized_full.update(discretized)
        discretise_data['initial_list_status'] = discretized_full

        est = KBinsDiscretizer(n_bins= standard_num_bins, encode='ordinal', strategy='kmeans',subsample=200_000)
        out_prncp_dataframe = pd.DataFrame(discretise_data['out_prncp'])
        est.fit(out_prncp_dataframe)
        out_prncp_dataframe = est.transform(out_prncp_dataframe)
        discretise_data['out_prncp'] = out_prncp_dataframe
        #
        est = KBinsDiscretizer(n_bins= standard_num_bins, encode='ordinal', strategy='kmeans',subsample=200_000)
        out_prncp_inv_dataframe = pd.DataFrame(discretise_data['out_prncp_inv'])
        est.fit(out_prncp_inv_dataframe)
        out_prncp_inv_dataframe = est.transform(out_prncp_inv_dataframe)
        discretise_data['out_prncp_inv'] = out_prncp_inv_dataframe
        #
        est = KBinsDiscretizer(n_bins= standard_num_bins, encode='ordinal', strategy='kmeans',subsample=200_000)
        total_pymnt_dataframe = pd.DataFrame(discretise_data['total_pymnt'])
        est.fit(total_pymnt_dataframe)
        total_pymnt_dataframe = est.transform(total_pymnt_dataframe)
        discretise_data['total_pymnt'] = total_pymnt_dataframe
        #
        est = KBinsDiscretizer(n_bins= standard_num_bins, encode='ordinal', strategy='kmeans',subsample=200_000)
        total_rec_int_dataframe = pd.DataFrame(discretise_data['total_rec_int'])
        est.fit(total_rec_int_dataframe)
        total_rec_int_dataframe = est.transform(total_rec_int_dataframe)
        discretise_data['total_rec_int'] = total_rec_int_dataframe
        #
        est = KBinsDiscretizer(n_bins= standard_num_bins, encode='ordinal', strategy='kmeans',subsample=200_000)
        total_rec_late_fee_dataframe = pd.DataFrame(discretise_data['total_rec_late_fee'])
        est.fit(total_rec_late_fee_dataframe)
        total_rec_late_fee_dataframe = est.transform(total_rec_late_fee_dataframe)
        discretise_data['total_rec_late_fee'] = total_rec_late_fee_dataframe
        #
        est = KBinsDiscretizer(n_bins= standard_num_bins, encode='ordinal', strategy='kmeans',subsample=200_000)
        recoveries_dataframe = pd.DataFrame(discretise_data['recoveries'])
        est.fit(recoveries_dataframe)
        recoveries_dataframe = est.transform(recoveries_dataframe)
        discretise_data['recoveries'] = recoveries_dataframe
        #
        est = KBinsDiscretizer(n_bins= standard_num_bins, encode='ordinal', strategy='kmeans',subsample=200_000)
        last_pymnt_amnt_dataframe = np.array([discretise_data['last_pymnt_amnt'].dropna().to_numpy()]).transpose()
        est.fit(last_pymnt_amnt_dataframe)
        last_pymnt_amnt_dataframe = est.transform(last_pymnt_amnt_dataframe)
        discretized = pd.Series(last_pymnt_amnt_dataframe.reshape(-1), index=discretise_data['last_pymnt_amnt'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['last_pymnt_amnt'].index)
        discretized_full.update(discretized)
        discretise_data['last_pymnt_amnt'] = discretized_full


        discretise_data['last_credit_pull_d'] = pd.to_datetime(discretise_data['last_credit_pull_d'], format='%b-%Y')
        discretise_data['last_credit_pull_d'] = discretise_data['last_credit_pull_d'].dt.year
        discretized = discretise_data['last_credit_pull_d'].dropna()
        discretized = pd.Series(discretized, index=discretise_data['last_credit_pull_d'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['last_credit_pull_d'].index)
        discretized_full.update(discretized)
        discretise_data['last_credit_pull_d'] = discretized_full
        #
        discretise_data['last_fico_range_high'] = pd.cut(discretise_data['last_fico_range_high'], bins= standard_num_bins)
        #
        discretise_data['collections_12_mths_ex_med'] = pd.cut(discretise_data['collections_12_mths_ex_med'], bins= standard_num_bins)
        #
        discretized = discretise_data['policy_code'].dropna()
        discretized = pd.Series(discretized, index=discretise_data['policy_code'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['policy_code'].index)
        discretized_full.update(discretized)
        discretise_data['policy_code'] = discretized_full

        discretized = discretise_data['application_type'].dropna()
        discretized = pd.Series(discretized, index=discretise_data['application_type'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['application_type'].index)
        discretized_full.update(discretized)
        discretise_data['application_type'] = discretized_full
        #
        discretise_data['acc_now_delinq'] = pd.cut(discretise_data['acc_now_delinq'], bins= standard_num_bins)
        #
        est = KBinsDiscretizer(n_bins= standard_num_bins, encode='ordinal', strategy='kmeans',subsample=200_000)
        tot_coll_amt_dataframe = pd.DataFrame(discretise_data['tot_coll_amt'])
        est.fit(tot_coll_amt_dataframe)
        tot_coll_amt_dataframe = est.transform(tot_coll_amt_dataframe)
        discretise_data['tot_coll_amt'] = tot_coll_amt_dataframe

        est = KBinsDiscretizer(n_bins= standard_num_bins, encode='ordinal', strategy='kmeans',subsample=200_000)
        tot_cur_bal_dataframe = pd.DataFrame(discretise_data['tot_cur_bal'])
        est.fit(tot_cur_bal_dataframe)
        tot_cur_bal_dataframe = est.transform(tot_cur_bal_dataframe)
        discretise_data['tot_cur_bal'] = tot_cur_bal_dataframe
        #
        est = KBinsDiscretizer(n_bins=  standard_num_bins, encode='ordinal', strategy='kmeans',subsample=200_000)
        open_acc_6m_dataframe = np.array([discretise_data['open_acc_6m'].dropna().to_numpy()]).transpose()
        est.fit(open_acc_6m_dataframe)
        open_acc_6m_dataframe = est.transform(open_acc_6m_dataframe)
        discretized = pd.Series(open_acc_6m_dataframe.reshape(-1), index=discretise_data['open_acc_6m'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['open_acc_6m'].index)
        discretized_full.update(discretized)
        discretise_data['open_acc_6m'] = discretized_full
        #


        est = KBinsDiscretizer(n_bins= standard_num_bins, encode='ordinal', strategy='kmeans',subsample=200_000)
        open_act_il_dataframe = np.array([discretise_data['open_act_il'].dropna().to_numpy()]).transpose()
        est.fit(open_act_il_dataframe)
        open_act_il_dataframe = est.transform(open_act_il_dataframe)
        discretized = pd.Series(open_act_il_dataframe.reshape(-1), index=discretise_data['open_act_il'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['open_act_il'].index)
        discretized_full.update(discretized)
        discretise_data['open_act_il'] = discretized_full

        est = KBinsDiscretizer(n_bins= standard_num_bins, encode='ordinal', strategy='kmeans',subsample=200_000)
        open_il_12m_dataframe = np.array([discretise_data['open_il_12m'].dropna().to_numpy()]).transpose()
        est.fit(open_il_12m_dataframe)
        open_il_12m_dataframe = est.transform(open_il_12m_dataframe)
        discretized = pd.Series(open_il_12m_dataframe.reshape(-1), index=discretise_data['open_il_12m'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['open_il_12m'].index)
        discretized_full.update(discretized)
        discretise_data['open_il_12m'] = discretized_full

        est = KBinsDiscretizer(n_bins= standard_num_bins, encode='ordinal', strategy='kmeans',subsample=200_000)
        open_il_24m_dataframe = np.array([discretise_data['open_il_24m'].dropna().to_numpy()]).transpose()
        est.fit(open_il_24m_dataframe)
        open_il_24m_dataframe = est.transform(open_il_24m_dataframe)
        discretized = pd.Series(open_il_24m_dataframe.reshape(-1), index=discretise_data['open_il_24m'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['open_il_24m'].index)
        discretized_full.update(discretized)
        discretise_data['open_il_24m'] = discretized_full
        #
        est = KBinsDiscretizer(n_bins= standard_num_bins, encode='ordinal', strategy='kmeans',subsample=200_000)
        total_bal_il_dataframe = np.array([discretise_data['total_bal_il'].dropna().to_numpy()]).transpose()
        est.fit(total_bal_il_dataframe)
        total_bal_il_dataframe = est.transform(total_bal_il_dataframe)
        discretized = pd.Series(total_bal_il_dataframe.reshape(-1), index=discretise_data['total_bal_il'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['total_bal_il'].index)
        discretized_full.update(discretized)
        discretise_data['total_bal_il'] = discretized_full
        #
        est = KBinsDiscretizer(n_bins= standard_num_bins, encode='ordinal', strategy='kmeans',subsample=200_000)
        open_rv_12m_dataframe = np.array([discretise_data['open_rv_12m'].dropna().to_numpy()]).transpose()
        est.fit(open_rv_12m_dataframe)
        open_rv_12m_dataframe = est.transform(open_rv_12m_dataframe)
        discretized = pd.Series(open_rv_12m_dataframe.reshape(-1), index=discretise_data['open_rv_12m'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['open_rv_12m'].index)
        discretized_full.update(discretized)
        discretise_data['open_rv_12m'] = discretized_full
        #
        est = KBinsDiscretizer(n_bins= standard_num_bins , encode='ordinal', strategy='kmeans',subsample=200_000)
        open_rv_24m_dataframe = np.array([discretise_data['open_rv_24m'].dropna().to_numpy()]).transpose()
        est.fit(open_rv_24m_dataframe)
        open_rv_24m_dataframe = est.transform(open_rv_24m_dataframe)
        discretized = pd.Series(open_rv_24m_dataframe.reshape(-1), index=discretise_data['open_rv_24m'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['open_rv_24m'].index)
        discretized_full.update(discretized)
        discretise_data['open_rv_24m'] = discretized_full
        #
        est = KBinsDiscretizer(n_bins= standard_num_bins , encode='ordinal', strategy='kmeans',subsample=200_000)
        max_bal_bc_dataframe = np.array([discretise_data['max_bal_bc'].dropna().to_numpy()]).transpose()
        est.fit(max_bal_bc_dataframe)
        max_bal_bc_dataframe = est.transform(max_bal_bc_dataframe)
        discretized = pd.Series(max_bal_bc_dataframe.reshape(-1), index=discretise_data['max_bal_bc'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['max_bal_bc'].index)
        discretized_full.update(discretized)
        discretise_data['max_bal_bc'] = discretized_full
        #
        est = KBinsDiscretizer(n_bins= standard_num_bins, encode='ordinal', strategy='kmeans',subsample=200_000)
        all_util_dataframe = np.array([discretise_data['all_util'].dropna().to_numpy()]).transpose()
        est.fit(all_util_dataframe)
        all_util_dataframe = est.transform(all_util_dataframe)
        discretized = pd.Series(all_util_dataframe.reshape(-1), index=discretise_data['all_util'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['all_util'].index)
        discretized_full.update(discretized)
        discretise_data['all_util'] = discretized_full

        est = KBinsDiscretizer(n_bins= standard_num_bins, encode='ordinal', strategy='kmeans',subsample=200_000)
        total_rev_hi_lim_dataframe = np.array([discretise_data['total_rev_hi_lim'].dropna().to_numpy()]).transpose()
        est.fit(total_rev_hi_lim_dataframe)
        total_rev_hi_lim_dataframe = est.transform(total_rev_hi_lim_dataframe)
        discretized = pd.Series(total_rev_hi_lim_dataframe.reshape(-1), index=discretise_data['total_rev_hi_lim'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['total_rev_hi_lim'].index)
        discretized_full.update(discretized)
        discretise_data['total_rev_hi_lim'] = discretized_full

        est = KBinsDiscretizer(n_bins= standard_num_bins, encode='ordinal', strategy='kmeans',subsample=200_000)
        inq_fi_dataframe = np.array([discretise_data['inq_fi'].dropna().to_numpy()]).transpose()
        est.fit(inq_fi_dataframe)
        inq_fi_dataframe = est.transform(inq_fi_dataframe)
        discretized = pd.Series(inq_fi_dataframe.reshape(-1), index=discretise_data['inq_fi'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['inq_fi'].index)
        discretized_full.update(discretized)
        discretise_data['inq_fi'] = discretized_full
        #
        est = KBinsDiscretizer(n_bins= standard_num_bins, encode='ordinal', strategy='kmeans',subsample=200_000)
        total_cu_tl_dataframe = np.array([discretise_data['total_cu_tl'].dropna().to_numpy()]).transpose()
        est.fit(total_cu_tl_dataframe)
        total_cu_tl_dataframe = est.transform(total_cu_tl_dataframe)
        discretized = pd.Series(total_cu_tl_dataframe.reshape(-1), index=discretise_data['total_cu_tl'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['total_cu_tl'].index)
        discretized_full.update(discretized)
        discretise_data['total_cu_tl'] = discretized_full

        est = KBinsDiscretizer(n_bins=  standard_num_bins, encode='ordinal', strategy='kmeans',subsample=200_000)
        inq_last_12m_dataframe = np.array([discretise_data['inq_last_12m'].dropna().to_numpy()]).transpose()
        est.fit(inq_last_12m_dataframe)
        inq_last_12m_dataframe = est.transform(inq_last_12m_dataframe)
        discretized = pd.Series(inq_last_12m_dataframe.reshape(-1), index=discretise_data['inq_last_12m'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['inq_last_12m'].index)
        discretized_full.update(discretized)
        discretise_data['inq_last_12m'] = discretized_full
        #
        est = KBinsDiscretizer(n_bins= standard_num_bins, encode='ordinal', strategy='kmeans',subsample=200_000)
        acc_open_past_24mths_dataframe = np.array([discretise_data['acc_open_past_24mths'].dropna().to_numpy()]).transpose()
        est.fit(acc_open_past_24mths_dataframe)
        acc_open_past_24mths_dataframe = est.transform(acc_open_past_24mths_dataframe)
        discretized = pd.Series(acc_open_past_24mths_dataframe.reshape(-1), index=discretise_data['acc_open_past_24mths'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['acc_open_past_24mths'].index)
        discretized_full.update(discretized)
        discretise_data['acc_open_past_24mths'] = discretized_full
        #
        est = KBinsDiscretizer(n_bins= standard_num_bins, encode='ordinal', strategy='kmeans',subsample=200_000)
        avg_cur_bal_dataframe = np.array([discretise_data['avg_cur_bal'].dropna().to_numpy()]).transpose()
        est.fit(avg_cur_bal_dataframe)
        avg_cur_bal_dataframe = est.transform(avg_cur_bal_dataframe)
        discretized = pd.Series(avg_cur_bal_dataframe.reshape(-1), index=discretise_data['avg_cur_bal'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['avg_cur_bal'].index)
        discretized_full.update(discretized)
        discretise_data['avg_cur_bal'] = discretized_full
        #
        est = KBinsDiscretizer(n_bins= standard_num_bins, encode='ordinal', strategy='kmeans',subsample=200_000)
        bc_open_to_buy_dataframe = np.array([discretise_data['bc_open_to_buy'].dropna().to_numpy()]).transpose()
        est.fit(bc_open_to_buy_dataframe)
        bc_open_to_buy_dataframe = est.transform(bc_open_to_buy_dataframe)
        discretized = pd.Series(bc_open_to_buy_dataframe.reshape(-1), index=discretise_data['bc_open_to_buy'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['bc_open_to_buy'].index)
        discretized_full.update(discretized)
        discretise_data['bc_open_to_buy'] = discretized_full
        #
        est = KBinsDiscretizer(n_bins= standard_num_bins, encode='ordinal', strategy='kmeans',subsample=200_000)
        bc_util_dataframe = np.array([discretise_data['bc_util'].dropna().to_numpy()]).transpose()
        est.fit(bc_util_dataframe)
        bc_util_dataframe = est.transform(bc_util_dataframe)
        discretized = pd.Series(bc_util_dataframe.reshape(-1), index=discretise_data['bc_util'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['bc_util'].index)
        discretized_full.update(discretized)
        discretise_data['bc_util'] = discretized_full
        # 
        discretized = pd.cut(discretise_data['chargeoff_within_12_mths'].dropna(), bins= standard_num_bins)
        discretized = pd.Series(discretized, index=discretise_data['chargeoff_within_12_mths'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['chargeoff_within_12_mths'].index)
        discretized_full.update(discretized)
        discretise_data['chargeoff_within_12_mths'] = discretized_full

        est = KBinsDiscretizer(n_bins= standard_num_bins, encode='ordinal', strategy='kmeans',subsample=200_000)
        delinq_amnt_dataframe = np.array([discretise_data['delinq_amnt'].dropna().to_numpy()]).transpose()
        est.fit(delinq_amnt_dataframe)
        delinq_amnt_dataframe = est.transform(delinq_amnt_dataframe)
        discretized = pd.Series(delinq_amnt_dataframe.reshape(-1), index=discretise_data['delinq_amnt'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['delinq_amnt'].index)
        discretized_full.update(discretized)
        discretise_data['delinq_amnt'] = discretized_full
        #
        est = KBinsDiscretizer(n_bins= standard_num_bins, encode='ordinal', strategy='kmeans',subsample=200_000)
        mo_sin_old_il_acct_dataframe = np.array([discretise_data['mo_sin_old_il_acct'].dropna().to_numpy()]).transpose()
        est.fit(mo_sin_old_il_acct_dataframe)
        mo_sin_old_il_acct_dataframe = est.transform(mo_sin_old_il_acct_dataframe)
        discretized = pd.Series(mo_sin_old_il_acct_dataframe.reshape(-1), index=discretise_data['mo_sin_old_il_acct'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['mo_sin_old_il_acct'].index)
        discretized_full.update(discretized)
        discretise_data['mo_sin_old_il_acct'] = discretized_full
        #
        est = KBinsDiscretizer(n_bins= standard_num_bins, encode='ordinal', strategy='kmeans',subsample=200_000)
        mo_sin_old_rev_tl_op_dataframe = np.array([discretise_data['mo_sin_old_rev_tl_op'].dropna().to_numpy()]).transpose()
        est.fit(mo_sin_old_rev_tl_op_dataframe)
        mo_sin_old_rev_tl_op_dataframe = est.transform(mo_sin_old_rev_tl_op_dataframe)
        discretized = pd.Series(mo_sin_old_rev_tl_op_dataframe.reshape(-1), index=discretise_data['mo_sin_old_rev_tl_op'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['mo_sin_old_rev_tl_op'].index)
        discretized_full.update(discretized)
        discretise_data['mo_sin_old_rev_tl_op'] = discretized_full
        #
        est = KBinsDiscretizer(n_bins= standard_num_bins, encode='ordinal', strategy='kmeans',subsample=200_000)
        mo_sin_rcnt_rev_tl_op_dataframe = np.array([discretise_data['mo_sin_rcnt_rev_tl_op'].dropna().to_numpy()]).transpose()
        est.fit(mo_sin_rcnt_rev_tl_op_dataframe)
        mo_sin_rcnt_rev_tl_op_dataframe = est.transform(mo_sin_rcnt_rev_tl_op_dataframe)
        discretized = pd.Series(mo_sin_rcnt_rev_tl_op_dataframe.reshape(-1), index=discretise_data['mo_sin_rcnt_rev_tl_op'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['mo_sin_rcnt_rev_tl_op'].index)
        discretized_full.update(discretized)
        discretise_data['mo_sin_rcnt_rev_tl_op'] = discretized_full
        #
        est = KBinsDiscretizer(n_bins= standard_num_bins, encode='ordinal', strategy='kmeans',subsample=200_000)
        mo_sin_rcnt_tl_dataframe = np.array([discretise_data['mo_sin_rcnt_tl'].dropna().to_numpy()]).transpose()
        est.fit(mo_sin_rcnt_tl_dataframe)
        mo_sin_rcnt_tl_dataframe = est.transform(mo_sin_rcnt_tl_dataframe)
        discretized = pd.Series(mo_sin_rcnt_tl_dataframe.reshape(-1), index=discretise_data['mo_sin_rcnt_tl'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['mo_sin_rcnt_tl'].index)
        discretized_full.update(discretized)
        discretise_data['mo_sin_rcnt_tl'] = discretized_full

        est = KBinsDiscretizer(n_bins= standard_num_bins, encode='ordinal', strategy='kmeans',subsample=200_000)
        mort_acc_dataframe = np.array([discretise_data['mort_acc'].dropna().to_numpy()]).transpose()
        est.fit(mort_acc_dataframe)
        mort_acc_dataframe = est.transform(mort_acc_dataframe)
        discretized = pd.Series(mort_acc_dataframe.reshape(-1), index=discretise_data['mort_acc'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['mort_acc'].index)
        discretized_full.update(discretized)
        discretise_data['mort_acc'] = discretized_full
        #
        est = KBinsDiscretizer(n_bins= standard_num_bins, encode='ordinal', strategy='kmeans',subsample=200_000)
        mths_since_recent_bc_dataframe = np.array([discretise_data['mths_since_recent_bc'].dropna().to_numpy()]).transpose()
        est.fit(mths_since_recent_bc_dataframe)
        mths_since_recent_bc_dataframe = est.transform(mths_since_recent_bc_dataframe)
        discretized = pd.Series(mths_since_recent_bc_dataframe.reshape(-1), index=discretise_data['mths_since_recent_bc'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['mths_since_recent_bc'].index)
        discretized_full.update(discretized)
        discretise_data['mths_since_recent_bc'] = discretized_full
        #
        est = KBinsDiscretizer(n_bins= standard_num_bins, encode='ordinal', strategy='kmeans',subsample=200_000)
        mths_since_recent_inq_dataframe = np.array([discretise_data['mths_since_recent_inq'].dropna().to_numpy()]).transpose()
        est.fit(mths_since_recent_inq_dataframe)
        mths_since_recent_inq_dataframe = est.transform(mths_since_recent_inq_dataframe)
        discretized = pd.Series(mths_since_recent_inq_dataframe.reshape(-1), index=discretise_data['mths_since_recent_inq'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['mths_since_recent_inq'].index)
        discretized_full.update(discretized)
        discretise_data['mths_since_recent_inq'] = discretized_full

        est = KBinsDiscretizer(n_bins= standard_num_bins, encode='ordinal', strategy='kmeans',subsample=200_000)
        num_accts_ever_120_pd_dataframe = np.array([discretise_data['num_accts_ever_120_pd'].dropna().to_numpy()]).transpose()
        est.fit(num_accts_ever_120_pd_dataframe)
        num_accts_ever_120_pd_dataframe = est.transform(num_accts_ever_120_pd_dataframe)
        discretized = pd.Series(num_accts_ever_120_pd_dataframe.reshape(-1), index=discretise_data['num_accts_ever_120_pd'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['num_accts_ever_120_pd'].index)
        discretized_full.update(discretized)
        discretise_data['num_accts_ever_120_pd'] = discretized_full

        est = KBinsDiscretizer(n_bins= standard_num_bins, encode='ordinal', strategy='kmeans',subsample=200_000)
        num_actv_bc_tl_dataframe = np.array([discretise_data['num_actv_bc_tl'].dropna().to_numpy()]).transpose()
        est.fit(num_actv_bc_tl_dataframe)
        num_actv_bc_tl_dataframe = est.transform(num_actv_bc_tl_dataframe)
        discretized = pd.Series(num_actv_bc_tl_dataframe.reshape(-1), index=discretise_data['num_actv_bc_tl'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['num_actv_bc_tl'].index)
        discretized_full.update(discretized)
        discretise_data['num_actv_bc_tl'] = discretized_full

        est = KBinsDiscretizer(n_bins= standard_num_bins, encode='ordinal', strategy='kmeans',subsample=200_000)
        num_actv_rev_tl_dataframe = np.array([discretise_data['num_actv_rev_tl'].dropna().to_numpy()]).transpose()
        est.fit(num_actv_rev_tl_dataframe)
        num_actv_rev_tl_dataframe = est.transform(num_actv_rev_tl_dataframe)
        discretized = pd.Series(num_actv_rev_tl_dataframe.reshape(-1), index=discretise_data['num_actv_rev_tl'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['num_actv_rev_tl'].index)
        discretized_full.update(discretized)
        discretise_data['num_actv_rev_tl'] = discretized_full
        #
        est = KBinsDiscretizer(n_bins= standard_num_bins, encode='ordinal', strategy='kmeans',subsample=200_000)
        num_bc_sats_dataframe = np.array([discretise_data['num_bc_sats'].dropna().to_numpy()]).transpose()
        est.fit(num_bc_sats_dataframe)
        num_bc_sats_dataframe = est.transform(num_bc_sats_dataframe)
        discretized = pd.Series(num_bc_sats_dataframe.reshape(-1), index=discretise_data['num_bc_sats'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['num_bc_sats'].index)
        discretized_full.update(discretized)
        discretise_data['num_bc_sats'] = discretized_full
        #
        est = KBinsDiscretizer(n_bins= standard_num_bins, encode='ordinal', strategy='kmeans',subsample=200_000)
        num_bc_tl_dataframe = np.array([discretise_data['num_bc_tl'].dropna().to_numpy()]).transpose()
        est.fit(num_bc_tl_dataframe)
        num_bc_tl_dataframe = est.transform(num_bc_tl_dataframe)
        discretized = pd.Series(num_bc_tl_dataframe.reshape(-1), index=discretise_data['num_bc_tl'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['num_bc_tl'].index)
        discretized_full.update(discretized)
        discretise_data['num_bc_tl'] = discretized_full
        #
        est = KBinsDiscretizer(n_bins= standard_num_bins, encode='ordinal', strategy='kmeans',subsample=200_000)
        num_il_tl_dataframe =  np.array([discretise_data['num_il_tl'].dropna().to_numpy()]).transpose()
        est.fit(num_il_tl_dataframe)
        num_il_tl_dataframe = est.transform(num_il_tl_dataframe)
        discretized = pd.Series(num_il_tl_dataframe.reshape(-1), index=discretise_data['num_il_tl'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['num_il_tl'].index)
        discretized_full.update(discretized)
        discretise_data['num_il_tl'] = discretized_full

        est = KBinsDiscretizer(n_bins= standard_num_bins, encode='ordinal', strategy='kmeans',subsample=200_000)
        num_op_rev_tl_dataframe = np.array([discretise_data['num_op_rev_tl'].dropna().to_numpy()]).transpose()
        est.fit(num_op_rev_tl_dataframe)
        num_op_rev_tl_dataframe = est.transform(num_op_rev_tl_dataframe)
        discretized = pd.Series(num_op_rev_tl_dataframe.reshape(-1), index=discretise_data['num_op_rev_tl'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['num_op_rev_tl'].index)
        discretized_full.update(discretized)
        discretise_data['num_op_rev_tl'] = discretized_full
        #
        est = KBinsDiscretizer(n_bins= standard_num_bins, encode='ordinal', strategy='kmeans',subsample=200_000)
        num_rev_accts_dataframe = np.array([discretise_data['num_rev_accts'].dropna().to_numpy()]).transpose()
        est.fit(num_rev_accts_dataframe)
        num_rev_accts_dataframe = est.transform(num_rev_accts_dataframe)
        discretized = pd.Series(num_rev_accts_dataframe.reshape(-1), index=discretise_data['num_rev_accts'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['num_rev_accts'].index)
        discretized_full.update(discretized)
        discretise_data['num_rev_accts'] = discretized_full
        #
        est = KBinsDiscretizer(n_bins=  standard_num_bins , encode='ordinal', strategy='kmeans',subsample=200_000)
        num_tl_120dpd_2m_dataframe = np.array([discretise_data['num_tl_120dpd_2m'].dropna().to_numpy()]).transpose()
        est.fit(num_tl_120dpd_2m_dataframe)
        num_tl_120dpd_2m_dataframe = est.transform(num_tl_120dpd_2m_dataframe)
        discretized = pd.Series(num_tl_120dpd_2m_dataframe.reshape(-1), index=discretise_data['num_tl_120dpd_2m'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['num_tl_120dpd_2m'].index)
        discretized_full.update(discretized)
        discretise_data['num_tl_120dpd_2m'] = discretized_full

        est = KBinsDiscretizer(n_bins=  standard_num_bins, encode='ordinal', strategy='kmeans',subsample=200_000)
        num_tl_30dpd_dataframe = np.array([discretise_data['num_tl_30dpd'].dropna().to_numpy()]).transpose()
        est.fit(num_tl_30dpd_dataframe)
        num_tl_30dpd_dataframe = est.transform(num_tl_30dpd_dataframe)
        discretized = pd.Series(num_tl_30dpd_dataframe.reshape(-1), index=discretise_data['num_tl_30dpd'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['num_tl_30dpd'].index)
        discretized_full.update(discretized)
        discretise_data['num_tl_30dpd'] = discretized_full

        est = KBinsDiscretizer(n_bins=  standard_num_bins, encode='ordinal', strategy='kmeans',subsample=200_000)
        num_tl_90g_dpd_24m_dataframe = np.array([discretise_data['num_tl_90g_dpd_24m'].dropna().to_numpy()]).transpose()
        est.fit(num_tl_90g_dpd_24m_dataframe)
        num_tl_90g_dpd_24m_dataframe = est.transform(num_tl_90g_dpd_24m_dataframe)
        discretized = pd.Series(num_tl_90g_dpd_24m_dataframe.reshape(-1), index=discretise_data['num_tl_90g_dpd_24m'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['num_tl_90g_dpd_24m'].index)
        discretized_full.update(discretized)
        discretise_data['num_tl_90g_dpd_24m'] = discretized_full

        est = KBinsDiscretizer(n_bins=  standard_num_bins, encode='ordinal', strategy='kmeans',subsample=200_000)
        num_tl_op_past_12m_dataframe = np.array([discretise_data['num_tl_op_past_12m'].dropna().to_numpy()]).transpose()
        est.fit(num_tl_op_past_12m_dataframe)
        num_tl_op_past_12m_dataframe = est.transform(num_tl_op_past_12m_dataframe)
        discretized = pd.Series(num_tl_op_past_12m_dataframe.reshape(-1), index=discretise_data['num_tl_op_past_12m'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['num_tl_op_past_12m'].index)
        discretized_full.update(discretized)
        discretise_data['num_tl_op_past_12m'] = discretized_full
        #
        est = KBinsDiscretizer(n_bins= standard_num_bins, encode='ordinal', strategy='kmeans',subsample=200_000)
        pct_tl_nvr_dlq_dataframe = np.array([discretise_data['pct_tl_nvr_dlq'].dropna().to_numpy()]).transpose()
        est.fit(pct_tl_nvr_dlq_dataframe)
        pct_tl_nvr_dlq_dataframe = est.transform(pct_tl_nvr_dlq_dataframe)
        discretized = pd.Series(pct_tl_nvr_dlq_dataframe.reshape(-1), index=discretise_data['pct_tl_nvr_dlq'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['pct_tl_nvr_dlq'].index)
        discretized_full.update(discretized)
        discretise_data['pct_tl_nvr_dlq'] = discretized_full
        #
        est = KBinsDiscretizer(n_bins= standard_num_bins, encode='ordinal', strategy='kmeans',subsample=200_000)
        percent_bc_gt_75_dataframe = np.array([discretise_data['percent_bc_gt_75'].dropna().to_numpy()]).transpose()
        est.fit(percent_bc_gt_75_dataframe)
        percent_bc_gt_75_dataframe = est.transform(percent_bc_gt_75_dataframe)
        discretized = pd.Series(percent_bc_gt_75_dataframe.reshape(-1), index=discretise_data['percent_bc_gt_75'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['percent_bc_gt_75'].index)
        discretized_full.update(discretized)
        discretise_data['percent_bc_gt_75'] = discretized_full

        est = KBinsDiscretizer(n_bins= standard_num_bins, encode='ordinal', strategy='kmeans',subsample=200_000)
        pub_rec_bankruptcies_dataframe = np.array([discretise_data['pub_rec_bankruptcies'].dropna().to_numpy()]).transpose()
        est.fit(pub_rec_bankruptcies_dataframe)
        pub_rec_bankruptcies_dataframe = est.transform(pub_rec_bankruptcies_dataframe)
        discretized = pd.Series(pub_rec_bankruptcies_dataframe.reshape(-1), index=discretise_data['pub_rec_bankruptcies'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['pub_rec_bankruptcies'].index)
        discretized_full.update(discretized)
        discretise_data['pub_rec_bankruptcies'] = discretized_full

        est = KBinsDiscretizer(n_bins= standard_num_bins, encode='ordinal', strategy='kmeans',subsample=200_000)
        tax_liens_dataframe =  np.array([discretise_data['tax_liens'].dropna().to_numpy()]).transpose()
        est.fit(tax_liens_dataframe)
        tax_liens_dataframe = est.transform(tax_liens_dataframe)
        discretized = pd.Series(tax_liens_dataframe.reshape(-1), index=discretise_data['tax_liens'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['tax_liens'].index)
        discretized_full.update(discretized)
        discretise_data['tax_liens'] = discretized_full

        est = KBinsDiscretizer(n_bins= standard_num_bins, encode='ordinal', strategy='kmeans',subsample=200_000)
        total_bal_ex_mort_dataframe = np.array([discretise_data['total_bal_ex_mort'].dropna().to_numpy()]).transpose()
        est.fit(total_bal_ex_mort_dataframe)
        total_bal_ex_mort_dataframe = est.transform(total_bal_ex_mort_dataframe)
        discretized = pd.Series(total_bal_ex_mort_dataframe.reshape(-1), index=discretise_data['total_bal_ex_mort'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['total_bal_ex_mort'].index)
        discretized_full.update(discretized)
        discretise_data['total_bal_ex_mort'] = discretized_full
        #
        est = KBinsDiscretizer(n_bins= standard_num_bins, encode='ordinal', strategy='kmeans',subsample=200_000)
        total_bc_limit_dataframe = np.array([discretise_data['total_bc_limit'].dropna().to_numpy()]).transpose()
        est.fit(total_bc_limit_dataframe)
        total_bc_limit_dataframe = est.transform(total_bc_limit_dataframe)
        discretized = pd.Series(total_bc_limit_dataframe.reshape(-1), index=discretise_data['total_bc_limit'].dropna().index)
        discretized_full = pd.Series('N/A', index= discretise_data['total_bc_limit'].index)
        discretized_full.update(discretized)
        discretise_data['total_bc_limit'] = discretized_full
        #
        discretise_data['hardship_flag'].astype('category')
        discretise_data['disbursement_method'].astype('category')
        discretise_data['debt_settlement_flag'].astype('category')

        category_data = discretise_data.astype('category')
        str_data = discretise_data.astype('str')

        return str_data



    def preprocess_data(data: pd.DataFrame):
        
        discretised_data = DataPreprocessing.discretise_data(data)
        return discretised_data
    
    
    def get_feature_states(discretised_data: pd.DataFrame):
        feature_states_dict = {}
        
        for column in discretised_data.columns:
            feature_states_dict.update({column:discretised_data[column].unique().tolist()})
            
        return feature_states_dict
    
    
    
    def split_data(data: pd.DataFrame, num_rows: int):
        
        #subest_data = data.sample(n=num_rows)
        subset_data = data.sample(n = num_rows)
        
        # splits data into 75% train and 25% test
        train_val, test =  train_test_split(subset_data, test_size = 0.2)
        
        train, validation =  train_test_split(train_val, test_size = 0.25)
        
        return train, validation, test
    
    def get_evidence_list(test_data, target_label_list: list, evidence_features: list):
        # gets the evidence list of the testing data to use as evidence when classifying loan status
        
        targets_removed_df = test_data.copy()
        
        for target_label in target_label_list:
            del targets_removed_df[target_label]
            
        testing_evidence_list = []
        for i in range(len(targets_removed_df)):
            testing_evidence_dict = {}
            for z in range(len(evidence_features)):
                testing_evidence_dict[evidence_features[z]] = targets_removed_df[evidence_features[z]].iloc[i]
                testing_evidence_dict['loan_status'] = "Fully Paid"
            testing_evidence_list.append(testing_evidence_dict)
        
        return testing_evidence_list