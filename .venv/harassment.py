import pandas as pd

df = pd.read_excel(r'C:\Users\examp\OneDrive\Робочий стіл\data_cts_violent_and_sexual_crime.xlsx')
pd.set_option('display.max_columns', None)
print(df.info())
