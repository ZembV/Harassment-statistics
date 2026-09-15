import pandas as pd
import statsmodels.formula.api as smf

df = pd.read_excel(r'C:\Users\examp\OneDrive\Робочий стіл\data_cts_violent_and_sexual_crime.xlsx')
filtered_df = df[df['Unit of measurement'].str.strip().str.lower() == 'rate per 100,000 population']

house = filtered_df[['VALUE', 'Dimension', 'Category', 'Sex', 'Year']]
formula = ('VALUE ~ Dimension + Category + Sex + Year')
model_spline = smf.ols(formula=formula, data=house)
result_spline = model_spline.fit()
print(result_spline.summary())
