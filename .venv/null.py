import pandas as pd

df = pd.read_excel(r'C:\Users\examp\OneDrive\Робочий стіл\data_cts_violent_and_sexual_crime.xlsx')

missing_values = df.isnull().sum()
print("Кількість пропущених значень у кожному стовпці:")
print(missing_values)