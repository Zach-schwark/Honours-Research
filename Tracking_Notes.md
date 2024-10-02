# Notes to keep track of what I've done when.

## Data Preprocessing:

### Feature extraction/engineering:

- consider removing "addr_state" since it has 50 distict values, which is a lot regarding complexity of the model 

### Discretisation:

### Other preprocessing:




## Fine Tuning:

First run / Finetuning:

1 run on whole dataset 

## Structure Learning:

### different scores:
random
BIC
Bdeu
BDs
K2

#### priors/pseudo counts:

First run/finetuning:

BDeu: equivalent sample size = 10 
BD2: equivalent sample size = 10


## Parameter Estimation:

### Hyperparameters / priors:

First run/finetuning:

All models had K2 prior.

## Inference:

### Evidence List:

#### Initial evidence list:
- Only did for the BIC score
- trained on 10 000 lines of data
- BIC score -> therefore Dirichlet prior
- I trained the model a couples of times and looked at the nodes that appeared most often / were consistent
- I only included features that were in the active trail of my target distribution features
- I plan to do finance research to decide on which features would be the most useful

##### features in network that relate to customer:

#### Very Basic List:


- **annual_inc**: The self-reported annual income provided by the borrower during registration.
- **emp_length**: Employment length in years. Possible values are between 0 and 10 where 0 means less than one year and 10 means ten or more years.
- **grade**: LC assigned loan grade
- **fico_range_high**: The upper boundary range the borrower’s FICO at loan origination belongs to.
- **purpose**: A category provided by the borrower for the loan request.
- **dti**: A ratio calculated using the borrower’s total monthly debt payments on the total debt obligations, excluding mortgage and the requested LC loan, divided by the borrower’s self-reported monthly income
- **home_ownership**: The home ownership status provided by the borrower during registration. Our values are: RENT, OWN, MORTGAGE, OTHER.
- **tot_cur_bal**: Total current balance of all accounts.
- **pub_rec_bankruptcies**: Number of public record bankruptcies.
- **verification_status**: Indicates if income was verified by LC, not verified, or if the income source was verified

#### Basic List:

annual_inc, grade, verification_status, last_fico_range_high, home_ownership, purpose, dti, application_type, delinq_2yrs, fico_range_high, pub_rec, open_acc, total_acc, avg_cur_bal, tax_liens, pub_rec_bankruptcies, revol_bal, tot_cur_bal, emp_length, mort_acc, num_il_tl, num_actv_rev_tl, num_op_rev_tl

- **annual_inc**: The self-reported annual income provided by the borrower during registration.
- **emp_length**: Employment length in years. Possible values are between 0 and 10 where 0 means less than one year and 10 means ten or more years.
- **grade**: LC assigned loan grade
- **home_ownership**: The home ownership status provided by the borrower during registration. Our values are: RENT, OWN, MORTGAGE, OTHER.
- **verification_status**: Indicates if income was verified by LC, not verified, or if the income source was verified
- **last_fico_range_high**: The upper boundary range the borrower’s last FICO pulled belongs to.
- **fico_range_high**: The upper boundary range the borrower’s FICO at loan origination belongs to.
- **purpose**: A category provided by the borrower for the loan request.
- **dti**: A ratio calculated using the borrower’s total monthly debt payments on the total debt obligations, excluding mortgage and the requested LC loan, divided by the borrower’s self-reported monthly income
- **application_type**: Indicates whether the loan is an individual application or a joint application with two co-borrowers.
- **delinq_2yrs**: The number of 30+ days past-due incidences of delinquency in the borrower's credit file for the past 2 years.
- **avg_cur_bal**: Average current balance of all accounts.
- **tot_cur_bal**: Total current balance of all accounts.
- **pub_rec_bankruptcies**: Number of public record bankruptcies.
- **mort_acc**: Number of mortgage accounts.
- **num_il_tl**: Number of installment accounts.
- **num_rev_accts**: Number of revolving accounts.
- **total_bal_ex_mort**: Total credit balance excluding mortgage.



#### More Detailed List:

Features that are in the basic list plus:

earliest_cr_line, mo_sin_old_rev_tl_op, pct_tl_nvr_dlq, max_bal_bc, total_bal_ex_mort, acc_now_delinq, total_rev_hi_lim, num_actv_bc_tl, total_bal_il

- **revol_bal**: Total credit revolving balance.
- **num_actv_rev_tl**: Number of currently active revolving trades.
- **num_op_rev_tl**: Number of open revolving accounts.
- **max_bal_bc**: Maximum current balance owed on all revolving accounts.
- **total_rev_hi_lim**: Total revolving high credit/credit limit.
- **total_bal_il**: Total current balance of all installment accounts.
- **open_acc**: The number of open credit lines in the borrower's credit file.
- **total_acc**: The total number of credit lines currently in the borrower's credit file.
- **tax_liens**: Number of tax liens.
- **pub_rec**: Number of derogatory public records
- **num_bc_tl**: Number of bankcard accounts.
- **earliest_cr_line**: The month the borrower's earliest reported credit line was opened.
- **pct_tl_nvr_dlq**: Percent of trades never delinquent.
- **acc_now_delinq**: The number of accounts on which the borrower is now delinquent.

#### Advanced List:

The previous 2 lists plus:

- **revol_util**: Revolving line utilization rate, or the amount of credit the borrower is using relative to all available revolving credit.
- **all_util**: Balance to credit limit on all trades.
- **bc_util**: Ratio of total current balance to high credit/credit limit for all bankcard accounts.
- **total_cu_tl**: Number of finance trades.
- **total_bc_limit**: Total bankcard high credit/credit limit.
- **num_actv_bc_tl**: Number of currently active bankcard accounts.
- **num_bc_sats**: Number of satisfactory bankcard accounts.
- **percent_bc_gt_75**: Percentage of all bankcard accounts > 75% of limit.
- **num_tl_30dpd**: Number of accounts currently 30 days past due (updated in past 2 months).
- **num_tl_90g_dpd_24m**: Number of accounts 90 or more days past due in last 24 months.
- **num_tl_120dpd_2m**: Number of accounts currently 120 days past due (updated in past 2 months)
- **num_accts_ever_120_pd**: Number of accounts ever 120 or more days past due.


#### maybe (all_customer_info) :

- **open_il_12m**: Number of installment accounts opened in past 12 months
- **open_il_24m**: Number of installment accounts opened in past 24 months
- **num_tl_op_past_12m**: Number of accounts opened in past 12 months.
- **open_acc_6m**: Number of open trades in last 6 months
- **acc_open_past_24mths**: Number of trades opened in past 24 months.
- **open_rv_12m**: Number of revolving trades opened in past 12 months
- **open_rv_24m**: Number of revolving trades opened in past 24 months.
- **mo_sin_rcnt_tl**: Months since most recent account opened
- **mths_since_recent_bc**: Months since most recent bankcard account opened.
- **mo_sin_rcnt_rev_tl_op**: Months since most recent revolving account opened.
- **mo_sin_old_rev_tl_op**: Months since oldest revolving account opened.
- **mo_sin_old_il_acct**: Months since oldest bank installment account opened.
- **mths_since_recent_inq**: Months since most recent inquiry.
- **inq_fi**: Number of personal finance inquiries
- **inq_last_6mths**: The number of inquiries in past 6 months (excluding auto and mortgage inquiries).
- **inq_last_12m**: Number of credit inquiries in past 12 months
- **title**: The loan title provided by the borrower ( similar to what the loan is for)
- **bc_open_to_buy**: Total open to buy on revolving bankcards.


 open_act_il - I'm assuming this is " number of open_active_installment accounts, but cant assume

**initial_list_status** - The variable initial_list_status is available in the public data and identifies whether a loan was initially listed in the whole (W) or fractional (F) market. Loans listed “whole” become available for fractional funding (and vice versa) if there are no buyers within a certain time frame.



#### Features that often got removed from evidence list:
ie features that were continuously not in the model
used the all customer info list:

10 000 lines: 
- tax_liens
- pub_rec
- pub_rec_bankruptcies
- acc_now_delinq
- num_tl_30dpd
- purpose
- title

5000 lines:
- acc_now_delinq
- pub_rec
- pub_rec_bankruptcies
- num_tl_30dpd
- tax_liens
- title
- purpose
- emp_length 

2000 lines:
- acc_now_delinq
- pub_rec
- pub_rec_bankruptcies
- num_tl_30dpd
- tax_liens
- title
- purpose
- emp_length 
- total_cu_tl
- delinq_2yrs
- num_tl_90g_dpd_24m
- num_accts_ever_120_pd
- application_type
- pct_tl_nvr_dlq


50 000 lines:
- tax_liens

100 000 lines:
none


### Target Features / Probability distribution:

#### Initial target feature list:
- Only did for the BIC score
- trained on 10 000 lines of data
- BIC score -> therefore Dirichlet prior
- I trained the model a couples of times and looked at the nodes that appeared most often / were consistent
- I included the highest number of features relating to loan stuture that I could that were in the network.
- I plan to do finance research to decide on which features would be the most useful

Variables that are in network that relate to loan structure:

loan_amnt, installment, total_pymnt, total_rec_int, term, recoveries, last_pymnt_amnt, loan_status, int_rate,
disbursement_method, debt_settlement_flag, total_rec_late_fee, 

Target Loan structure variables:

- loan_amnt
- int_rate
- term
- installment
- disbursement_method

Variables to use in evidence to ensure positve outcome:

only this for now:
- loan_status - need to make "loan_status = fully paid"

figure out how to do this after initial inference setup:
- debt_settlement_flag - need to make "debt_settlement_flag = yes"
- total_rec_int - maybe try minimise this or maximise for bank profitability
- total_pymnt - maybe try minimise this or maximise for bank profitability
- total_rec_late_fee - need to try minimise this 
