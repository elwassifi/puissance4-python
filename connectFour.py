import tkinter as tk
from form import Form
from player import Player
from board import Board
from move import Move

class ConnectFour(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.build_menu()
        self.build_header()
        self.build_form_board(1, None)
        self.build_footer()

    def build_menu(self):
        self.menu_group = tk.Menu(self)

        self.menu_item1 = tk.Menu(self.menu_group, tearoff=0)
        self.menu_item1.add_command(label="Quitter", command=self.quit)

        self.menu_group.add_cascade(label="Fichier", menu=self.menu_item1)
        self.config(menu=self.menu_group)

    def build_header(self):
        tk.Label(
            self,
            text = 'PUISSANCE 4',
            font =('Times', 70, 'bold'),
            fg = 'blue'
            ).pack(side = tk.TOP, padx = 10, pady = 10)

    def build_form_board(self, action, player):
        if action == 1:
            self.form_container = tk.Frame(self, relief=tk.GROOVE)
            self.form_container.pack(side=tk.TOP, padx=100, pady=100)

            self.form_container.rowconfigure(0, weight=1)
            self.form_container.columnconfigure(0, weight=1)

            self.form = Form(self.form_container, self)
            self.form.grid(row=0, column=0, sticky="nsew")
            self.form.tkraise()
        elif action == 2:
            self.form_container.destroy()
            self.form.destroy()
            self.build_board(player)

    def build_board(self, player):
        self.board_container = tk.Frame(self, relief=tk.GROOVE)
        self.board_container.pack(side=tk.TOP, padx=30, pady=30)

        self.board_container.rowconfigure(0, weight=1)
        self.board_container.columnconfigure(0, weight=1)

        self.board = Board(self.board_container, self, player)
        self.board.tkraise()

    def show_winner(self, move, is_draw) :
        if is_draw :
            winner_label = tk.Label(
                self,
                text = 'Match nul !! Vous y étiez presque. Voulez-vous réessayer ?',
                font =('Times', 16),
                fg = "blue"
            )
            winner_label.pack()

        if (not is_draw) and move.player.is_ai :
            winner_label = tk.Label(
                self,
                text = 'Désolé :( !! ( '+ move.player.name+ ' ) vous a gagné. Voulez-vous réessayer ?',
                font =('Times', 16),
                fg = "red"
            )
            winner_label.pack()
        elif (not is_draw) and (not move.player.is_ai) :
            winner_label = tk.Label(
                self,
                text = 'Bravo ( '+ move.player.name+ ' ) :D !! Vous avez gagner. Voulez-vous réessayer ?',
                font =('Times', 16),
                fg = "green"
            )
            winner_label.pack()

        restart_button = tk.Button(
            self,
            text="Rejouer",
            relief=tk.GROOVE,
            cursor="man",
            width = 10,
            command= lambda : restart_game())

        restart_button.pack()

        def restart_game():
            self.board_container.destroy()
            self.board.destroy()
            winner_label.destroy()
            restart_button.destroy()
            self.build_form_board(1, None)

    def build_footer(self):
        tk.Label(
            self,
            text = 'Copyright © 2020 - elwassifi.fr',
            font =('Times', 16)
            ).pack(side = tk.BOTTOM, padx = 10, pady = 10)

if __name__ == "__main__":
    app = ConnectFour()
    app.title("Puissance 4")
    app.resizable(False, False)
    app.mainloop()