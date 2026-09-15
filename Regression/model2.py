import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_excel(r'C:\Users\examp\OneDrive\Робочий стіл\data_cts_violent_and_sexual_crime.xlsx')
filtered_df = df[df['Unit of measurement'].str.strip().str.lower() == 'rate per 100,000 population']

predictors = ['Country', 'Indicator', 'Dimension', 'Category', 'Sex']
outcome = 'VALUE'
X = pd.get_dummies(filtered_df[predictors], drop_first=True)
y = filtered_df[outcome]
model = LinearRegression()
model.fit(X, y)
print("Intercept:", model.intercept_)
print("Coefficients:")
for feature, coef in zip(X.columns, model.coef_):
    print(f"{feature}: {coef}")
