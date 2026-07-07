import tkinter as tk


from toolbar import ToolBar

from canvas import DesignCanvas

from properties import PropertiesPanel

from generator import CodeGenerator

from history import HistoryManager

from export import ExportManager

from project import ProjectManager

from style import UIStyle



class ESPHomeApp:



    def __init__(self):


        self.root = tk.Tk()



        # Configuration fenêtre

        self.root.title(
            UIStyle.WINDOW_TITLE
        )


        self.root.geometry(
            f"{UIStyle.WINDOW_WIDTH}x{UIStyle.WINDOW_HEIGHT}"
        )


        self.root.configure(
            bg=UIStyle.BACKGROUND
        )



        # Etat programme

        self.current_tool = "select"


        self.objects = []



        # Modules

        self.generator = CodeGenerator()


        self.history = HistoryManager()


        self.exporter = ExportManager()


        self.project = ProjectManager()



        self.create_interface()



        # raccourcis globaux

        self.root.bind(
            "<Delete>",
            self.delete_selected
        )


        self.root.bind(
            "<BackSpace>",
            self.delete_selected
        )




    def create_interface(self):


        # =====================
        # Barre outils
        # =====================

        self.toolbar = ToolBar(

            self.root,

            self.set_tool

        )


        self.toolbar.pack(

            side="top",

            fill="x"

        )



        # =====================
        # Zone centrale
        # =====================


        main = tk.Frame(

            self.root,

            bg=UIStyle.BACKGROUND

        )


        main.pack(

            fill="both",

            expand=True

        )



        # =====================
        # Canvas
        # =====================


        self.canvas = DesignCanvas(

            main,

            self

        )


        self.canvas.pack(

            side="left",

            padx=20,

            pady=20

        )



        # =====================
        # Propriétés
        # =====================


        self.properties = PropertiesPanel(

            main,

            self

        )


        self.properties.pack(

            side="right",

            fill="y",

            padx=15,

            pady=15

        )




    def set_tool(self, tool):

        self.current_tool = tool





    def add_object(self, obj):


        self.history.save(

            self.objects

        )


        self.objects.append(

            obj

        )


        self.update_code()





    def remove_object(self, obj):


        if obj in self.objects:


            self.history.save(

                self.objects

            )


            self.objects.remove(

                obj

            )


            self.update_code()





    def delete_selected(self, event=None):


        if self.canvas.selected:


            self.canvas.delete_selected()





    def update_code(self):


        code = self.generator.generate(

            self.objects

        )


        self.properties.set_code(

            code

        )





    def run(self):


        self.root.mainloop()
