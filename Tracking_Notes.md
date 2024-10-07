# Notes to keep track of what I've done when.

## Data Preprocessing:

### Feature extraction/engineering:

- consider removing "addr_state" since it has 50 distict values, which is a lot regarding complexity of the model 

### Discretisation:

### Other preprocessing:




## Fine Tuning:

First run / Finetuning:

    first run on whole datset did not work out. I ran into problems.
    Needing over 190GB of RAM for the BDs BN
    the BDeu taking over 13 hours just for stucture learning
    the BIC still runing over 13 hours aswell etc

### 1 run on 10 000 lines
####  ess=10 for structure learning priors, k2 sccore for parameter estimation

random:
- full: -83716.11
- desired: -5498.7417

BIC:
- full: -96348.92
- desired: -2750.0156

Bdeu:\
this score was estimated to take 33 days to complete the variable elimination of the desired distribution so I stopped it.
- full:
- desired: 

BDs:
- full: -97380.44
- desired: -2769.0144

K2:
- full: -99207.66
- desired: -2794.0796

##### ess=100 for structure learning priors:

these ran quicker with the prior, decreseing the prior might make it more accurate but run quicker

Bdeu:
- full: -82066.55
- desired: -2948.395

BDs:
- full: -97783.914
- desired: -2694.8018

##### ess=50 for structure learning priors:

Bdeu:
- full: -81801.016
- desired: -2977.7705

BDs:
- full: -98273.375
- desired: -2764.6963

###### ess=1000 for structure learning priors:

Bdeu:
- full: 
- desired: 

BDs:
- full: -101985.39
- desired: -2875.7534

####  ess=10 for structure learning priors, BDeu score for parameter estimation

BIC:
- full: -95452.75
- desired: -2857.6394

Bdeu:
- full:
- desired: 

BDs:
- full:
- desired: 

K2:
- full: -97256.83
- desired: -2687.0728


#### ess=1000 for structure learning, BDeu with ess=1000 for parameter estimation

##### LogLikelihood:
random:
- ran into error 

BIC:
- full: -101404.875
- desired: -3206.0286

Bdeu:
- full: -86472.68
- desired: ran into error, int_rate not in graph

BDs:
- full: -103673.555
- desired: -3013.8362

K2:
- full: -98227.16
- desired: -3059.7332

Chow-Liu:
- full: -103353.125
- desired: -3203.9448

##### Correlation:

random:
- ran into error

BIC:
- accuracy: 0.5525150905432595
- f1: 0.0

Bdeu:
- ran into error

BDs:
- accuracy: 0.42160493827160495
- f1: 0.0

K2:
- accuracy: 0.4560126582278481
- f1: 0.07030827474310439

Chow-Liu:
- accuracy: 0.44537037037037036
- f1: 0.0


#### ess=50 for structure learning, BDeu with ess=50 for parameter estimation

##### LogLikelihood:
random:
- full: 
- desired: 

BIC:
- full: -95383.305,
- desired: -2759.7083,

Bdeu:
- full: -80765.58,
- desired: -2874.6968,

BDs:
- full: -inf,
- desired: nan,

K2:
- full: -97868.92,
- desired: -2827.8086,

Chow-Liu:
- full: 
- desired: 

##### Correlation:

random:
- accuracy:
- f1: 

BIC:
- accuracy: 0.5205479452054794,
- f1: 0.0,

Bdeu:
- accuracy: 0.5916515426497277,
- f1: 0.0425531914893617,

BDs:
- accuracy: 0.4661392405063291,
- f1: 0.0,

K2:
- accuracy: 0.4800389483933788,
- f1: 0.011111111111111112,

Chow-Liu:
- accuracy: 
- f1: 

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
