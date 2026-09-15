import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel(r'C:\Users\examp\OneDrive\Робочий стіл\data_cts_violent_and_sexual_crime.xlsx')

filtered_df_rate = df[df['Unit of measurement'].str.strip().str.lower() == 'rate per 100,000 population']
filtered_df_counts = df[df['Unit of measurement'].str.strip().str.lower() == 'counts']

numeric_column = 'VALUE'

t_distribution_rate = stats.t(df=len(filtered_df_rate) - 1, loc=filtered_df_rate[numeric_column].mean(), scale=filtered_df_rate[numeric_column].std())

t_distribution_counts = stats.t(df=len(filtered_df_counts) - 1, loc=filtered_df_counts[numeric_column].mean(), scale=filtered_df_counts[numeric_column].std())

x = np.linspace(t_distribution_rate.ppf(0.001), t_distribution_rate.ppf(0.999), 1000)
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(x, t_distribution_rate.pdf(x), 'r-', lw=2, label='t distribution')
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.title('t Distribution for Rate')
plt.legend()

x = np.linspace(t_distribution_counts.ppf(0.001), t_distribution_counts.ppf(0.999), 1000)
plt.subplot(1, 2, 2)
plt.plot(x, t_distribution_counts.pdf(x), 'b-', lw=2, label='t distribution')
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.title('t Distribution for Counts')
plt.legend()

plt.tight_layout()
plt.show()
