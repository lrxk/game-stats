import argparse
import json
class GameStatsByCupException(Exception):
    def __init__(self,message):
        self.message=message
class GameStatsByCup:
    def __init__(self):
        parser=argparse.ArgumentParser()
        parser.add_argument('-m','--maps',help='Enter the maps played',type=str,metavar='')
        parser.add_argument('-p','--players',help='Enter the players and their scores',type=str,metavar='')
        parser.add_argument('-c','--cc',help='Enter the CC',type=int,metavar=0)
        parser.add_argument('-d','--difficulty',help='Enter the AI difficulty',type=str,metavar='')
        args=parser.parse_args()
        if args.maps=='':
            raise GameStatsByCupException('Maps must be given')
        if args.players=='':
            raise GameStatsByCupException('players must be given')
        if args.cc==0:
            raise GameStatsByCupException('cc must be given')
        if args.difficulty=='':
            raise GameStatsByCupException('AI difficulty must be given')
        self.maps=args.maps
        self.players=args.players
        self.cc=args.cc
        self.difficulty=args.difficulty
    def dataToJson(self):
        filename='result-by-cup.json'
        data=json.loads(self.players)
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        first=self.get_key(1)
        second=self.get_key(2)
        third=self.get_key(3)
        podium={"first":first,"second":second,"third":third}
        with open(filename,'r+') as file:
            jsonList=[]
            entry={}
            entry[self.ID]=dt_string
            entry[self.PLAYERS]=self.data
            entry[self.MAP_NAME]=self.map_name
            entry[self.PODIUM]=podium
            #empty file
            if os.path.getsize(filename)==0:
                jsonList=[entry]
                json.dump(jsonList,file, separators=(',', ':'))
                
            else:
                jsonList=json.load(file)
                jsonList.append(entry)
                file.seek(0)
                file.truncate()
                json.dump(jsonList,file)     
        pass
    