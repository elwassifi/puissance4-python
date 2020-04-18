import tkinter as tk
from player import Player
from game import Game
import constante as cst

class Board(tk.Frame):

    def __init__(self, parent, controller, player):
        tk.Frame.__init__(self,parent)

        # parent attributes
        self.controller = controller
        self.parent = parent

        # Board attributes
        self.grille = []
        self.labels = []
        self.rows = []
        self.buttons = []
        self.gameover = False

        # Players attributes
        self.human = player

        if player.symbol == cst.SYMBOL_X :
            sym = 0
        else :
            sym = 1

        self.ai = Player("IA", sym, True)

        # Game attributes
        self.game = Game()

        # Init Board attributes (grille[8][9], labels[6][7])
        for row in range(cst.NB_ROW + 2) :
            self.grille.append(list((cst.NB_COL + 2)*[-1]))

        for row in range(cst.NB_ROW):
            self.labels.append(list((cst.NB_COL)*[-1]))
            self.rows.append(cst.NB_ROW-1)
            self.buttons.append(row)
        self.buttons.append(row)
        self.rows.append(cst.NB_ROW-1)

        # buil board
        self.build_board()

    def build_board(self):

        # Build Label
        for row in range(cst.NB_ROW):
            for col in range(cst.NB_COL):
                if(self.grille[row+1][col+1] == cst.SYMBOL_X) :
                    txt = "X"
                    color = "yellow"
                elif(self.grille[row+1][col+1] == cst.SYMBOL_O) :
                    txt = "O"
                    color = "blue"
                else :
                    txt = ""
                    color = "gray"

                label = tk.Label(self.parent, text= txt, bg=color, width=6, height=2)
                self.labels[row][col] = label
                label.grid(row=row, column=col, padx=5, pady=5)

        # Build buttons
        for col in range(cst.NB_COL):
            button = tk.Button(self.parent, text="Col %s"%col, width=6, height=2,command= lambda x=col: self.button_clicked(x))
            self.buttons[col] = button
            button.grid(row=cst.NB_COL,column=col, padx=5, pady=5)

    def button_clicked(self, col):
        #Human
        if not self.gameover :
            self.play(self.human, col)

        #AI
        if not self.gameover :
            available_col = self.game.get_best_col(self.grille, self.rows, self.ai, self.human)
            self.play(self.ai, available_col-1)

    def play(self, player, col) :
        row = self.rows[col]
        self.rows[col] -= 1

        if(player.symbol == cst.SYMBOL_X) :
            txt = "X"
            color = "yellow"
        elif(player.symbol == cst.SYMBOL_O) :
            txt = "O"
            color = "blue"

        self.grille[row+1][col+1] = player.symbol

        label = tk.Label(self.parent, text= txt, bg=color, width=6, height=2)
        self.labels[row][col].grid_forget()
        self.labels[row][col]= label
        label.grid(row=row, column=col, padx=5, pady=5)

        if(self.rows[col] == -1) :
            self.buttons[col].config(state=tk.DISABLED)

        move = self.game.evaluate_move(self.grille, row+1, col+1, player)

        if(self.game.is_gameover(move)) :
            for col in range(cst.NB_COL):
                self.buttons[col].config(state=tk.DISABLED)
            self.gameover = True
            self.controller.show_winner(move, False)
        elif self.game.is_draw(self.rows):
            self.controller.show_winner(move, True)
