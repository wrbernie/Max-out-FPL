"""These functions will take in text files and creat csv files on a local folder"""

from scrapers import *
import csv
import os
import pandas as pd




def wr_team_summary(data,basefolder):
    gw_history_df = pd.DataFrame.from_records(data["current"])
    gw_history_df.to_csv(os.path.join(basefolder, 'history.csv'), index=False)

def wr_player_summary(data,basefolder):
    player_summary_df = pd.DataFrame.from_records(data["history"])
    player_summary_df.to_csv(os.path.join(basefolder, 'salah.csv'), index=False)


def main():
    print('starting')
    data = scr_player_summary(233)
    
    folder_name = "Players"
    
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print("here")

    wr_player_summary(data,folder_name)

    print("ending")


if __name__ == "__main__":
    main()