from importlib.metadata import entry_points
from scrapers import *
from sorters import *
from writers import *

def create_gw_data():

    print("here")
    for i in range(1,39):
        data = scr_gw_live(i)
        data = data["elements"]
        gw = pd.DataFrame()
        ids = pd.DataFrame()
        

        for j in range(len(data)):
            stats = pd.DataFrame.from_records(data[j]["stats"],index = [j])
            id = pd.DataFrame({'id':[data[j]['id']]}, index = [j])
            ids = pd.concat([ids,id],axis=0)
            gw = pd.concat([gw,stats],axis=0)
        
        dataout = pd.concat([ids,gw],axis=1)
        wr_gw_live(dataout,i)

        print('finished gameweek ' + str(i))

    print('ending')

def create_manager_data(entry_id):
    
    mngdata = scr_manager_info(entry_id)
    mngname = mngdata["player_first_name"]

    print("Creating Summary File")
    sumdata = scr_team_summary(entry_id)
    wr_team_summary(sumdata,mngname)

    print("Creating Transfer File")
    transferdata = scr_team_transfers(entry_id)
    wr_team_transfers(transferdata,mngname)

    print("Getting Picks")
    for i in range(1,39):
        pickdata = scr_team_picks(entry_id,i)
        wr_gw_picks(pickdata,i,mngname)
        print("gw " + str(i) + " created")


def main():

    ids = [931343,3882246,849616,983454,480734,712553,289748,6520504,618986,5083876,3870811,617728]
    print("starting first player")
    for i in ids:
        create_manager_data(i)
        print("next manager")
    print("ending")

if __name__ == "__main__":
    main()
    #main()


