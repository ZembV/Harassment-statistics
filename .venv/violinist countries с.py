import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

df = pd.read_excel(r'C:\Users\examp\OneDrive\Робочий стіл\data_cts_violent_and_sexual_crime.xlsx')
filtered_df_rate = df[df['Unit of measurement'].str.strip().str.lower() == 'rate per 100,000 population']
column_rate = filtered_df_rate['column_name']
plt.figure(figsize=(10,5))
plt.subplot(1, 2, 1)
stats.probplot(column_rate, plot=plt)
plt.title('Q-Q plot for rate per 100,000 population')
filtered_df_counts = df[df['Unit of measurement'].str.strip().str.lower() == 'counts']
column_counts = filtered_df_counts['column_name']
plt.subplot(1, 2, 2)
stats.probplot(column_counts, plot=plt)
plt.title('Q-Q plot for counts')

plt.tight_layout()
plt.show()
