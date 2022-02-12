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

    