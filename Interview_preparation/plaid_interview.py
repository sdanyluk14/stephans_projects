import pandas as pd

class Plaid:
    def __init__(self, link):
        self.df = pd.read_csv(link)

plaid = Plaid('Interview_preparation/ds_interview_financial_security_data.csv')

print(plaid.df.head())

0.8849192717279285
0.8849192717279285