import pandas as pd
import numpy as np

df = pd.read_excel(r'C:\Users\examp\OneDrive\Робочий стіл\data_cts_violent_and_sexual_crime.xlsx')
filtered_df = df[df['Unit of measurement'].str.strip().str.lower() == 'rate per 100,000 population']

def interquartile_range(values):
    q1 = np.percentile(values, 25)
    print(f"25% квантиль: {q1:.2f}")
    q3 = np.percentile(values, 75)
    print(f"75% квантиль: {q3:.2f}")
    # Обчислення міжквантильного розмаху
    iqr = q3 - q1
    return iqr

iqr = interquartile_range(filtered_df['VALUE'])

print(f"Міжквантильний розмах: {iqr:.2f}")