import pandas as pd

def categorizeVariables(df_loan_data):
    
    # Occupation from string to category
    if 'Occupation' in df_loan_data.columns:
        df_loan_data.Occupation = df_loan_data.Occupation.astype('category')
    
    # Loan status from string to ordered category
    if 'LoanStatus' in df_loan_data.columns:
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
                        'Completed',]
        loan_status_class = pd.api.types.CategoricalDtype(ordered=True, categories=loan_status_list)
        df_loan_data.LoanStatus = df_loan_data.LoanStatus.astype(loan_status_class);
        
     # Loan status from string to ordered category
    if 'LoanStatusSimplified' in df_loan_data.columns:
        loan_simplified_status_list = ['PaymentsStopped',
                                       'PastDue',
                                       'Ongoing',
                                       'Completed']
        loan_simplified_status_class = pd.api.types.CategoricalDtype(ordered=True, categories=loan_simplified_status_list)
        df_loan_data.LoanStatusSimplified = df_loan_data.LoanStatusSimplified.astype(loan_simplified_status_class);
    
    # Listing category from string to category
    if 'ListingCategory' in df_loan_data.columns:
        df_loan_data.ListingCategory = df_loan_data.ListingCategory.astype('category')
    
    # Loan origination date from string to DateTime
    if 'LoanOriginationDate' in df_loan_data.columns:
        df_loan_data.LoanOriginationDate = pd.to_datetime(df_loan_data.LoanOriginationDate)