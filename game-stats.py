import argparse
import json
import os
from datetime import datetime
class ArgumentException(Exception):
    def __init__(self,message) -> None:
        self.message=message
        
class GameStats:
    ID="id"
    PLAYERS="players"
    MAP_NAME="map_name"
    PODIUM="podium"
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
        self.map_name=args.map
    
    # function to return key for any value
    def get_key(self,val):
        for key, value in self.data.items():
            if val == value:
                return key
 
        return "key doesn't exist"
    def dataToJSON(self):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        first=self.get_key(1)
        second=self.get_key(2)
        third=self.get_key(3)
        podium={"first":first,"second":second,"third":third}
        with open('result.json','r+') as file:
            jsonList=[]
            entry={}
            entry[self.ID]=dt_string
            entry[self.PLAYERS]=self.data
            entry[self.MAP_NAME]=self.map_name
            entry[self.PODIUM]=podium
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