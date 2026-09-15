import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel(r'C:\Users\examp\OneDrive\Робочий стіл\data_cts_violent_and_sexual_crime.xlsx')
filtered_df = df[df['Unit of measurement'].str.strip().str.lower() == 'counts']
categories = filtered_df["Region"]
values = filtered_df["VALUE"]
plt.bar(categories, values)
plt.bar(categories, values, color='#b3bcff')
plt.xlabel("Region")
plt.ylabel("VALUE")
plt.title("Стовпчикова діаграма за обмеженням 'counts'")
plt.xticks(rotation=45)

plt.savefig('coropchart.png')
plt.show()