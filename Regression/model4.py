import pandas as pd
import statsmodels.formula.api as smf

df = pd.read_excel(r'C:\Users\examp\OneDrive\Робочий стіл\data_cts_violent_and_sexual_crime.xlsx')
filtered_df = df[df['Unit of measurement'].str.strip().str.lower() == 'counts']

house = filtered_df[['VALUE', 'Country', 'Indicator', 'Dimension', 'Category', 'Sex']]
predictors = ['Country', 'Indicator', 'Dimension', 'Category', 'Sex']
outcome = 'VALUE'

formula = outcome + ' ~ ' + ' + '.join(predictors)
model = smf.ols(formula, data=house)
results = model.fit()
print(results.summary())