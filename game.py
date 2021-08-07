"""
Set task: Create a Rock-Paper-Scissors game with a graphical user interface.
Method: 
* The GUI has three buttons, one for Rock, Paper and Scissors each.
* Triggering one of them initiates a new game.
* A random value is created for the PC and compared to the selected button.
* Two additional buttons allow the user to reset the game and play again, or quit.
"""

import tkinter as tk
from random import randrange

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.RPS = RockPaperScissors()
        self.pack(padx=250,pady=10)
        self.create_widgets()

    def create_widgets(self):
        self.frameHeadline = tk.Frame()
        self.frameVersus = tk.Frame()
        self.frameResult = tk.Frame()
        self.frameButtons = tk.Frame()
        self.frameReset = tk.Frame()
        
        self.labelTitle = tk.Label(master=self.frameHeadline,text="Rock Paper Scissor",font="Verdana 32 bold")
        self.labelTitle.pack()
        self.frameHeadline.pack()

        self.player1label = tk.Label(master=self.frameVersus,textvariable=self.RPS.varPlayer1,font="Verdana 16")
        self.player2label = tk.Label(master=self.frameVersus,textvariable=self.RPS.varPlayer2,font="Verdana 16")
        self.vs = tk.Label(master=self.frameVersus,text="vs.",font="Verdana 16")
        self.player1label.pack(side="left")
        self.vs.pack(side="left")
        self.player2label.pack(side="right")
        self.frameVersus.pack()

        self.result = tk.Label(master=self.frameResult,textvariable=self.RPS.varRes,bg="white",font="Verdana 20",width=20,height=1)
        self.result.pack()
        self.frameResult.pack()

        self.rockbutton = tk.Button(master=self.frameButtons,text="\n\n  _ _ _ _\n _| | | | |\n|_        |\n  |   R   |\n  |       |",font="Courier",command=lambda: self.pressButton(0))
        self.paperbutton = tk.Button(master=self.frameButtons,text="  _ _ _ _\n  | | | | |\n  | | | | |\n _| | | | |\n|_        |\n  |   P   |\n  |       |",font="Courier",command=lambda: self.pressButton(1))
        self.scissorsbutton = tk.Button(master=self.frameButtons,text="__    __\n\ \  / /\n   \ \/ /_ _\n   _| | | | |\n  |_        |\n    |   S   |\n    |       |",font="Courier",command=lambda: self.pressButton(2))
        self.rockbutton.pack(side="left")
        self.paperbutton.pack(side="left")
        self.scissorsbutton.pack(side="left")
        self.frameButtons.pack()

        self.reset = tk.Button(master=self.frameReset,text="Reset",font="Verdana 10",fg="red",command=self.reset)
        self.reset.pack(side="left")
        self.close = tk.Button(master=self.frameReset,text="Quit",font="Verdana 10",fg="red",command=self.master.destroy)
        self.close.pack(side="right")
        self.padding = tk.Label(master=self.frameReset,height=5)
        self.padding.pack(side="bottom")
        self.frameReset.pack()


    def pressButton(self,button):
        self.RPS.game(button)
        self.rockbutton["state"] = "disabled"
        self.paperbutton["state"] = "disabled"
        self.scissorsbutton["state"] = "disabled"
        return

    def reset(self):
        self.RPS.reset()
        self.rockbutton["state"] = "normal"
        self.paperbutton["state"] = "normal"
        self.scissorsbutton["state"] = "normal"

class RockPaperScissors:
    def __init__(self):
        self.hands = ["Rock", "Paper", "Scissors"]
        self.varPlayer1 = tk.StringVar()
        self.varPlayer2 = tk.StringVar()
        self.varPlayer1.set("Player")
        self.varPlayer2.set("Computer")
        self.varRes = tk.StringVar()
        # self.varRes.set("")

    def game(self,guess):
        #guess = input("Please enter '0' for 'Rock', '1' for 'Paper' or '2' for 'Scissors'.")
        pc = randrange(3)
        # if guess.lower() not in ["0","1","2"]:
        #     print("Aborted, please enter a valid number.")
        #     return
        # guess = int(guess)
        # print(f"Your selection: {self.hands[guess]}\nPC selection: {self.hands[pc]}")
        self.varPlayer1.set(self.hands[guess])
        self.varPlayer2.set(self.hands[pc])
        if guess == pc:
            # print("Draw.")
            self.varRes.set("Draw.")
        elif guess == (pc + 1) % 3:
            # print("Player victory.")
            self.varRes.set("You win!")
        else:
            # print("PC victory.")
            self.varRes.set("You lose!")        
        return
    
    def reset(self):
        self.varPlayer1.set("Player")
        self.varPlayer2.set("Computer")
        self.varRes.set("")



root = tk.Tk()
app = Application(master=root)
app.mainloop()

# RPS = RockPaperScissors()

# while True:
#     RPS.game()