import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel(r'C:\Users\examp\OneDrive\Робочий стіл\data_cts_violent_and_sexual_crime.xlsx')
filtered_df = df[df['Unit of measurement'].str.strip().str.lower() == 'rate per 100,000 population']

x = filtered_df['Year']
y = filtered_df['VALUE']
plt.scatter(x, y, color='#bcffb3', edgecolors='black')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlim(2000, 2024)
plt.xlabel('Year')
plt.ylabel('VALUE')
plt.show()
