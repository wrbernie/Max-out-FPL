import csv
import math
import os
from scrapers import *


def extract_stat_names(dict_of_stats):
    """ Extracts all the names of the statistics

    Args:
        dict_of_stats (dict): Dictionary containing key-value pair of stats
    """
    stat_names = []
    for key, val in dict_of_stats.items():
        stat_names += [key]
    return stat_names

def sort_players(data):
    """Creates a file with sorted data for all the players in the game.
    
    Args: Raw player data
    """
    statnm = extract_stat_names(data[0])
    fnm = os.getcwd() + '/data/seasons/22/player_data_raw.csv'
    os.makedirs(os.path.dirname(fnm), exist_ok=True)
    f = open(fnm, 'w+', encoding='utf-8',newline='')
    w = csv.DictWriter(f, sorted(statnm))
    w.writeheader()
    for player in data:
        w.writerow({k:str(v).encode('utf-8').decode('utf-8') for k, v in player.items()})



def ID_Players():
    """Creates a file that lists Last Name, First Name, and ID within FPL
    
    Args: The Raw data file that includes all data for the whole game"""

    headers = ['first_name', 'second_name', 'id']
    fin = open(os.getcwd() + '/Data/Seasons/22/playerdata.csv', 'r+', encoding='utf-8')
    outname = os.getcwd() + '/data/seasons/22/player_ids.csv'
    
    fout = open(outname, 'w+', encoding='utf-8', newline='')
    reader = csv.DictReader(fin)
    writer = csv.DictWriter(fout, headers, extrasaction='ignore')
    writer.writeheader()
    for line in reader:
        writer.writerow(line)

def sort_livedata(data):
    """reads in live data for a current week and creates a file for every player in the game
    """

def main():
    
    ID_Players()
    

if __name__ == "__main__":
    main()