import argparse
import json
from turtle import TPen

from click import argument
class ArgumentException(Exception):
    def __init__(self,message) -> None:
        self.message=message
        
class GameStats:
    PLAYERS="players"
    MAP_NAME="map_name"
    def __init__(self) -> None:
        args=self.argument()
        if args.map=='':
            
        pass
    def argument(self):
        parser=argparse.ArgumentParser()
        parser.add_argument('-p','--players',help='Enter players and their positions',type=str,metavar='')
        parser.add_argument('-m','--map',help='Enter the map',type=str,metavar='')
        args=parser.parse_args()
        return args