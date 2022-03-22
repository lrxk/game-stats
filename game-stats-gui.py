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
        vcmd = (root.register(self.callback))
        self.nb_Players_Entry=tk.Entry(root,validate='all',validatecommand=(vcmd,'%P'))
        self.nb_Players_Entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.nb_Players_Entry["font"] = ft
        self.nb_Players_Entry["fg"] = "#333333"
        self.nb_Players_Entry["justify"] = "center"
        self.nb_Players_Entry["text"] = "Nb_Players"
        self.nb_Players_Entry.place(x=150,y=70,width=70,height=25)

        self.validator_1=tk.Button(root)
        self.validator_1["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        self.validator_1["font"] = ft
        self.validator_1["fg"] = "#000000"
        self.validator_1["justify"] = "center"
        self.validator_1["text"] = "Ok"
        self.validator_1.place(x=260,y=70,width=70,height=25)
        self.validator_1["command"] = self.validator_1_command
        self.players_entries=[]
        self.score_entries=[]
        
    def callback(self, P):
        if str.isdigit(P) or P == "":
            return True
        else:
            return False
    def reset(self):
        for i in range(len(self.players_entries)):
            self.players_entries[i].destroy()
            self.score_entries[i].destroy()


    def validator_1_command(self):
        self.reset()
        count=int(self.nb_Players_Entry.get())
        yPlacement=110
        if count>self.MAX_ENTRIES:
            raise Exception("Can only be "+str(self.MAX_ENTRIES)+" entries")
        for i in range(count):
            self.players_entries.append(tk.Entry(root))
            self.score_entries.append(tk.Entry(root))
        for i in range(count):
            self.players_entries[i].place(x=self.width/4,y=yPlacement,width=70,height=25)
            self.score_entries[i].place(x=self.width/4+80,y=yPlacement,width=70,height=25)
            yPlacement+=50
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
