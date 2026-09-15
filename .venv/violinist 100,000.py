import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(r'C:\Users\examp\OneDrive\Робочий стіл\data_cts_violent_and_sexual_crime.xlsx')
filtered_df = df[df['Unit of measurement'].str.strip().str.lower() == 'rate per 100,000 population']
plt.figure(figsize=(10, 6))
plt.violinplot(filtered_df['VALUE'], vert=False, showmedians=True)
plt.xlabel('Значення')
plt.title('Скрипковий графік розподілу злочинності')
plt.show()
