import pandas as pd
import plotly.express as px

df = pd.read_excel(r'C:\Users\examp\OneDrive\Робочий стіл\data_cts_violent_and_sexual_crime.xlsx')
filtered_df = df[df['Unit of measurement'].str.strip().str.lower() == 'rate per 100,000 population']
house = filtered_df[['VALUE', 'Country', 'Indicator', 'Dimension', 'Category', 'Sex', 'Year']]
predictors = ['Country', 'Indicator', 'Dimension', 'Category', 'Sex']
outcome = 'VALUE'

fig = px.scatter(house, x='Country', y='VALUE', color='Indicator', size='VALUE', hover_data=['Dimension', 'Category', 'Sex', 'Year'],
                 size_max=60, title='Bubble Chart of Violent and Sexual Crimes')

fig.update_layout(xaxis_title='Country', yaxis_title='Rate per 100,000 population', legend_title='Indicator')

fig.show()