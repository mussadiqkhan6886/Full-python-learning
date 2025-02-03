import json
import sys
import requests

# If command line is not equal to 2 than exit
if sys.argv != 2:
    sys.exit()
    
# get() given url + given name and store in respond variable 
respond = requests.get("https://itunes.apple.com/search?entity=songs&limit=25&term=" + sys.argv[1])

o = respond.json() # it get all enitites of it 

for result in o["results"]: # for every result in o variable ["result"] 
    print(result["trackName"]) # print trackName in given result 
    