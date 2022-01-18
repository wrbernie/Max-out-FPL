"""These functions will retrieve data from FPL website and return a text file"""

import requests
import json
import time

def scr_team_summary(entry_id):
    """ Retrieve the summary/history data for a specific entry/team
    Args:
        entry_id (int) : ID of the team whose data is to be retrieved
    """
    base_url = "https://fantasy.premierleague.com/api/entry/"
    full_url = base_url + str(entry_id) + "/history/"
    response = ''
    while response == '':
        try:
            response = requests.get(full_url)
        except:
            time.sleep(5)
    if response.status_code != 200:
        raise Exception("Response was code " + str(response.status_code))
    data = json.loads(response.text)
    return data

def scr_player_summary(PID):
    """This function scrapes for gw data for an individual player
    
    Args:
        PID (int): ID for the player who will be reteieved.
        Returns: Text file of data for a specific player.
    """
    base_URL = "https://fantasy.premierleague.com/api/element-summary/"
    full_URL = base_URL + str(PID) + "/"
    response = ''
    while response == '':
        try:
            response = requests.get(full_URL)
        except:
            time.sleep(5)
    if response.status_code != 200:
        raise Exception("Response was code " + str(response.status_code))
    data = json.loads(response.text)
    return(data)


def scr_team_gw(teamID,gw):
    """This function scrapes for gw specific data for a specific team.
    
    Args:
        teamID (int): ID for specific team to be colected.
        gw (int): The desired gameweek
    """
    base_URL = "https://fantasy.premierleague.com/api/entry/"
    full_URL = base_URL + str(teamID) + "/event/" + str(gw) + "/picks/"

    response = ''
    while response == '':
        try:
            response = requests.get(full_URL)
        except:
            time.sleep(5)
    if response.status_code != 200:
        raise Exception("Response was code " + str(response.status_code))
    data = json.loads(response.text)
    return(data)

def scr_gw_live(gw):
    """This function scrapes for all player data in a specific gameweek.

    Args:        
        gw(int): The gameweek that will be scraped.
        returns: Text file with gameweek data.
    """
    base_URL = "https://fantasy.premierleague.com/api/event/"
    full_URL = base_URL + str(gw) + "/live/"

    response = ''
    while response == '':
        try:
            response = requests.get(full_URL)
        except:
            time.sleep(5)
    if response.status_code != 200:
        raise Exception("Response was code " + str(response.status_code))
    data = json.loads(response.text)
    return(data)

def main():
    ID = 233
    gw = 1
    print(scr_team_gw(ID,gw)["picks"])
    

if __name__ == "__main__":
    main()
