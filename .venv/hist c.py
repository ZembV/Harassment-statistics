import pandas as pd
import matplotlib.pyplot as plt

file_path = r'C:\Users\examp\OneDrive\Робочий стіл\data_cts_violent_and_sexual_crime.xlsx'
df = pd.read_excel(file_path)
filtered_df = df[df['Unit of measurement'].str.strip().str.lower() == 'counts']
plt.figure(figsize=(10, 6))
plt.hist(filtered_df['VALUE'], bins=20, color='#b3bcff', edgecolor='black', density=True)
plt.xlabel('Кількість')
plt.ylabel('Частота')
plt.title('Графік густини кількості сексуального насилля')
plt.grid(True)
filtered_df['VALUE'].plot.density(ax=plt.gca(), grid=True, color='red')

plt.show()
