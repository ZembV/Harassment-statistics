import pandas as pd
import numpy as np

df = pd.read_excel(r'C:\Users\examp\OneDrive\Робочий стіл\data_cts_violent_and_sexual_crime.xlsx')
filtered_df = df[df['Unit of measurement'].str.strip().str.lower() == 'counts']

def mean_absolute_deviation(values):
    mean_value = np.mean(values)
    absolute_deviations = np.abs(values - mean_value)
    mad_value = np.mean(absolute_deviations)
    return mad_value

mad = mean_absolute_deviation(filtered_df['VALUE'])

print(f"Середнє абсолютне відхилення: {mad:.2f}")