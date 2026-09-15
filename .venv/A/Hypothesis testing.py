import pandas as pd
from scipy.stats import ttest_ind

df = pd.read_excel(r'C:\Users\examp\OneDrive\Робочий стіл\data_cts_violent_and_sexual_crime.xlsx')
df = df[(df['Dimension'] == 'by relationship to perpetrator') & (df['Unit of measurement'] == 'Rate per 100,000 population')]

group_A = df[df['Category'].isin(['Intimate partner or family member', 'Other Perpetrator known to the victim'])]
group_B = df[df['Category'] == 'Perpetrator unknown to the victim']

group_A_values = group_A['VALUE'].values
group_B_values = group_B['VALUE'].values

ttest_result = ttest_ind(group_A_values, group_B_values, alternative='greater')
p_value = ttest_result.pvalue

if p_value < 0.05:
    print("Нульова гіпотеза відхиляється. Група А більша або дорівнює групі Б.")
else:
    print("Нульова гіпотеза приймається. Група А менша за групу Б.")

print(f"p-value: {p_value}")