import tkinter as tk
import tkinter.font as tkFont
import json
from datetime import date, datetime

import os
import pandas as pd

from databaseFiller import DatabaseFiller
class App:
    def __init__(self, root):
        """ Initialize the application. """
        number_player_option=[str(i) for i in range(2,13)]
        number_map_option=["4","6","8","12","16","24","32","48"]

        df=pd.read_csv("Mario_kart8deluxe_maps_with_dlcs_map.csv")
        self.map_options=df['Circuit_Name']
        #setting title
        root.title("Game-Stats")
        #setting window size
        self.width=900
        self.height=1000
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (self.width, self.height, (screenwidth - self.width) / 2, (screenheight - self.height) / 2)
        root.geometry(alignstr)
        root.resizable(True,True)
        self.vcmd = (root.register(self.callback))

        #String var
        self.nbPlayer_clicked=tk.StringVar()
        self.nbPlayer_clicked.set(str(number_player_option[0]))
        self.nbMap_clicked=tk.StringVar()
        self.nbMap_clicked.set(number_map_option[0])

        #NB players option menu
        self.nb_Players_option_menu=tk.OptionMenu(root,self.nbPlayer_clicked,*number_player_option)
        self.nb_Players_option_menu.place(x=150,y=70,width=70,height=25)


        #NB map option menu
        self.nb_map_option_menu=tk.OptionMenu(root,self.nbMap_clicked,*number_map_option)
        self.nb_map_option_menu.place(x=30,y=70,width=70,height=25)

        #map label
        self.map_label=tk.Label(root)
        self.map_label["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.map_label["font"] = ft
        self.map_label["fg"] = "#333333"
        self.map_label["justify"] = "center"
        self.map_label["text"] = "Number of Maps"
        self.map_label.place(x=30,y=40,width=90,height=25)

        # Nb player label
        self.nb_Player_label=tk.Label(root)
        self.nb_Player_label["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.nb_Player_label["font"] = ft
        self.nb_Player_label["fg"] = "#333333"
        self.nb_Player_label["justify"] = "center"
        self.nb_Player_label["text"] = "Number of Players"
        self.nb_Player_label.place(x=150,y=40,width=110,height=25)


        #Player label
        self.player_label=tk.Label(root)
        self.player_label["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.player_label["font"] = ft
        self.player_label["fg"] = "#333333"
        self.player_label["justify"] = "center"
        self.player_label["text"] = "Player"
        self.player_label.place(x=self.width/4,y=100,width=70,height=25)

        #score label
        self.score_label=tk.Label(root)
        self.score_label["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.score_label["font"] = ft
        self.score_label["fg"] = "#333333"
        self.score_label["justify"] = "center"
        self.score_label["text"] = "Score"
        self.score_label.place(x=self.width/4+80,y=100,width=70,height=25)
        
        #validator of the number of players
        self.validator_1=tk.Button(root)
        self.validator_1["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        self.validator_1["font"] = ft
        self.validator_1["fg"] = "#000000"
        self.validator_1["justify"] = "center"
        self.validator_1["text"] = "Ok"
        self.validator_1.place(x=260,y=70,width=70,height=25)
        self.validator_1["command"] = self.validator_1_command

        #send the data button
        self.send_button=tk.Button(root)
        self.send_button["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        self.send_button["font"] = ft
        self.send_button["fg"] = "#000000"
        self.send_button["justify"] = "center"
        self.send_button["text"] = "Send"
        self.send_button.place(x=360,y=70,width=70,height=25)
        self.send_button["command"] = self.send_button_command

        #entries lists
        self.players_entries=[]
        self.score_entries=[]
        self.map_name_option_menus=[]
        self.clicked_options=[]
    def send_button_command(self):
        players_name=[]
        players_score=[]
        map_names=[]

        for i in range(len(self.clicked_options)):
            map_names.append(self.clicked_options[i].get())
        for i in range(len(self.players_entries)):
            players_name.append(self.players_entries[i].get())
            players_score.append(int(self.score_entries[i].get()))
        gss=GameStatsSystem(map_name=map_names,players=players_name,scores=players_score)
        gss.dataToJSON()
        dbf=DatabaseFiller()
        now = datetime.now()
        date = now.strftime("%d/%m/%Y %H:%M:%S")
        dbf.insert_data(map_name=map_names,players=players_name,scores=players_score,date=date)
        
    def callback(self, P)->bool:
        """ Validate the input """
        if str.isdigit(P) or P == "":
            return True
        else:
            return False
    def validator_1_command(self):
        """ command for the validator button """
        count=int(self.nbPlayer_clicked.get())
        count_map_number=int(self.nbMap_clicked.get())
        yPlacement=130
        yPlacementForMap=130
        self.widget_destroyer()
        if len(self.map_name_option_menus)!=0:
            for i in range(len(self.map_name_option_menus)): 
                self.map_name_option_menus[i].destroy()
        self.reset_lists()
        
        self.widget_creator(count)
        self.set_clicked_options(count_map_number)
    
        self.set_map_name_option_menus(count_map_number)
        self.player_and_score_placement(count, yPlacement)
        self.map_name_option_menu_placement(count_map_number, yPlacementForMap)

    def map_name_option_menu_placement(self, count_map_number, yPlacementForMap):
        """ place the map name option menu """
        for i in range(count_map_number):
            self.map_name_option_menus[i].place(x=self.width/4+160,y=yPlacementForMap,width=150,height=25)
            yPlacementForMap+=50

    def player_and_score_placement(self, count, yPlacement):
        """ place the player and score entries """
        for i in range(count):
            self.players_entries[i].place(x=self.width/4,y=yPlacement,width=70,height=25)
            self.score_entries[i].place(x=self.width/4+80,y=yPlacement,width=70,height=25)
            yPlacement+=50

    def set_map_name_option_menus(self, count_map_number):
        """ set the map name option menu """
        for i in range(count_map_number):
            map_name_option_menu=tk.OptionMenu(root,self.clicked_options[i],*self.map_options)
            self.map_name_option_menus.append(map_name_option_menu)
            map_name_option_menu.pack()

    def reset_lists(self):
        """ reset the lists """
        #reset the lists
        self.players_entries=[]
        self.score_entries=[]
        self.map_name_option_menus=[]

    def widget_destroyer(self):
        """ destroy the widgets """
        #destroy the widgets
        if len(self.players_entries)!=0:
            for i in (range(len(self.players_entries))):
                self.players_entries[i].destroy()
                self.score_entries[i].destroy()

    def widget_creator(self, count):
            """ create the widgets """
        #create or recreate the lists and the widgets
            for i in range(count):
                player_entry=tk.Entry(root)
                score_entry=tk.Entry(root,validate='all',validatecommand=(self.vcmd,'%P'))
                self.players_entries.append(player_entry)
                self.score_entries.append(score_entry)
                player_entry.pack()
                score_entry.pack()

    def set_clicked_options(self, count_map_number):
        """ set the clicked options """
        for i in range(count_map_number):
            clicked=tk.StringVar()
            clicked.set(self.map_options[0])
            self.clicked_options.append(clicked)
class GameStatsSystem:

    """ This class is used to create the game stats system """
    ID="id"
    PLAYERS="players"
    MAP_NAME="map_name"
    PODIUM="podium"
    def __init__(self,map_name,players,scores) -> None:
        """ init """
        self.map_name=map_name
        self.players=players
        self.scores=scores
        stringified_dict=json.dumps(self.assemble())
        self.data=json.loads(stringified_dict)
    def assemble(self)->dict:
        """ assemble the data in a dict """
        result={}
        for i in range(len(self.players)):
            result.update({self.players[i]:self.scores[i]})
        return result
    # function to return key for any value
    def get_key(self,val):
        """ get the key for a value """
        for key, value in self.data.items():
            if val == value:
                return key
 
        return "key doesn't exist"
    #get the key of the max value
    def get_max_key(self,p):
        """ get the key of the max value """
        max=0
        for key, value in self.data.items():
            if max <= value :
                if self.get_key(value) not in p:
                    max=value
         
        return self.get_key(max)
    def dataToJSON(self):
        """ data to json """
        #TODO bug : the whole podium is occupied by the same person
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        #temporary variable to have the podium
        p=[]
        first=self.get_max_key(p)
        p.append(first)
        second=self.get_max_key(p)
        p.append(second)
        third=self.get_max_key(p)
        p.append(third)
        print(p)
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
if __name__ == "__main__":
    """ main """
    root = tk.Tk()
    app = App(root)
    root.mainloop()
