import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel(r'C:\Users\examp\OneDrive\Робочий стіл\data_cts_violent_and_sexual_crime.xlsx')
filtered_df = df[df['Unit of measurement'].str.strip().str.lower() == 'rate per 100,000 population']
mean_values = filtered_df.groupby('Region')['VALUE'].mean().reset_index()

categories = mean_values['Region']
values = mean_values['VALUE']

plt.bar(categories, values)
plt.xlabel("Region")
plt.ylabel("Average VALUE")
plt.title("Стовпчикова діаграма за обмеженням 'rate per 100,000 population'")
plt.xticks(rotation=45)
plt.bar(categories, values, color='#bcffb3')

plt.savefig('avg_coropchart.png')
plt.show()