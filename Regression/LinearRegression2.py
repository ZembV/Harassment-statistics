import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_excel(r'C:\Users\examp\OneDrive\Робочий стіл\data_cts_violent_and_sexual_crime.xlsx')
filtered_df = df[df['Unit of measurement'].str.strip().str.lower() == 'counts']

predictors = ['Year']
outcome = 'VALUE'
model = LinearRegression()
model.fit(filtered_df[predictors], filtered_df[outcome])
print(f'Intercept: {model.intercept_:.3f}')
print(f'Coefficient Exposure: {model.coef_[0]:.3f}')