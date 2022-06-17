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
            #c = pd.concat([id,stats],axis = 1)
            id = pd.DataFrame({'id':[data[j]['id']]}, index = [j])
            ids = pd.concat([ids,id],axis=0)
            gw = pd.concat([gw,stats],axis=0)
        
        dataout = pd.concat([ids,gw],axis=1)
        wr_gw_live(dataout,i)

        print('finished gameweek ' + str(i))

    print('ending')



def main():

    data = scr_gw_live(1)
    data = data["elements"]

    r = len(data)
    
    for j in range(r):
        id = pd.DataFrame.from_dict(data[j]["id"])
        print(id)


if __name__ == "__main__":
    create_gw_data()
    #main()


