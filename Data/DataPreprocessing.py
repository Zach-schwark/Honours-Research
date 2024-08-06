# imports
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, KBinsDiscretizer
import math


class DataPreprocessing:
    
    def load_data(num_rows: int)-> pd.DataFrame:
        # reads from CS, removes rows with null/missing values and automatically infers and converts datatypes for the data.
        
        data = pd.read_csv("Data/accepted_2007_to_2018Q4.csv", engine='c', nrows = num_rows)
        data = data.drop(['id', 'member_id', 'settlement_term','settlement_percentage', 'settlement_amount', 'settlement_date','settlement_status', 'debt_settlement_flag_date', 'hardship_last_payment_amount', 'hardship_payoff_balance_amount', 'orig_projected_additional_accrued_interest',
           'hardship_loan_status', 'hardship_dpd', 'hardship_length','payment_plan_start_date','hardship_end_date', 'hardship_start_date', 'hardship_amount', 'deferral_term', 'hardship_status', 'hardship_reason', 'hardship_type',
           'sec_app_mths_since_last_major_derog', 'sec_app_collections_12_mths_ex_med', 'sec_app_chargeoff_within_12_mths', 'sec_app_num_rev_accts', 'sec_app_open_act_il', 'sec_app_revol_util', 'sec_app_open_acc', 'sec_app_mort_acc',
           'sec_app_inq_last_6mths', 'sec_app_earliest_cr_line', 'sec_app_fico_range_high', 'sec_app_fico_range_low', 'verification_status_joint', 'dti_joint', 'annual_inc_joint', 'desc', 'url', 'revol_bal_joint','mths_since_last_record', 'mths_since_recent_bc_dlq', 'mths_since_last_major_derog', 'mths_since_recent_revol_delinq', 'next_pymnt_d',
           'il_util', 'mths_since_rcnt_il','mths_since_last_delinq', 'zip_code' ], axis=1)
        data = data.dropna()
        data.convert_dtypes()
        return data
        
        
    #def normalize_data(data: pd.DataFrame):
    #    normalized_data = data.copy()
    #    for column  in normalized_data.columns:
    #        if normalized_data[column].dtype == np.float64:
    #            normalized_data[column] = MinMaxScaler().fit_transform(np.array(normalized_data[column]).reshape(-1,1)) 
    #    return normalized_data
    
    def discretise_data(data: pd.DataFrame):
        discretise_data = data.copy()

        discretise_data['loan_amnt'] = pd.cut(discretise_data['loan_amnt'], bins= 50)
        discretise_data['funded_amnt'] = pd.cut(discretise_data['funded_amnt'], bins= 50)
        discretise_data['funded_amnt_inv'] = pd.cut(discretise_data['funded_amnt_inv'], bins= 50)
        discretise_data['int_rate'] = pd.cut(discretise_data['int_rate'], bins= 50)
        discretise_data['installment'] = pd.cut(discretise_data['installment'], bins = 50)

        est = KBinsDiscretizer(n_bins= 50, encode='ordinal', strategy='kmeans')
        annual_inc_dataframe = pd.DataFrame(discretise_data['annual_inc'])
        est.fit(annual_inc_dataframe)
        annual_inc_dataframe = est.transform(annual_inc_dataframe)
        discretise_data['annual_inc'] = annual_inc_dataframe

        discretise_data['loan_status'] = discretise_data['loan_status'].apply(lambda x: 'Fully Paid' if 'Fully Paid' in x else x)
        #discretise_data['loan_status'] = discretise_data['loan_status'].apply(lambda x: 'Late' if 'Late' in x else x)

        # 'Current'
        values_to_keep = ['Fully Paid','Current', 'Charged Off']
        pattern = '|'.join(values_to_keep)

        discretise_data = discretise_data[discretise_data['loan_status'].str.contains(pattern)]


        est = KBinsDiscretizer(n_bins= 50, encode='ordinal', strategy='kmeans')
        dti_dataframe = pd.DataFrame(discretise_data['dti'])
        est.fit(dti_dataframe)
        dti_dataframe = est.transform(dti_dataframe)
        discretise_data['dti'] = dti_dataframe


        est = KBinsDiscretizer(n_bins= 31, encode='ordinal', strategy='kmeans')
        delinq_2yrs_dataframe = pd.DataFrame(discretise_data['delinq_2yrs'])
        est.fit(delinq_2yrs_dataframe)
        delinq_2yrs_dataframe = est.transform(delinq_2yrs_dataframe)
        discretise_data['delinq_2yrs'] = delinq_2yrs_dataframe
        #discretise_data['delinq_2yrs'] = pd.cut(discretise_data['delinq_2yrs'], bins= 3)


        discretise_data['earliest_cr_line'] = discretise_data['earliest_cr_line'].apply(lambda x: x.split('-')[1])

        discretise_data['fico_range_low'] = pd.cut(discretise_data['fico_range_low'], bins= 20)
        discretise_data['fico_range_high'] = pd.cut(discretise_data['fico_range_high'], bins= 20)

        est = KBinsDiscretizer(n_bins= 6, encode='ordinal', strategy='kmeans')
        inq_last_6mths_dataframe = pd.DataFrame(discretise_data['inq_last_6mths'])
        est.fit(inq_last_6mths_dataframe)
        inq_last_6mths_dataframe = est.transform(inq_last_6mths_dataframe)
        discretise_data['inq_last_6mths'] = inq_last_6mths_dataframe


        est = KBinsDiscretizer(n_bins= 50, encode='ordinal', strategy='kmeans')
        open_acc_dataframe = pd.DataFrame(discretise_data['open_acc'])
        est.fit(open_acc_dataframe)
        open_acc_dataframe = est.transform(open_acc_dataframe)
        discretise_data['open_acc'] = open_acc_dataframe

        est = KBinsDiscretizer(n_bins= 34, encode='ordinal', strategy='kmeans')
        pub_rec_dataframe = pd.DataFrame(discretise_data['pub_rec'])
        est.fit(pub_rec_dataframe)
        pub_rec_dataframe = est.transform(pub_rec_dataframe)
        discretise_data['pub_rec'] = pub_rec_dataframe

        est = KBinsDiscretizer(n_bins= 50, encode='ordinal', strategy='kmeans')
        revol_bal_dataframe = pd.DataFrame(discretise_data['revol_bal'])
        est.fit(revol_bal_dataframe)
        revol_bal_dataframe = est.transform(revol_bal_dataframe)
        discretise_data['revol_bal'] = revol_bal_dataframe

        est = KBinsDiscretizer(n_bins= 50, encode='ordinal', strategy='kmeans')
        revol_util_dataframe = pd.DataFrame(discretise_data['revol_util'])
        est.fit(revol_util_dataframe)
        revol_util_dataframe = est.transform(revol_util_dataframe)
        discretise_data['revol_util'] = revol_util_dataframe

        est = KBinsDiscretizer(n_bins= 50, encode='ordinal', strategy='kmeans')
        total_acc_dataframe = pd.DataFrame(discretise_data['total_acc'])
        est.fit(total_acc_dataframe)
        total_acc_dataframe = est.transform(total_acc_dataframe)
        discretise_data['total_acc'] = total_acc_dataframe



        est = KBinsDiscretizer(n_bins= 50, encode='ordinal', strategy='kmeans')
        out_prncp_dataframe = pd.DataFrame(discretise_data['out_prncp'])
        est.fit(out_prncp_dataframe)
        out_prncp_dataframe = est.transform(out_prncp_dataframe)
        discretise_data['out_prncp'] = out_prncp_dataframe

        est = KBinsDiscretizer(n_bins= 50, encode='ordinal', strategy='kmeans')
        out_prncp_inv_dataframe = pd.DataFrame(discretise_data['out_prncp_inv'])
        est.fit(out_prncp_inv_dataframe)
        out_prncp_inv_dataframe = est.transform(out_prncp_inv_dataframe)
        discretise_data['out_prncp_inv'] = out_prncp_inv_dataframe


        #discretise_data['total_pymnt'] = pd.cut(discretise_data['total_pymnt'], bins= 50)
        est = KBinsDiscretizer(n_bins= 50, encode='ordinal', strategy='kmeans')
        total_pymnt_dataframe = pd.DataFrame(discretise_data['total_pymnt'])
        est.fit(total_pymnt_dataframe)
        total_pymnt_dataframe = est.transform(total_pymnt_dataframe)
        discretise_data['total_pymnt'] = total_pymnt_dataframe

        #discretise_data['total_pymnt_inv'] = pd.cut(discretise_data['total_pymnt_inv'], bins= 50)
        est = KBinsDiscretizer(n_bins= 50, encode='ordinal', strategy='kmeans')
        total_pymnt_inv_dataframe = pd.DataFrame(discretise_data['total_pymnt_inv'])
        est.fit(total_pymnt_inv_dataframe)
        total_pymnt_inv_dataframe = est.transform(total_pymnt_inv_dataframe)
        discretise_data['total_pymnt_inv'] = total_pymnt_inv_dataframe

        #discretise_data['total_rec_prncp'] = pd.cut(discretise_data['total_rec_prncp'], bins= 50)
        est = KBinsDiscretizer(n_bins= 50, encode='ordinal', strategy='kmeans')
        total_rec_prncp_dataframe = pd.DataFrame(discretise_data['total_rec_prncp'])
        est.fit(total_rec_prncp_dataframe)
        total_rec_prncp_dataframe = est.transform(total_rec_prncp_dataframe)
        discretise_data['total_rec_prncp'] = total_rec_prncp_dataframe

        est = KBinsDiscretizer(n_bins= 50, encode='ordinal', strategy='kmeans')
        total_rec_int_dataframe = pd.DataFrame(discretise_data['total_rec_int'])
        est.fit(total_rec_int_dataframe)
        total_rec_int_dataframe = est.transform(total_rec_int_dataframe)
        discretise_data['total_rec_int'] = total_rec_int_dataframe

        est = KBinsDiscretizer(n_bins= 50, encode='ordinal', strategy='kmeans')
        total_rec_late_fee_dataframe = pd.DataFrame(discretise_data['total_rec_late_fee'])
        est.fit(total_rec_late_fee_dataframe)
        total_rec_late_fee_dataframe = est.transform(total_rec_late_fee_dataframe)
        discretise_data['total_rec_late_fee'] = total_rec_late_fee_dataframe

        est = KBinsDiscretizer(n_bins= 50, encode='ordinal', strategy='kmeans')
        recoveries_dataframe = pd.DataFrame(discretise_data['recoveries'])
        est.fit(recoveries_dataframe)
        recoveries_dataframe = est.transform(recoveries_dataframe)
        discretise_data['recoveries'] = recoveries_dataframe

        est = KBinsDiscretizer(n_bins= 50, encode='ordinal', strategy='kmeans')
        collection_recovery_fee_dataframe = pd.DataFrame(discretise_data['collection_recovery_fee'])
        est.fit(collection_recovery_fee_dataframe)
        collection_recovery_fee_dataframe = est.transform(collection_recovery_fee_dataframe)
        discretise_data['collection_recovery_fee'] = collection_recovery_fee_dataframe

        est = KBinsDiscretizer(n_bins= 50, encode='ordinal', strategy='kmeans')
        last_pymnt_amnt_dataframe = pd.DataFrame(discretise_data['last_pymnt_amnt'])
        est.fit(last_pymnt_amnt_dataframe)
        last_pymnt_amnt_dataframe = est.transform(last_pymnt_amnt_dataframe)
        discretise_data['last_pymnt_amnt'] = last_pymnt_amnt_dataframe

        discretise_data['last_fico_range_high'] = pd.cut(discretise_data['last_fico_range_high'], bins= 50)
        discretise_data['last_fico_range_low'] = pd.cut(discretise_data['last_fico_range_low'], bins= 50)

        discretise_data['collections_12_mths_ex_med'] = pd.cut(discretise_data['collections_12_mths_ex_med'], bins= 10)

        discretise_data['policy_code'] = pd.cut(discretise_data['policy_code'], bins= 2, labels= [1,0])

        discretise_data['acc_now_delinq'] = pd.cut(discretise_data['acc_now_delinq'], bins= 7)

        est = KBinsDiscretizer(n_bins= 50, encode='ordinal', strategy='kmeans')
        tot_coll_amt_dataframe = pd.DataFrame(discretise_data['tot_coll_amt'])
        est.fit(tot_coll_amt_dataframe)
        tot_coll_amt_dataframe = est.transform(tot_coll_amt_dataframe)
        discretise_data['tot_coll_amt'] = tot_coll_amt_dataframe

        est = KBinsDiscretizer(n_bins= 50, encode='ordinal', strategy='kmeans')
        tot_cur_bal_dataframe = pd.DataFrame(discretise_data['tot_cur_bal'])
        est.fit(tot_cur_bal_dataframe)
        tot_cur_bal_dataframe = est.transform(tot_cur_bal_dataframe)
        discretise_data['tot_cur_bal'] = tot_cur_bal_dataframe

        est = KBinsDiscretizer(n_bins= 17, encode='ordinal', strategy='kmeans')
        open_acc_6m_dataframe = pd.DataFrame(discretise_data['open_acc_6m'])
        est.fit(open_acc_6m_dataframe)
        open_acc_6m_dataframe = est.transform(open_acc_6m_dataframe)
        discretise_data['open_acc_6m'] = open_acc_6m_dataframe

        est = KBinsDiscretizer(n_bins= 50, encode='ordinal', strategy='kmeans')
        open_act_il_dataframe = pd.DataFrame(discretise_data['open_act_il'])
        est.fit(open_act_il_dataframe)
        open_act_il_dataframe = est.transform(open_act_il_dataframe)
        discretise_data['open_act_il'] = open_act_il_dataframe

        est = KBinsDiscretizer(n_bins= 15, encode='ordinal', strategy='kmeans')
        open_il_12m_dataframe = pd.DataFrame(discretise_data['open_il_12m'])
        est.fit(open_il_12m_dataframe)
        open_il_12m_dataframe = est.transform(open_il_12m_dataframe)
        discretise_data['open_il_12m'] = open_il_12m_dataframe

        est = KBinsDiscretizer(n_bins= 27, encode='ordinal', strategy='kmeans')
        open_il_24m_dataframe = pd.DataFrame(discretise_data['open_il_24m'])
        est.fit(open_il_24m_dataframe)
        open_il_24m_dataframe = est.transform(open_il_24m_dataframe)
        discretise_data['open_il_24m'] = open_il_24m_dataframe

        est = KBinsDiscretizer(n_bins= 50, encode='ordinal', strategy='kmeans')
        total_bal_il_dataframe = pd.DataFrame(discretise_data['total_bal_il'])
        est.fit(total_bal_il_dataframe)
        total_bal_il_dataframe = est.transform(total_bal_il_dataframe)
        discretise_data['total_bal_il'] = total_bal_il_dataframe

        est = KBinsDiscretizer(n_bins= 28, encode='ordinal', strategy='kmeans')
        open_rv_12m_dataframe = pd.DataFrame(discretise_data['open_rv_12m'])
        est.fit(open_rv_12m_dataframe)
        open_rv_12m_dataframe = est.transform(open_rv_12m_dataframe)
        discretise_data['open_rv_12m'] = open_rv_12m_dataframe


        est = KBinsDiscretizer(n_bins= 50 , encode='ordinal', strategy='kmeans')
        open_rv_24m_dataframe = pd.DataFrame(discretise_data['open_rv_24m'])
        est.fit(open_rv_24m_dataframe)
        open_rv_24m_dataframe = est.transform(open_rv_24m_dataframe)
        discretise_data['open_rv_24m'] = open_rv_24m_dataframe


        est = KBinsDiscretizer(n_bins= 50 , encode='ordinal', strategy='kmeans')
        max_bal_bc_dataframe = pd.DataFrame(discretise_data['max_bal_bc'])
        est.fit(max_bal_bc_dataframe)
        max_bal_bc_dataframe = est.transform(max_bal_bc_dataframe)
        discretise_data['max_bal_bc'] = max_bal_bc_dataframe


        est = KBinsDiscretizer(n_bins= 50, encode='ordinal', strategy='kmeans')
        all_util_dataframe = pd.DataFrame(discretise_data['all_util'])
        est.fit(all_util_dataframe)
        all_util_dataframe = est.transform(all_util_dataframe)
        discretise_data['all_util'] = all_util_dataframe

        est = KBinsDiscretizer(n_bins= 50, encode='ordinal', strategy='kmeans')
        total_rev_hi_lim_dataframe = pd.DataFrame(discretise_data['total_rev_hi_lim'])
        est.fit(total_rev_hi_lim_dataframe)
        total_rev_hi_lim_dataframe = est.transform(total_rev_hi_lim_dataframe)
        discretise_data['total_rev_hi_lim'] = total_rev_hi_lim_dataframe

        est = KBinsDiscretizer(n_bins= 33, encode='ordinal', strategy='kmeans')
        inq_fi_dataframe = pd.DataFrame(discretise_data['inq_fi'])
        est.fit(inq_fi_dataframe)
        inq_fi_dataframe = est.transform(inq_fi_dataframe)
        discretise_data['inq_fi'] = inq_fi_dataframe

        est = KBinsDiscretizer(n_bins= 50, encode='ordinal', strategy='kmeans')
        total_cu_tl_dataframe = pd.DataFrame(discretise_data['total_cu_tl'])
        est.fit(total_cu_tl_dataframe)
        total_cu_tl_dataframe = est.transform(total_cu_tl_dataframe)
        discretise_data['total_cu_tl'] = total_cu_tl_dataframe

        est = KBinsDiscretizer(n_bins= 48, encode='ordinal', strategy='kmeans')
        inq_last_12m_dataframe = pd.DataFrame(discretise_data['inq_last_12m'])
        est.fit(inq_last_12m_dataframe)
        inq_last_12m_dataframe = est.transform(inq_last_12m_dataframe)
        discretise_data['inq_last_12m'] = inq_last_12m_dataframe

        est = KBinsDiscretizer(n_bins= 50, encode='ordinal', strategy='kmeans')
        acc_open_past_24mths_dataframe = pd.DataFrame(discretise_data['acc_open_past_24mths'])
        est.fit(acc_open_past_24mths_dataframe)
        acc_open_past_24mths_dataframe = est.transform(acc_open_past_24mths_dataframe)
        discretise_data['acc_open_past_24mths'] = acc_open_past_24mths_dataframe

        est = KBinsDiscretizer(n_bins= 50, encode='ordinal', strategy='kmeans')
        avg_cur_bal_dataframe = pd.DataFrame(discretise_data['avg_cur_bal'])
        est.fit(avg_cur_bal_dataframe)
        avg_cur_bal_dataframe = est.transform(avg_cur_bal_dataframe)
        discretise_data['avg_cur_bal'] = avg_cur_bal_dataframe

        est = KBinsDiscretizer(n_bins= 50, encode='ordinal', strategy='kmeans')
        bc_open_to_buy_dataframe = pd.DataFrame(discretise_data['bc_open_to_buy'])
        est.fit(bc_open_to_buy_dataframe)
        bc_open_to_buy_dataframe = est.transform(bc_open_to_buy_dataframe)
        discretise_data['bc_open_to_buy'] = bc_open_to_buy_dataframe

        est = KBinsDiscretizer(n_bins= 50, encode='ordinal', strategy='kmeans')
        bc_util_dataframe = pd.DataFrame(discretise_data['bc_util'])
        est.fit(bc_util_dataframe)
        bc_util_dataframe = est.transform(bc_util_dataframe)
        discretise_data['bc_util'] = bc_util_dataframe

        est = KBinsDiscretizer(n_bins= 50, encode='ordinal', strategy='kmeans')
        delinq_amnt_dataframe = pd.DataFrame(discretise_data['delinq_amnt'])
        est.fit(delinq_amnt_dataframe)
        delinq_amnt_dataframe = est.transform(delinq_amnt_dataframe)
        discretise_data['delinq_amnt'] = delinq_amnt_dataframe

        est = KBinsDiscretizer(n_bins= 50, encode='ordinal', strategy='kmeans')
        mo_sin_old_il_acct_dataframe = pd.DataFrame(discretise_data['mo_sin_old_il_acct'])
        est.fit(mo_sin_old_il_acct_dataframe)
        mo_sin_old_il_acct_dataframe = est.transform(mo_sin_old_il_acct_dataframe)
        discretise_data['mo_sin_old_il_acct'] = mo_sin_old_il_acct_dataframe

        est = KBinsDiscretizer(n_bins= 50, encode='ordinal', strategy='kmeans')
        mo_sin_old_rev_tl_op_dataframe = pd.DataFrame(discretise_data['mo_sin_old_rev_tl_op'])
        est.fit(mo_sin_old_rev_tl_op_dataframe)
        mo_sin_old_rev_tl_op_dataframe = est.transform(mo_sin_old_rev_tl_op_dataframe)
        discretise_data['mo_sin_old_rev_tl_op'] = mo_sin_old_rev_tl_op_dataframe

        est = KBinsDiscretizer(n_bins= 50, encode='ordinal', strategy='kmeans')
        mo_sin_rcnt_rev_tl_op_dataframe = pd.DataFrame(discretise_data['mo_sin_rcnt_rev_tl_op'])
        est.fit(mo_sin_rcnt_rev_tl_op_dataframe)
        mo_sin_rcnt_rev_tl_op_dataframe = est.transform(mo_sin_rcnt_rev_tl_op_dataframe)
        discretise_data['mo_sin_rcnt_rev_tl_op'] = mo_sin_rcnt_rev_tl_op_dataframe

        est = KBinsDiscretizer(n_bins= 50, encode='ordinal', strategy='kmeans')
        mo_sin_rcnt_tl_dataframe = pd.DataFrame(discretise_data['mo_sin_rcnt_tl'])
        est.fit(mo_sin_rcnt_tl_dataframe)
        mo_sin_rcnt_tl_dataframe = est.transform(mo_sin_rcnt_tl_dataframe)
        discretise_data['mo_sin_rcnt_tl'] = mo_sin_rcnt_tl_dataframe

        est = KBinsDiscretizer(n_bins= 41, encode='ordinal', strategy='kmeans')
        mort_acc_dataframe = pd.DataFrame(discretise_data['mort_acc'])
        est.fit(mort_acc_dataframe)
        mort_acc_dataframe = est.transform(mort_acc_dataframe)
        discretise_data['mort_acc'] = mort_acc_dataframe

        est = KBinsDiscretizer(n_bins= 50, encode='ordinal', strategy='kmeans')
        mths_since_recent_bc_dataframe = pd.DataFrame(discretise_data['mths_since_recent_bc'])
        est.fit(mths_since_recent_bc_dataframe)
        mths_since_recent_bc_dataframe = est.transform(mths_since_recent_bc_dataframe)
        discretise_data['mths_since_recent_bc'] = mths_since_recent_bc_dataframe

        est = KBinsDiscretizer(n_bins= 25, encode='ordinal', strategy='kmeans')
        mths_since_recent_inq_dataframe = pd.DataFrame(discretise_data['mths_since_recent_inq'])
        est.fit(mths_since_recent_inq_dataframe)
        mths_since_recent_inq_dataframe = est.transform(mths_since_recent_inq_dataframe)
        discretise_data['mths_since_recent_inq'] = mths_since_recent_inq_dataframe

        est = KBinsDiscretizer(n_bins= 41, encode='ordinal', strategy='kmeans')
        num_accts_ever_120_pd_dataframe = pd.DataFrame(discretise_data['num_accts_ever_120_pd'])
        est.fit(num_accts_ever_120_pd_dataframe)
        num_accts_ever_120_pd_dataframe = est.transform(num_accts_ever_120_pd_dataframe)
        discretise_data['num_accts_ever_120_pd'] = num_accts_ever_120_pd_dataframe

        est = KBinsDiscretizer(n_bins= 36, encode='ordinal', strategy='kmeans')
        num_actv_bc_tl_dataframe = pd.DataFrame(discretise_data['num_actv_bc_tl'])
        est.fit(num_actv_bc_tl_dataframe)
        num_actv_bc_tl_dataframe = est.transform(num_actv_bc_tl_dataframe)
        discretise_data['num_actv_bc_tl'] = num_actv_bc_tl_dataframe

        est = KBinsDiscretizer(n_bins= 49, encode='ordinal', strategy='kmeans')
        num_actv_rev_tl_dataframe = pd.DataFrame(discretise_data['num_actv_rev_tl'])
        est.fit(num_actv_rev_tl_dataframe)
        num_actv_rev_tl_dataframe = est.transform(num_actv_rev_tl_dataframe)
        discretise_data['num_actv_rev_tl'] = num_actv_rev_tl_dataframe

        est = KBinsDiscretizer(n_bins= 50, encode='ordinal', strategy='kmeans')
        num_bc_sats_dataframe = pd.DataFrame(discretise_data['num_bc_sats'])
        est.fit(num_bc_sats_dataframe)
        num_bc_sats_dataframe = est.transform(num_bc_sats_dataframe)
        discretise_data['num_bc_sats'] = num_bc_sats_dataframe


        est = KBinsDiscretizer(n_bins= 50, encode='ordinal', strategy='kmeans')
        num_bc_tl_dataframe = pd.DataFrame(discretise_data['num_bc_tl'])
        est.fit(num_bc_tl_dataframe)
        num_bc_tl_dataframe = est.transform(num_bc_tl_dataframe)
        discretise_data['num_bc_tl'] = num_bc_tl_dataframe

        est = KBinsDiscretizer(n_bins= 50, encode='ordinal', strategy='kmeans')
        num_il_tl_dataframe = pd.DataFrame(discretise_data['num_il_tl'])
        est.fit(num_il_tl_dataframe)
        num_il_tl_dataframe = est.transform(num_il_tl_dataframe)
        discretise_data['num_il_tl'] = num_il_tl_dataframe

        est = KBinsDiscretizer(n_bins= 50, encode='ordinal', strategy='kmeans')
        num_op_rev_tl_dataframe = pd.DataFrame(discretise_data['num_op_rev_tl'])
        est.fit(num_op_rev_tl_dataframe)
        num_op_rev_tl_dataframe = est.transform(num_op_rev_tl_dataframe)
        discretise_data['num_op_rev_tl'] = num_op_rev_tl_dataframe

        est = KBinsDiscretizer(n_bins= 50, encode='ordinal', strategy='kmeans')
        num_rev_accts_dataframe = pd.DataFrame(discretise_data['num_rev_accts'])
        est.fit(num_rev_accts_dataframe)
        num_rev_accts_dataframe = est.transform(num_rev_accts_dataframe)
        discretise_data['num_rev_accts'] = num_rev_accts_dataframe

        est = KBinsDiscretizer(n_bins= 49, encode='ordinal', strategy='kmeans')
        num_rev_tl_bal_gt_0_dataframe = pd.DataFrame(discretise_data['num_rev_tl_bal_gt_0'])
        est.fit(num_rev_tl_bal_gt_0_dataframe)
        num_rev_tl_bal_gt_0_dataframe = est.transform(num_rev_tl_bal_gt_0_dataframe)
        discretise_data['num_rev_tl_bal_gt_0'] = num_rev_tl_bal_gt_0_dataframe

        est = KBinsDiscretizer(n_bins= 50, encode='ordinal', strategy='kmeans')
        num_sats_dataframe = pd.DataFrame(discretise_data['num_sats'])
        est.fit(num_sats_dataframe)
        num_sats_dataframe = est.transform(num_sats_dataframe)
        discretise_data['num_sats'] = num_sats_dataframe

        est = KBinsDiscretizer(n_bins= 6, encode='ordinal', strategy='kmeans')
        num_tl_120dpd_2m_dataframe = pd.DataFrame(discretise_data['num_tl_120dpd_2m'])
        est.fit(num_tl_120dpd_2m_dataframe)
        num_tl_120dpd_2m_dataframe = est.transform(num_tl_120dpd_2m_dataframe)
        discretise_data['num_tl_120dpd_2m'] = num_tl_120dpd_2m_dataframe

        est = KBinsDiscretizer(n_bins= 5, encode='ordinal', strategy='kmeans')
        num_tl_30dpd_dataframe = pd.DataFrame(discretise_data['num_tl_30dpd'])
        est.fit(num_tl_30dpd_dataframe)
        num_tl_30dpd_dataframe = est.transform(num_tl_30dpd_dataframe)
        discretise_data['num_tl_30dpd'] = num_tl_30dpd_dataframe

        est = KBinsDiscretizer(n_bins= 29, encode='ordinal', strategy='kmeans')
        num_tl_90g_dpd_24m_dataframe = pd.DataFrame(discretise_data['num_tl_90g_dpd_24m'])
        est.fit(num_tl_90g_dpd_24m_dataframe)
        num_tl_90g_dpd_24m_dataframe = est.transform(num_tl_90g_dpd_24m_dataframe)
        discretise_data['num_tl_90g_dpd_24m'] = num_tl_90g_dpd_24m_dataframe

        est = KBinsDiscretizer(n_bins= 30, encode='ordinal', strategy='kmeans')
        num_tl_op_past_12m_dataframe = pd.DataFrame(discretise_data['num_tl_op_past_12m'])
        est.fit(num_tl_op_past_12m_dataframe)
        num_tl_op_past_12m_dataframe = est.transform(num_tl_op_past_12m_dataframe)
        discretise_data['num_tl_op_past_12m'] = num_tl_op_past_12m_dataframe

        est = KBinsDiscretizer(n_bins= 50, encode='ordinal', strategy='kmeans')
        pct_tl_nvr_dlq_dataframe = pd.DataFrame(discretise_data['pct_tl_nvr_dlq'])
        est.fit(pct_tl_nvr_dlq_dataframe)
        pct_tl_nvr_dlq_dataframe = est.transform(pct_tl_nvr_dlq_dataframe)
        discretise_data['pct_tl_nvr_dlq'] = pct_tl_nvr_dlq_dataframe

        est = KBinsDiscretizer(n_bins= 50, encode='ordinal', strategy='kmeans')
        percent_bc_gt_75_dataframe = pd.DataFrame(discretise_data['percent_bc_gt_75'])
        est.fit(percent_bc_gt_75_dataframe)
        percent_bc_gt_75_dataframe = est.transform(percent_bc_gt_75_dataframe)
        discretise_data['percent_bc_gt_75'] = percent_bc_gt_75_dataframe

        est = KBinsDiscretizer(n_bins= 10, encode='ordinal', strategy='kmeans')
        pub_rec_bankruptcies_dataframe = pd.DataFrame(discretise_data['pub_rec_bankruptcies'])
        est.fit(pub_rec_bankruptcies_dataframe)
        pub_rec_bankruptcies_dataframe = est.transform(pub_rec_bankruptcies_dataframe)
        discretise_data['pub_rec_bankruptcies'] = pub_rec_bankruptcies_dataframe

        est = KBinsDiscretizer(n_bins= 32, encode='ordinal', strategy='kmeans')
        tax_liens_dataframe = pd.DataFrame(discretise_data['tax_liens'])
        est.fit(tax_liens_dataframe)
        tax_liens_dataframe = est.transform(tax_liens_dataframe)
        discretise_data['tax_liens'] = tax_liens_dataframe


        est = KBinsDiscretizer(n_bins= 50, encode='ordinal', strategy='kmeans')
        tot_hi_cred_lim_dataframe = pd.DataFrame(discretise_data['tot_hi_cred_lim'])
        est.fit(tot_hi_cred_lim_dataframe)
        tot_hi_cred_lim_dataframe = est.transform(tot_hi_cred_lim_dataframe)
        discretise_data['tot_hi_cred_lim'] = tot_hi_cred_lim_dataframe

        est = KBinsDiscretizer(n_bins= 50, encode='ordinal', strategy='kmeans')
        total_bal_ex_mort_dataframe = pd.DataFrame(discretise_data['total_bal_ex_mort'])
        est.fit(total_bal_ex_mort_dataframe)
        total_bal_ex_mort_dataframe = est.transform(total_bal_ex_mort_dataframe)
        discretise_data['total_bal_ex_mort'] = total_bal_ex_mort_dataframe

        est = KBinsDiscretizer(n_bins= 50, encode='ordinal', strategy='kmeans')
        total_bc_limit_dataframe = pd.DataFrame(discretise_data['total_bc_limit'])
        est.fit(total_bc_limit_dataframe)
        total_bc_limit_dataframe = est.transform(total_bc_limit_dataframe)
        discretise_data['total_bc_limit'] = total_bc_limit_dataframe

        est = KBinsDiscretizer(n_bins= 50, encode='ordinal', strategy='kmeans')
        total_il_high_credit_limit_dataframe = pd.DataFrame(discretise_data['total_il_high_credit_limit'])
        est.fit(total_il_high_credit_limit_dataframe)
        total_il_high_credit_limit_dataframe = est.transform(total_il_high_credit_limit_dataframe)
        discretise_data['total_il_high_credit_limit'] = total_il_high_credit_limit_dataframe

        
        return discretise_data
    
    

    def preprocess_data(data: pd.DataFrame):
        # normalizes and discretises data
        #normalized_data = DataPreprocessing.normalize_data(data)
        discretised_data = DataPreprocessing.discretise_data(data)
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