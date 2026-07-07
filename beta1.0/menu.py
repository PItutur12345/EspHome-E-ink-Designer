import tkinter as tk
from tkinter import filedialog, messagebox

from style import UIStyle



class AppMenu:


    def __init__(self, app):

        self.app = app

        self.create_menu()



    def create_menu(self):


        menubar = tk.Menu(

            self.app.root,

            bg=UIStyle.PANEL_BACKGROUND,

            fg=UIStyle.TEXT_COLOR

        )


        # ======================
        # Fichier
        # ======================


        file_menu = tk.Menu(

            menubar,

            tearoff=0

        )


        file_menu.add_command(

            label="Nouveau projet",

            command=self.new_project

        )


        file_menu.add_command(

            label="Ouvrir",

            command=self.open_project

        )


        file_menu.add_command(

            label="Sauvegarder",

            command=self.save_project

        )


        file_menu.add_separator()


        file_menu.add_command(

            label="Exporter ESPHome",

            command=self.export_esphome

        )


        file_menu.add_separator()


        file_menu.add_command(

            label="Quitter",

            command=self.app.root.destroy

        )


        menubar.add_cascade(

            label="Fichier",

            menu=file_menu

        )



        # ======================
        # Edition
        # ======================


        edit_menu = tk.Menu(

            menubar,

            tearoff=0

        )


        edit_menu.add_command(

            label="Annuler",

            command=self.undo

        )


        edit_menu.add_command(

            label="Refaire",

            command=self.redo

        )


        menubar.add_cascade(

            label="Edition",

            menu=edit_menu

        )



        # ======================
        # Ecran
        # ======================


        screen_menu = tk.Menu(

            menubar,

            tearoff=0

        )


        screen_menu.add_command(

            label="E-Ink 400x300",

            command=lambda:
                self.set_screen(
                    400,
                    300
                )

        )


        screen_menu.add_command(

            label="E-Ink 296x128",

            command=lambda:
                self.set_screen(
                    296,
                    128
                )

        )


        menubar.add_cascade(

            label="Ecran",

            menu=screen_menu

        )



        # ======================
        # Aide
        # ======================


        help_menu = tk.Menu(

            menubar,

            tearoff=0

        )


        help_menu.add_command(

            label="A propos",

            command=self.about

        )


        menubar.add_cascade(

            label="Aide",

            menu=help_menu

        )



        self.app.root.config(

            menu=menubar

        )




    # ======================
    # ACTIONS
    # ======================


    def new_project(self):


        self.app.objects.clear()


        self.app.canvas.delete(

            "all"

        )


        self.app.canvas.draw_grid()


        self.app.update_code()




    def save_project(self):


        path = self.app.project.save(

            "project",

            self.app.objects

        )


        messagebox.showinfo(

            "Sauvegarde",

            f"Projet enregistré :\n{path}"

        )




    def open_project(self):


        objects = self.app.project.load(

            "project"

        )


        self.app.objects = objects


        self.app.canvas.delete(

            "all"

        )


        self.app.canvas.draw_grid()


        self.app.update_code()




    def export_esphome(self):


        code = self.app.generator.generate(

            self.app.objects

        )


        path = self.app.exporter.export_lambda(

            code

        )


        messagebox.showinfo(

            "Export",

            f"Fichier créé :\n{path}"

        )




    def undo(self):


        if self.app.history.can_undo():


            state = self.app.history.undo(

                self.app.objects

            )


            self.app.objects = state


            self.app.update_code()




    def redo(self):


        if self.app.history.can_redo():


            state = self.app.history.redo(

                self.app.objects

            )


            self.app.objects = state


            self.app.update_code()




    def set_screen(

        self,

        width,

        height

    ):


        UIStyle.EINK_WIDTH = width

        UIStyle.EINK_HEIGHT = height


        self.app.canvas.config(

            width=width,

            height=height

        )




    def about(self):


        messagebox.showinfo(

            "ESPHome E-Ink Designer",

            "Designer graphique ESPHome\nVersion 1.0"

        )
