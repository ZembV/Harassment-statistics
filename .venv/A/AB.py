import pandas as pd
from scipy import stats

df = pd.read_excel(r'C:\Users\examp\OneDrive\Робочий стіл\data_cts_violent_and_sexual_crime.xlsx')
df = df[(df['Dimension'] == 'by relationship to perpetrator') & (df['Unit of measurement'] == 'Counts')]

group_A = df[df['Category'].isin(['Intimate partner or family member', 'Other Perpetrator known to the victim'])]
group_B = df[df['Category'] == 'Perpetrator unknown to the victim']
t_stat, p_value = stats.ttest_ind(group_A['VALUE'], group_B['VALUE'])
print(f'T-statistic: {t_stat}')
print(f'P-value: {p_value}')

