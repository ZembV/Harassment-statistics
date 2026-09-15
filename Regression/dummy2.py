import pandas as pd
from sklearn.linear_model import LinearRegression
df = pd.read_excel(r'C:\Users\examp\OneDrive\Робочий стіл\data_cts_violent_and_sexual_crime.xlsx')
filtered_df = df[df['Unit of measurement'].str.strip().str.lower() == 'rate per 100,000 population']
house = filtered_df[['VALUE', 'Country', 'Indicator', 'Dimension', 'Category', 'Sex', 'Year']]
predictors = ['Country', 'Indicator', 'Dimension', 'Category', 'Sex']
outcome = 'VALUE'

X = pd.get_dummies(house[predictors], drop_first=True)
house_lm_factor = LinearRegression()
house_lm_factor.fit(X, house[outcome])

print(f'Intercept: {house_lm_factor.intercept_:.3f}')
print('Coefficients:')
for name, coef in zip(X.columns, house_lm_factor.coef_):
    print(f' {name}: {coef}')