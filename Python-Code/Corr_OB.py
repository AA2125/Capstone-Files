#I took it from here: https://www.datacamp.com/tutorial/seaborn-heatmaps
#Changing the path and title for nat and intel

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Load the Excel file 
file_path = r"C:\Users\alsaf\Desktop\Nat_Corr.xlsx"
df = pd.read_excel(file_path)

#Drop non-numeric columns (https://stackoverflow.com/questions/58781581/drop-rows-with-non-numeric-entries-in-a-column-python)
df_numeric = df.select_dtypes(include='number')

# Pearson correlation matrix 
pearson_corr = df_numeric.corr(method='pearson') # pandas magic stuff idk

#Spearman correlation matrix 
spearman_corr = df_numeric.corr(method='spearman')

# Plot heatmaps (Pearson and Spearman)
plt.figure(figsize=(10, 6))
sns.heatmap(pearson_corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Nat-Pearson Correlation Heatmap") #Taken from seabron for heatmap shape
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
sns.heatmap(spearman_corr, annot=True, cmap="viridis", fmt=".2f")
plt.title("Nat-Spearman Correlation Heatmap")
plt.tight_layout()
plt.show()