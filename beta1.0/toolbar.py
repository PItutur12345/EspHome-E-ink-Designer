import tkinter as tk

from style import UIStyle



class ToolBar(tk.Frame):


    def __init__(self, parent, callback):

        super().__init__(

            parent,

            bg=UIStyle.PANEL_BACKGROUND,

            height=60

        )


        self.callback = callback


        self.buttons = {}


        self.current_tool = "select"


        self.create_ui()



    def create_ui(self):


        # titre application

        title = tk.Label(

            self,

            text="ESPHome E-Ink Designer",

            bg=UIStyle.PANEL_BACKGROUND,

            fg=UIStyle.TEXT_COLOR,

            font=UIStyle.FONT_TITLE

        )


        title.pack(

            side="left",

            padx=20

        )



        # séparation visuelle

        separator = tk.Frame(

            self,

            width=2,

            bg=UIStyle.BORDER_COLOR

        )


        separator.pack(

            side="left",

            fill="y",

            pady=10,

            padx=10

        )



        # outils

        tools = [

            (
                "🖱 Sélection",
                "select"
            ),

            (
                "T Texte",
                "text"
            ),

            (
                "▣ Image",
                "image"
            )

        ]



        for name, value in tools:


            button = tk.Button(

                self,

                text=name,

                width=14,

                height=1,

                relief="flat",

                bd=0,

                bg=UIStyle.BUTTON_COLOR,

                fg=UIStyle.TEXT_COLOR,

                activebackground=UIStyle.BUTTON_ACTIVE,

                activeforeground="white",

                font=UIStyle.FONT_NORMAL,

                cursor="hand2",


                command=lambda v=value:
                    self.select_tool(v)

            )



            button.pack(

                side="left",

                padx=5,

                pady=12

            )


            self.buttons[value] = button



        # sélection par défaut

        self.update_buttons()



    def select_tool(self, tool):


        self.current_tool = tool


        self.callback(tool)


        self.update_buttons()




    def update_buttons(self):


        for name, button in self.buttons.items():


            if name == self.current_tool:


                button.configure(

                    bg=UIStyle.BUTTON_ACTIVE,

                    fg="white"

                )


            else:


                button.configure(

                    bg=UIStyle.BUTTON_COLOR,

                    fg=UIStyle.TEXT_COLOR

                )
