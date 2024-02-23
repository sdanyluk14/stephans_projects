import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_html('https://fbref.com/en/comps/9/Premier-League-Stats')

# Save the actual df that we'd like
results_df = df[0]

results_df.loc[results_df['Squad'] == 'Everton', 'Pts'] += 10

print(results_df.head())
print(results_df.columns)

def create_plot(df, x_col, y_col, plot_lab, title, x_label, y_label):
    # Create a linear regression line between x_col and y_col
    m, b = np.polyfit(df[x_col], df[y_col], 1)
    # Plot the linear regression line
    plt.plot(df[x_col], m*df[x_col] + b, color='red')

    plt.scatter(df[x_col], df[y_col])
    # Iterate over each row in the DataFrame
    for index, row in df.iterrows():
        # Annotate each point with its label from the 'label' column
        plt.annotate(row[plot_lab], (row[x_col], row[y_col]), textcoords="offset points", xytext=(0,-10), ha='center', fontsize=6)

    # Set plot title and labels
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

create_plot(results_df, 'xGD', 'Pts', 'Squad', 'xGD vs Pts', 'xGD', 'Pts')