import argparse
import json
import os
from datetime import datetime
class ArgumentException(Exception):
    def __init__(self,message) -> None:
        self.message=message
        
class GameStats:
    PLAYERS="players"
    MAP_NAME="map_name"
    def __init__(self):
        parser=argparse.ArgumentParser()
        parser.add_argument('-p','--players',help='Enter players and their positions',type=str,metavar='')
        parser.add_argument('-m','--map',help='Enter the map',type=str,metavar='')
        args=parser.parse_args()
        if args.map=='':
            raise ArgumentException("Map name required")
        if args.players=='':
            raise ArgumentException('Players and their positions needed')
        self.data=json.loads(args.players)
    
    def dataToJSON(self):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        with open('result.json','r+') as file:
            jsonList=[]
            entry={}
            entry['id']=dt_string
            entry['players']=self.data
            #empty file
            if os.path.getsize("result.json")==0:
                jsonList=[entry]
                json.dump(jsonList,file, separators=(',', ':'))
                
            else:
                jsonList=json.load(file)
                jsonList.append(entry)
                file.seek(0)
                file.truncate()
                json.dump(jsonList,file)            
                
if __name__=="__main__":
    gs=GameStats()
    gs.dataToJSON()