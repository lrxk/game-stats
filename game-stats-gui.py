import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        nb_Players_Entry=tk.Entry(root)
        nb_Players_Entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        nb_Players_Entry["font"] = ft
        nb_Players_Entry["fg"] = "#333333"
        nb_Players_Entry["justify"] = "center"
        nb_Players_Entry["text"] = "Nb_Players"
        nb_Players_Entry.place(x=150,y=70,width=70,height=25)

        validator_1=tk.Button(root)
        validator_1["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        validator_1["font"] = ft
        validator_1["fg"] = "#000000"
        validator_1["justify"] = "center"
        validator_1["text"] = "Ok"
        validator_1.place(x=260,y=70,width=70,height=25)
        validator_1["command"] = self.validator_1_command

    def validator_1_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
