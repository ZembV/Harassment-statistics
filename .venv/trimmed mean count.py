import pandas as pd
from scipy.stats import trim_mean

df = pd.read_excel(r'C:\Users\examp\OneDrive\Робочий стіл\data_cts_violent_and_sexual_crime.xlsx')
filtered_df = df[df['Unit of measurement'].str.strip().str.lower() == 'counts']
trimmed_mean = trim_mean(filtered_df['VALUE'], 0.1)

print(f"Середнє усічене значення для стовпця 'VALUE': {trimmed_mean:.2f}")