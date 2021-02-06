import pandas as pd

def categorizeVariables(df_loan_data):
    # Borrower state from string to category
    df_loan_data.BorrowerState = df_loan_data.BorrowerState.astype('category')
    
    # Occupation from string to category
    df_loan_data.Occupation = df_loan_data.Occupation.astype('category')
    
    # Employment status from string to category
    df_loan_data.EmploymentStatus = df_loan_data.EmploymentStatus.astype('category')
    
    # Loan status from string to ordered category
    loan_status_list = ['Chargedoff',
                        'Defaulted',
                        'Past Due (>120 days)',
                        'Past Due (91-120 days)',
                        'Past Due (61-90 days)',
                        'Past Due (31-60 days)',
                        'Past Due (16-30 days)',
                        'Past Due (1-15 days)',
                        'Current',
                        'FinalPaymentInProgress',
                        'Completed',
                        'Cancelled',]
    loan_status_class = pd.api.types.CategoricalDtype(ordered=True, categories=loan_status_list)
    df_loan_data.LoanStatus = df_loan_data.LoanStatus.astype(loan_status_class);
    
    # Listing category from string to category
    df_loan_data.ListingCategory = df_loan_data.ListingCategory.astype('category')
    
    # Loan origination date from string to DateTime
    df_loan_data.LoanOriginationDate = pd.to_datetime(df_loan_data.LoanOriginationDate)