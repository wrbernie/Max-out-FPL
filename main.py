from scrapers import *
from sorters import *
from writers import *

print("getting Data")
data = scr_data()

print("Making player data")
wr_player_data(data)

print("IDing Players")
ID_Players()