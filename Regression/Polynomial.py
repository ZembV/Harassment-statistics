import pandas as pd
import statsmodels.formula.api as smf

df = pd.read_excel(r'C:\Users\examp\OneDrive\Робочий стіл\data_cts_violent_and_sexual_crime.xlsx')
filtered_df = df[df['Unit of measurement'].str.strip().str.lower() == 'rate per 100,000 population']

house = filtered_df[['VALUE', 'Country', 'Indicator', 'Dimension', 'Category', 'Sex', 'Year']]

model_poly = smf.ols(formula='VALUE ~ Country + Indicator + Dimension + Category + Sex + Year', data=house)
result_poly = model_poly.fit()

print(result_poly.summary())