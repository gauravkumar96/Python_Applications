import tkinter as tk


class TICTACTOE(tk.Tk):
    def __init__(self):  # A constructor as you may know
        super().__init__()
        self.title("Tic Tac Toe")
        self.btn = []
        self.turn = True
        self.count = 0
        self.resizable(width=False, height=False)
        self.Board()

    def Board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append(tk.Button(self, width=10, height=3, font="Calibre 35 bold",
                                     command=lambda x=i, y=j:self.Turn_Taken(x,y)))
                row[j].grid(row=i, column=j)
            self.btn.append(row)
        tk.Button(self, text="New Game", width=10, height=1, font="Calibre 15 bold", bg='black', fg='white',
                  activebackground='blue3',
                  activeforeground='white',
                  command=self.NEWGAME).grid(row=3, column=1
                  )

    def Turn_Taken(self,x,y):
        self.count += 1
        if self.turn:
            char = 'X'
            self.btn[x][y].config(text="X",bg='black',state='disabled')
        else:
            char = 'O'
            self.btn[x][y].config(text="O", bg='white', state='disabled')
        self.CheckResult(char)
        self.turn = not self.turn

    def NEWGAME(self):
        for widget in self.winfo_children():
            widget.destroy()

        self.btn = []
        self.turn = True
        self.count = 0
        self.Board()

    def CheckResult(self,char):
        if(((self.btn[0][0]['text'] == char) and(self.btn[0][1]['text'] == char)and(self.btn[0][2]['text'] == char))or
        ((self.btn[1][0]['text'] == char) and(self.btn[1][1]['text'] == char)and(self.btn[1][2]['text'] == char))or
        ((self.btn[2][0]['text'] == char) and(self.btn[2][1]['text'] == char)and(self.btn[2][2]['text'] == char))or
        ((self.btn[0][0]['text'] == char) and(self.btn[1][0]['text'] == char)and(self.btn[2][0]['text'] == char))or
        ((self.btn[0][1]['text'] == char) and(self.btn[1][1]['text'] == char)and(self.btn[2][1]['text'] == char))or
        ((self.btn[0][2]['text'] == char) and(self.btn[1][2]['text'] == char)and(self.btn[2][2]['text'] == char))or
        ((self.btn[0][0]['text'] == char) and(self.btn[1][1]['text'] == char)and(self.btn[2][2]['text'] == char))or
        ((self.btn[0][2]['text'] == char) and(self.btn[1][1]['text'] == char)and(self.btn[2][0]['text'] == char))):
            self.Result(char)
        elif self.count == 9:
            self.Result("Draw")

    def Result(self,char):
        top = tk.Toplevel(self)
        if char == "Draw":
            top.title("OOPS!!!")
            topText = tk.Label(top, text="It is a Draw", font='Calibre 30 bold', fg='blue')
        else:
            top.title("Congrats")
            topText = tk.Label(top, text=f"It is a Win by {char}", font='Calibre 30 bold', fg='blue')
        topButton = tk.Button(top, text="New Game", bg='black', fg='white', activebackground='blue3', activeforeground='white',command=self.NEWGAME)
        topText.grid(row=0, column=0, padx=10, pady=10)
        topButton.grid(row=1, column=0)

TICTACTOE().mainloop()
