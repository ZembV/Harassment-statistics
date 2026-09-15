import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel(r'C:\Users\examp\OneDrive\Робочий стіл\data_cts_violent_and_sexual_crime.xlsx')
filtered_df = df[df['Unit of measurement'].str.strip().str.lower() == 'counts']
data = filtered_df['VALUE']
plt.hist(data, bins=20, color='#b3bcff', edgecolor='black')
plt.xlabel('VALUE')
plt.ylabel('Frequency')
plt.title('Гістограма сексуальних домагань')
plt.show()
