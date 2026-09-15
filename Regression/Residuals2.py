import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_excel(r'C:\Users\examp\OneDrive\Робочий стіл\data_cts_violent_and_sexual_crime.xlsx')
filtered_df = df[df['Unit of measurement'].str.strip().str.lower() == 'counts']

x = filtered_df['Year']
y = filtered_df['VALUE']

coefficients = np.polyfit(x, y, 1)
polynomial = np.poly1d(coefficients)
y_fit = polynomial(x)

ax = filtered_df.plot.scatter(x='Year', y='VALUE', figsize=(4, 4))
ax.plot(x, y_fit)

for x_val, y_actual, y_fitted in zip(x, y, y_fit):
    ax.plot((x_val, x_val), (y_actual, y_fitted), '--', color='C1')

plt.tight_layout()
plt.show()
