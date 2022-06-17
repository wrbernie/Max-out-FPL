"""These functions will take in text files and creat csv files on a local folder"""

from sys import builtin_module_names
from scrapers import *
import csv
import os
import pandas as pd




def wr_team_summary(data):
    """
    Creates a csv file with a team's gameweek history.
    """
    gw_history_df = pd.DataFrame.from_records(data["current"])
    gw_history_df.to_csv(os.path.join(os.getcwd(), 'data/managers/willie/22/gw_history.csv'), index=False)

def wr_team_transfers(data):
    """
    Creates a csv file with a team's transfer history
    """
    team_transfers_df = pd.DataFrame.from_records(data)
    team_transfers_df.to_csv(os.path.join(os.getcwd(), 'data/managers/willie/22/transfer_history.csv'))

def wr_player_summary(data,basefolder):
    """
    Creates a csv file with gw-by-gw data for a specific player.
    """
    player_summary_df = pd.DataFrame.from_records(data["history"])
    player_summary_df.to_csv(os.path.join(basefolder, 'salah.csv'), index=False)

def wr_gw_picks(data,gw):
    """
    Creates a csv file with team data of a specific gameweek.
    """
    basefolder = os.getcwd() + "/data/managers/willie/22/gameweeks/"
    team_gw_df = pd.DataFrame.from_records(data["picks"])
    team_gw_df.to_csv(os.path.join(basefolder, str(gw) + '.csv'), index=False)

def wr_gw_live(data,gw):
    """creates a csv for a specific gameweek
    """
    basefolder = os.getcwd() + '/data/seasons/22/gameweeks/'
    gw_data_df = pd.DataFrame.from_records(data)
    gw_data_df.to_csv(os.path.join(basefolder, 'gw' + str(gw) + '.csv'), index = False)

def wr_player_data(data):
    """ Puts player data into a csv file
    """
    fulldata_df = pd.DataFrame.from_records(data["elements"])
    fulldata_df.to_csv(os.path.join(os.getcwd(), 'data/seasons/22/playerdata.csv'))




def main():
    print('starting')

    data = scr_gw_live(1)

    print(data["elements"][232])


if __name__ == "__main__":
    main()