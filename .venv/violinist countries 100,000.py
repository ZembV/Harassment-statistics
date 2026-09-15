import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(r'C:\Users\examp\OneDrive\Робочий стіл\data_cts_violent_and_sexual_crime.xlsx')
filtered_df = df[df['Unit of measurement'].str.strip().str.lower() == 'rate per 100,000 population']

top_10_countries = filtered_df.groupby('Country')['VALUE'].sum().nlargest(10)

plt.figure(figsize=(10, 6))
plt.violinplot([filtered_df[filtered_df['Country'] == country]['VALUE'] for country in top_10_countries.index], showmeans=True)
plt.xticks(range(1, len(top_10_countries) + 1), top_10_countries.index, rotation=45, ha='right')
plt.ylabel('Value')
plt.title('Скрипковий графік для 10 країн з найбільшою кількістю сексуальних злочинів')
plt.tight_layout()
plt.show()
