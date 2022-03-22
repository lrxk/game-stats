import tkinter as tk
import tkinter.font as tkFont

class App:
    MAX_ENTRIES=8
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        self.width=600
        self.height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (self.width, self.height, (screenwidth - self.width) / 2, (screenheight - self.height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        self.vcmd = (root.register(self.callback))

        #Nb Player entry
        self.nb_Players_Entry=tk.Entry(root,validate='all',validatecommand=(self.vcmd,'%P'))
        self.nb_Players_Entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.nb_Players_Entry["font"] = ft
        self.nb_Players_Entry["fg"] = "#333333"
        self.nb_Players_Entry["justify"] = "center"
        self.nb_Players_Entry["text"] = "Nb_Players"
        self.nb_Players_Entry.place(x=150,y=70,width=70,height=25)

        #map label
        self.map_label=tk.Label(root)
        self.map_label["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.map_label["font"] = ft
        self.map_label["fg"] = "#333333"
        self.map_label["justify"] = "center"
        self.map_label["text"] = "Map Name"
        self.map_label.place(x=self.width/4,y=30,width=70,height=25)

        # map entry
        self.map_entry=tk.Entry(root)
        self.map_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.map_entry["font"] = ft
        self.map_entry["fg"] = "#333333"
        self.map_entry["justify"] = "center"
        self.map_entry["text"] = "Map Name"
        self.map_entry.place(x=self.width/4+80,y=30,width=70,height=25)


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

    def send_button_command(self):
        #TODO

        pass


    def callback(self, P):
        if str.isdigit(P) or P == "":
            return True
        else:
            return False
    def validator_1_command(self):
        
        count=int(self.nb_Players_Entry.get())
        yPlacement=130
        if count>self.MAX_ENTRIES:
            raise Exception("Can only be "+str(self.MAX_ENTRIES)+" entries")
        if len(self.players_entries)!=0:
            for i in (range(len(self.players_entries))):
                self.players_entries[i].destroy()
                self.score_entries[i].destroy()
        self.players_entries=[]
        self.score_entries=[]
        for i in range(count):
            player_entry=tk.Entry(root)
            score_entry=tk.Entry(root,validate='all',validatecommand=(self.vcmd,'%P'))
            self.players_entries.append(player_entry)
            self.score_entries.append(score_entry)
            player_entry.pack()
            score_entry.pack()
        for i in range(count):
            self.players_entries[i].place(x=self.width/4,y=yPlacement,width=70,height=25)
            self.score_entries[i].place(x=self.width/4+80,y=yPlacement,width=70,height=25)
            yPlacement+=50
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
