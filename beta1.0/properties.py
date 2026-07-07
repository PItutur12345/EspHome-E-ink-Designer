import tkinter as tk

from style import UIStyle



class PropertiesPanel(tk.Frame):


    def __init__(self, parent, app):

        super().__init__(

            parent,

            bg=UIStyle.PANEL_BACKGROUND,

            width=330

        )


        self.app = app

        self.current_object = None


        self.pack_propagate(False)


        self.create_ui()



    # =================================
    # CREATION INTERFACE
    # =================================

    def create_ui(self):


        title = tk.Label(

            self,

            text="Propriétés",

            bg=UIStyle.PANEL_BACKGROUND,

            fg=UIStyle.TEXT_COLOR,

            font=UIStyle.FONT_TITLE

        )


        title.pack(

            anchor="w",

            padx=15,

            pady=15

        )



        # -----------------------------
        # Position
        # -----------------------------


        position = tk.LabelFrame(

            self,

            text="Position",

            bg=UIStyle.PANEL_BACKGROUND,

            fg=UIStyle.TEXT_COLOR,

            font=UIStyle.FONT_NORMAL,

            bd=1

        )


        position.pack(

            fill="x",

            padx=15,

            pady=10

        )



        self.x_value = tk.StringVar(

            value="0"

        )


        self.y_value = tk.StringVar(

            value="0"

        )



        self.create_field(

            position,

            "X",

            self.x_value

        )


        self.create_field(

            position,

            "Y",

            self.y_value

        )



        apply_button = tk.Button(

            position,

            text="Appliquer",

            bg=UIStyle.BUTTON_ACTIVE,

            fg="white",

            relief="flat",

            cursor="hand2",

            command=self.apply_position

        )


        apply_button.pack(

            pady=10

        )



        # -----------------------------
        # Informations objet
        # -----------------------------


        object_box = tk.LabelFrame(

            self,

            text="Objet",

            bg=UIStyle.PANEL_BACKGROUND,

            fg=UIStyle.TEXT_COLOR

        )


        object_box.pack(

            fill="x",

            padx=15,

            pady=10

        )



        self.object_info = tk.Label(

            object_box,

            text="Aucun objet",

            bg=UIStyle.PANEL_BACKGROUND,

            fg=UIStyle.TEXT_SECONDARY,

            font=UIStyle.FONT_NORMAL

        )


        self.object_info.pack(

            pady=10

        )



        # -----------------------------
        # Code ESPHome
        # -----------------------------


        code_label = tk.Label(

            self,

            text="Code ESPHome",

            bg=UIStyle.PANEL_BACKGROUND,

            fg=UIStyle.TEXT_COLOR,

            font=UIStyle.FONT_NORMAL

        )


        code_label.pack(

            anchor="w",

            padx=15,

            pady=(15,5)

        )



        self.code = tk.Text(

            self,

            height=18,

            width=38,

            bg="#111315",

            fg="#00FF88",

            insertbackground="white",

            relief="flat",

            font=UIStyle.FONT_CODE

        )


        self.code.pack(

            padx=15,

            pady=5,

            fill="both",

            expand=True

        )




    # =================================
    # CHAMP TEXTE
    # =================================


    def create_field(

        self,

        parent,

        name,

        variable

    ):


        row = tk.Frame(

            parent,

            bg=UIStyle.PANEL_BACKGROUND

        )


        row.pack(

            fill="x",

            padx=10,

            pady=5

        )



        label = tk.Label(

            row,

            text=name,

            width=5,

            bg=UIStyle.PANEL_BACKGROUND,

            fg=UIStyle.TEXT_COLOR

        )


        label.pack(

            side="left"

        )



        entry = tk.Entry(

            row,

            textvariable=variable,

            bg="#151719",

            fg="white",

            insertbackground="white",

            relief="flat"

        )


        entry.pack(

            side="right",

            fill="x",

            expand=True

        )




    # =================================
    # AFFICHAGE OBJET
    # =================================


    def show_object(

        self,

        obj

    ):


        self.current_object = obj



        self.x_value.set(

            str(obj.x)

        )


        self.y_value.set(

            str(obj.y)

        )


        self.object_info.configure(

            text=(

                "Type : "

                + obj.type

            )

        )




    # =================================
    # MODIFICATION POSITION
    # =================================


    def apply_position(self):


        if self.current_object is None:

            return



        try:

            new_x = int(

                self.x_value.get()

            )


            new_y = int(

                self.y_value.get()

            )


        except ValueError:

            return



        dx = (

            new_x -

            self.current_object.x

        )


        dy = (

            new_y -

            self.current_object.y

        )



        self.app.canvas.move(

            self.current_object.canvas_id,

            dx,

            dy

        )



        self.current_object.x = new_x

        self.current_object.y = new_y



        self.app.update_code()




    # =================================
    # CODE
    # =================================


    def set_code(

        self,

        text

    ):


        self.code.delete(

            "1.0",

            tk.END

        )


        self.code.insert(

            tk.END,

            text

        )