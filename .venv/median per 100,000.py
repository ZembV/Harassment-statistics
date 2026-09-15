import pandas as pd

df = pd.read_excel(r'C:\Users\examp\OneDrive\Робочий стіл\data_cts_violent_and_sexual_crime.xlsx')
filtered_df = df[df['Unit of measurement'].str.strip().str.lower() == 'rate per 100,000 population']
median_value = filtered_df['VALUE'].median()

print(f"Медіана для стовпця 'VALUE': {median_value:.2f}")