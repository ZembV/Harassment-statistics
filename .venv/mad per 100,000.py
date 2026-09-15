import pandas as pd
import numpy as np

df = pd.read_excel(r'C:\Users\examp\OneDrive\Робочий стіл\data_cts_violent_and_sexual_crime.xlsx')
filtered_df = df[df['Unit of measurement'].str.strip().str.lower() == 'rate per 100,000 population']


def median_absolute_deviation(values):
    median_value = np.median(values)
    absolute_deviations = np.abs(values - median_value)
    mad_value = np.median(absolute_deviations)
    return mad_value
mad = median_absolute_deviation(filtered_df['VALUE'])

print(f"Абсолютне медіанне відхилення: {mad:.2f}")