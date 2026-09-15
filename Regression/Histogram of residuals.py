import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder

df = pd.read_excel(r'C:\Users\examp\OneDrive\Робочий стіл\data_cts_violent_and_sexual_crime.xlsx')
filtered_df = df[df['Unit of measurement'].str.strip().str.lower() == 'rate per 100,000 population']
house = filtered_df[['VALUE', 'Country', 'Indicator', 'Dimension', 'Category', 'Sex', 'Year']]

categorical_vars = house[['Country', 'Indicator', 'Dimension', 'Category', 'Sex']]
numerical_vars = house[['VALUE']]

enc = OneHotEncoder(handle_unknown='ignore')
X = enc.fit_transform(categorical_vars)
y = numerical_vars.values.ravel()

model = LinearRegression().fit(X, y)
residuals = y - model.predict(X)

fig, ax = plt.subplots(figsize=(8, 6))
ax.hist(residuals, bins=20)
ax.set_xlabel('Залишки')
ax.set_ylabel('Частота')
ax.set_title('Гістограма залишків')
plt.tight_layout()
plt.show()