import argparse
import json
import os
from datetime import datetime


class GameStatsByCupException(Exception):
    def __init__(self, message):
        self.message = message


class GameStatsByCup:
    ID="id"
    PLAYERS="players"
    MAP_NAME="map_name"
    PODIUM="podium"
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument(
            '-m', '--maps', help='Enter the maps played', type=str, metavar='')
        parser.add_argument(
            '-p', '--players', help='Enter the players and their scores', type=str, metavar='')
        parser.add_argument(
            '-c', '--cc', help='Enter the CC', type=int, metavar='')
        parser.add_argument(
            '-d', '--difficulty', help='Enter the AI difficulty', type=str, metavar='')
        args = parser.parse_args()
        if args.maps == '':
            raise GameStatsByCupException('Maps must be given')
        if args.players == '':
            raise GameStatsByCupException('players must be given')
        if args.cc == 0:
            raise GameStatsByCupException('cc must be given')
        if args.difficulty == '':
            raise GameStatsByCupException('AI difficulty must be given')
        self.maps = args.maps
        self.players = args.players
        self.cc = args.cc
        self.difficulty = args.difficulty

    def get_maps(self):
        maps = []
        temporaryRange = 0
        maps = self.maps.split(',')
        return maps
    # function to return key for any value

    def get_key(self, val, data):
        for key, value in data.items():
            if val == value:
                return key

        return "key doesn't exist"

    def dataToJson(self):
        filename = 'result-by-cup.json'
        data = json.loads(self.players)
        data = {k: v for k, v in sorted(
            data.items(), key=lambda item: item[1])}
        values = list(data.values())
        first_score = max(values)
        values.remove(first_score)
        second_score = max(values)
        values.remove(second_score)
        third_score = max(values)
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        first = self.get_key(first_score, data)
        second = self.get_key(second_score, data)
        third = self.get_key(third_score, data)
        podium = {"first": first, "second": second, "third": third}
        with open(filename, 'r+') as file:
            jsonList = []
            entry = {}
            entry[self.ID] = dt_string
            entry[self.PLAYERS] = data
            entry[self.MAP_NAME] = self.get_maps()
            entry[self.PODIUM] = podium
            # empty file
            if os.path.getsize(filename) == 0:
                jsonList = [entry]
                json.dump(jsonList, file, separators=(',', ':'))
            else:
                jsonList = json.load(file)
                jsonList.append(entry)
                file.seek(0)
                file.truncate()
                json.dump(jsonList, file)


if __name__ == "__main__":
    gsbc = GameStatsByCup()
    # gsbc.get_maps()
    gsbc.dataToJson()
