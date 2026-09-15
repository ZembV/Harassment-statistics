import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

df = pd.read_excel(r'C:\Users\examp\OneDrive\Робочий стіл\data_cts_violent_and_sexual_crime.xlsx')
filtered_df = df[df['Unit of measurement'].str.strip().str.lower() == 'counts']

fig, ax = plt.subplots(figsize=(10, 6))
hb = ax.hexbin(x=filtered_df['Year'], y=filtered_df['VALUE'], gridsize=30, mincnt=1, cmap='plasma', edgecolors='none', norm=LogNorm())
plt.xlabel('Year')
plt.ylabel('VALUE')
plt.title('Hexbin Scatterplot')
cb = fig.colorbar(hb, ax=ax)
cb.set_label('counts')
bins = [0, 10, 20, 50, 100, 200, 500, 1000]
cb.set_ticks(bins)
cb.set_ticklabels([str(val) for val in bins])
plt.show()
