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


def main():
    ID = 233
    print(scr_player_summary(ID)["history"])
    

if __name__ == "__main__":
    main()
