#Taken from Seabron:
# https://seaborn.pydata.org/examples/scatterplot.html

#Corr file = intelgibility 
#Nat_corr = Naturalness


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#intelligibility + objective scores file
file_path = r"C:\Users\alsaf\Desktop\Capstone-Files\Code and Data\Correlation\Nat_Corr.xlsx"
df = pd.read_excel(file_path)

# Set style
sns.set(style="whitegrid") #keeps it clean idk i took it from seaborn docs

# Define the objective metrics to compare against Intel_MOS
objective_metrics = ['PESQ','VISQOL', 'STOI', 'Vqscore', 'ScoreQ', 'NISQUA', 'Torch-Audio']

# Create scatter plots with trend lines
plt.figure(figsize=(12, 10)) #Mess with the size so you can read
for i, metric in enumerate(objective_metrics, 1):
    plt.subplot(3, 3, i)
    sns.scatterplot(data=df, x='Nat_MOS', y=metric, s=40)
    sns.regplot(data=df, x='Nat_MOS', y=metric, scatter=False, color='red', ci=None)  #For a nice layout: https://seaborn.pydata.org/tutorial/axis_grids.html
    plt.title(f'Nat_MOS vs {metric}', fontsize=9.5)
    plt.xlabel("Nat_MOS", fontsize=7)  
    plt.ylabel(metric, fontsize=7)
    plt.xticks(fontsize=9) #Mess with size
    plt.yticks(fontsize=9) #size

plt.tight_layout() 
plt.show()
