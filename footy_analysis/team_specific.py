import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


class TeamClass:
    """Creates an individual team object, from which we can perform analysis"""

    def __init__(self, param1):
        team_sheets = pd.read_csv('footy_analysis/premier_league_fbpages.csv')
        print(team_sheets.head(5))

        self.df = pd.DataFrame()

        # Append all column not equal to 'team' to the df
        for col in team_sheets.columns[team_sheets.columns != 'team']:
            temp_df = pd.read_html(team_sheets.loc[team_sheets['team'] == param1][col].values[0])
            temp_df = temp_df[1]
            temp_df['season'] = col
            self.df = pd.concat([self.df, temp_df])
        
        self.team = param1
    
    def clean(self):
        self.df = self.df.loc[self.df['Comp'] == 'Premier League']
        self.df['Round'] = self.df['Round'].str.extract('(\d+)')
        self.df['Round'] = self.df['season'] + ': ' + self.df['Round'].astype(str)

        # Round values should be ordered chronologicaly
        self.df['Round'] = pd.Categorical(self.df['Round'], categories=self.df['Round'].unique(), ordered=True)

        return self.df
    
    def rolling_average(self, col, window):
        self.df[col + '_rolling'] = self.df[col].rolling(window=window).mean()
        return self.df
    
    def plot_rolling_averages(self, cols, seasons, colors=['green', 'red']):
        """Plots a rolling average for a given column and a list of seasons"""
        # Create a temp dataframe of only the seasons we want to plot, and only where cols are not null
        temp_df = self.df.loc[self.df['season'].isin(seasons) & self.df[cols[0]].notnull()]

        print(temp_df.head(5))
        # Plot the rolling average
        plt.figure(figsize=(14, 10))
        for col in range(len(cols)):
            plt.plot(temp_df['Round'], temp_df[cols[col] + '_rolling'], color=colors[col])
        
        # Fill in area between the two lines with green when col 0 is greater than col 1
        plt.fill_between(temp_df['Round'], temp_df[cols[0] + '_rolling'], temp_df[cols[1] + '_rolling'], 
                         where=temp_df[cols[0] + '_rolling'] > temp_df[cols[1] + '_rolling'], facecolor='lightgreen', interpolate=True)
        # Fill in area between the two lines with red when col 1 is greater than col 0
        plt.fill_between(temp_df['Round'], temp_df[cols[0] + '_rolling'], temp_df[cols[1] + '_rolling'], 
                         where=temp_df[cols[0] + '_rolling'] < temp_df[cols[1] + '_rolling'], facecolor='lightcoral', interpolate=True)
        plt.title(self.team + ' ' + cols[0] + ' vs ' + cols[1] + ' rolling average')
        plt.xticks(rotation=90)
        plt.show()
        
def main():
    """Main function for demonstrating the use of MyClass."""
    # Example usage:
    instance = TeamClass('Liverpool')

    instance.clean()

    # Calculate rolling averages
    instance.rolling_average('xG', 10)
    instance.rolling_average('xGA', 10)
    instance.rolling_average('GF', 10)

    instance.plot_rolling_averages(['GF', 'xG'], ['21-22', '22-23', '23-24'], ['darkgreen', 'lightgreen'])


if __name__ == "__main__":
    main()
