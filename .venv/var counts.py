import pandas as pd

df = pd.read_excel(r'C:\Users\examp\OneDrive\Робочий стіл\data_cts_violent_and_sexual_crime.xlsx')
filtered_df = df[df['Unit of measurement'].str.strip().str.lower() == 'counts']
variance = filtered_df['VALUE'].var()

print(f"Вибіркова дисперсія: {variance:.2f}")