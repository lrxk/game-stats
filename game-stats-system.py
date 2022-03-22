import json
from datetime import datetime
import os
class GameStatsSystem:
    ID="id"
    PLAYERS="players"
    MAP_NAME="map_name"
    PODIUM="podium"
    def __init__(self,map_name,players,scores) -> None:
        self.map_name=map_name
        self.players=players
        self.scores=scores
        stringified_dict=json.dumps(self.assemble())
        self.data=json.loads(stringified_dict)
    def assemble(self)->dict:
        result={}
        for i in range(len(self.players)):
            result.update({self.players[i]:self.scores[i]})
        return result
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
