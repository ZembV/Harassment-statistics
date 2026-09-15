import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path = r'C:\Users\examp\OneDrive\Робочий стіл\data_cts_violent_and_sexual_crime.xlsx'
df = pd.read_excel(file_path)
filtered_df = df[df['Unit of measurement'].str.strip().str.lower() == 'rate per 100,000 population']

fig, ax = plt.subplots(figsize=(8, 6))
box_data = filtered_df['VALUE'].values

q1, q2, q3 = np.percentile(box_data, [25, 50, 75])
box = ax.boxplot(box_data, vert=True, showfliers=True, patch_artist=True)
for patch in box['boxes']:
    patch.set_facecolor('#bcffb3')
ax.plot([1, 1], [q1, q3], color='k', linewidth=2, label='Процентилі')
ax.scatter(1, q2, color='k', marker='o', s=100)
ax.legend()
plt.show()
