import tkinter as tk
from player import Player

class Form(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.init_form(controller)

    def init_form(self, controller):
        sg_label = tk.Label(
            self,
            text = 'Commencer une nouvelle partie',
            font = ('Times', 16))

        sg_button = tk.Button(self,
            text ="Jouer",
            relief=tk.GROOVE,
            cursor="man",
            width = 10,
            command = lambda : [sg_label.pack_forget(), sg_button.pack_forget(), self.player_form(controller)])

        sg_label.pack()
        sg_button.pack(pady=(10,0))

    def player_form(self, controller):
        form_label = tk.Label(
            self,
            text = 'Renseigner les informations suivantes :',
            font = ('Times', 16))

        username_label = tk.Label(
            self,
            text = 'Pseudo :',
            font = ('Times', 16))

        username_value = tk.StringVar()
        username_entry = tk.Entry(self, textvariable = username_value)

        reg = self.register(self.is_valid_string)
        username_entry.config(validate ="all", validatecommand =(reg, '%P'))


        symbol_label = tk.Label(
            self,
            text = 'Symbole :',
            font = ('Times', 16))

        symbol_value = tk.IntVar()
        symbol_choice1 = tk.Radiobutton(self, text="X", variable=symbol_value, value=1)
        symbol_choice2 = tk.Radiobutton(self, text="O", variable=symbol_value, value=0)


        submit_button = tk.Button(
                            self,
                            text="Valider",
                            relief=tk.GROOVE,
                            cursor="man",
                            width = 10,
                            command= lambda : retrieve_form_datas())

        form_label.pack(pady=(0,10))

        username_label.pack()
        username_entry.pack()

        symbol_label.pack(pady=(10,0))
        symbol_choice1.pack()
        symbol_choice2.pack()

        submit_button.pack(pady=(10,0))

        def retrieve_form_datas():
            username = username_value.get()
            symbol = symbol_value.get()
            if self.is_valid_string(username) and (symbol == 1 or symbol == 0):
                player = Player(username.strip(),symbol)
                controller.build_form_board(2, player)
            else:
                error_label = tk.Label(
                self,
                text = 'une erreur est survenue, veuillez renseigner votre pseudo et choisir un symbole',
                fg = 'red',
                font = ('Times', 16))

                error_label.pack()

    def is_valid_string(self, str):
        if str.isspace()  or str == "":
            print(str)
            return False
        elif len(str) > 10 :
            return False
        else :
            return True