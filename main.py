from scrapers import *
from sorters import *
from writers import *

print("getting Data")
data = scr_gw_live(38)

print("Making player data")

data1 = data["elements"]

print(data1[0]['id'])

