import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

df = pd.read_excel(r'C:\Users\examp\OneDrive\Робочий стіл\data_cts_violent_and_sexual_crime.xlsx')

filtered_df_rate = df[df['Unit of measurement'].str.strip().str.lower() == 'rate per 100,000 population']

n = len(filtered_df_rate)
p = len(filtered_df_rate[filtered_df_rate['VALUE'] > 42.47]) / n

x = np.arange(binom.ppf(0.01, n, p), binom.ppf(0.99, n, p))
plt.plot(x, binom.pmf(x, n, p), 'bo', ms=8, label='binom pmf')
plt.vlines(x, 0, binom.pmf(x, n, p), colors='b', lw=5, alpha=0.5)

plt.show()


