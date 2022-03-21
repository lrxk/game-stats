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

        GLineEdit_100=tk.Entry(root)
        GLineEdit_100["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_100["font"] = ft
        GLineEdit_100["fg"] = "#333333"
        GLineEdit_100["justify"] = "center"
        GLineEdit_100["text"] = "Nb_Players"
        GLineEdit_100.place(x=150,y=70,width=70,height=25)

        GButton_135=tk.Button(root)
        GButton_135["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_135["font"] = ft
        GButton_135["fg"] = "#000000"
        GButton_135["justify"] = "center"
        GButton_135["text"] = "Ok"
        GButton_135.place(x=260,y=70,width=70,height=25)
        GButton_135["command"] = self.GButton_135_command

    def GButton_135_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
