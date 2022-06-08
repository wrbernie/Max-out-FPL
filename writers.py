"""These functions will take in text files and creat csv files on a local folder"""

from scrapers import *
import csv
import os
import pandas as pd




def wr_team_summary(data):
    """
    Creates a csv file with a team's gameweek history.
    """
    gw_history_df = pd.DataFrame.from_records(data["current"])
    gw_history_df.to_csv(os.path.join(getcwd, 'history.csv'), index=False)

def wr_player_summary(data,basefolder):
    """
    Creates a csv file with gw-by-gw data for a specific player.
    """
    player_summary_df = pd.DataFrame.from_records(data["history"])
    player_summary_df.to_csv(os.path.join(basefolder, 'salah.csv'), index=False)

def wr_team_gw(data,basefolder,gw):
    """
    Creates a csv file with team data of a specific gameweek.
    """
    team_gw_df = pd.DataFrame.from_records(data["picks"])
    team_gw_df.to_csv(os.path.join(basefolder, str(gw) + '.csv'), index=False)

def wr_gw_data(data,basefolder,gw):
    """creates a csv for a specific gameweek
    """
    gw_data_df = pd.DataFrame.from_records(data["elements"])
    gw_data_df.to_csv(os.path.join(basefolder, 'gw' + str(gw) + '.csv'), index = False)



def main():
    print('starting')
    data = scr_gw_live(1)
    
    folder_name = "gameweeks"
    
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print("here")

    wr_gw_data(data,folder_name,1)

    print("ending")


if __name__ == "__main__":
    main()