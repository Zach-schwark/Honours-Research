# Notes to keep track of what I've done when.

## Data Preprocessing:

### Feature extraction/engineering:

- consider removing "addr_state" since it has 50 distict values, which is a lot regarding complexity of the model 

### Discretisation:

### Other preprocessing:


## Structure Learning:

### different scores:

#### priors/pseudo counts:


## Parameter Estimation:

### Hyperparameters / priors:


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

Basic List:

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
- **pub_rec**: Number of derogatory public records
- **open_acc**: The number of open credit lines in the borrower's credit file.
- **total_acc**: The total number of credit lines currently in the borrower's credit file.
- **avg_cur_bal**: Average current balance of all accounts.
- **tot_cur_bal**: Total current balance of all accounts.
- **tax_liens**: Number of tax liens.
- **pub_rec_bankruptcies**: Number of public record bankruptcies.
- **revol_bal**: Total credit revolving balance.
- **mort_acc**: Number of mortgage accounts.
- **num_il_tl**: Number of installment accounts.
- **num_actv_rev_tl**: Number of currently active revolving trades.
- **num_op_rev_tl**: Number of open revolving accounts.

More Detailed List:

Features that are in the basic list plus:

earliest_cr_line, mo_sin_old_rev_tl_op, pct_tl_nvr_dlq, max_bal_bc, total_bal_ex_mort, acc_now_delinq, total_rev_hi_lim, num_actv_bc_tl, total_bal_il

- **earliest_cr_line**: The month the borrower's earliest reported credit line was opened.
- **mo_sin_old_rev_tl_op**: Months since oldest revolving account opened.
- **pct_tl_nvr_dlq**: Percent of trades never delinquent.
- **max_bal_bc**: Maximum current balance owed on all revolving accounts.
- **total_bal_ex_mort**: Total credit balance excluding mortgage.
- **acc_now_delinq**: The number of accounts on which the borrower is now delinquent.
- **total_rev_hi_lim**: Total revolving high credit/credit limit.
- **num_actv_bc_tl**: Number of currently active bankcard accounts.
- **total_bal_il**: Total current balance of all installment accounts.



Advanced List:

The previous 2 lists plus:

num_tl_90g_dpd_24m, num_rev_accts,  inq_last_6mths, mths_since_recent_inq, revol_util, all_util, mo_sin_old_il_acct, num_tl_30dpd, open_acc_6m, bc_util, total_cu_tl,total_bc_limit, num_tl_120dpd_2m, num_bc_tl, num_bc_sats

- **num_tl_90g_dpd_24m**: Number of accounts 90 or more days past due in last 24 months.
- **num_rev_accts**: Number of revolving accounts.
- **inq_last_6mths**: The number of inquiries in past 6 months (excluding auto and mortgage inquiries).
- **mths_since_recent_inq**: Months since most recent inquiry.
- **revol_util**: Revolving line utilization rate, or the amount of credit the borrower is using relative to all available revolving credit.
- **all_util**: Balance to credit limit on all trades.
- **mo_sin_old_il_acct**: Months since oldest bank installment account opened.
- **num_tl_30dpd**: Number of accounts currently 30 days past due (updated in past 2 months).
- **open_acc_6m**: Number of open trades in last 6 months
- **bc_util**: Ratio of total current balance to high credit/credit limit for all bankcard accounts.
- **total_cu_tl**: Number of finance trades.
- **total_bc_limit**: Total bankcard high credit/credit limit.
- **num_tl_120dpd_2m**: Number of accounts currently 120 days past due (updated in past 2 months)
- **num_bc_tl**: Number of bankcard accounts.
- **num_bc_sats**: Number of satisfactory bankcard accounts.


maybe open_act_il - im assuming this is " number of open_active_installment accounts, but cant assume

### Target Features / Probability distribution:

#### Initial target feature list:
- Only did for the BIC score
- trained on 10 000 lines of data
- BIC score -> therefore Dirichlet prior
- I trained the model a couples of times and looked at the nodes that appeared most often / were consistent
- I included the highest number of features relating to loan stuture that I could that were in the network.
- I plan to do finance research to decide on which features would be the most useful

