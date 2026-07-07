import tkinter as tk

from style import UIStyle

from objects import TextObject, ImageObject



class DesignCanvas(tk.Canvas):


    def __init__(self, parent, app):


        super().__init__(

            parent,

            width=UIStyle.EINK_WIDTH,

            height=UIStyle.EINK_HEIGHT,

            bg=UIStyle.CANVAS_BACKGROUND,

            highlightthickness=2,

            highlightbackground=UIStyle.BORDER_COLOR

        )


        self.app = app


        self.selected = None


        self.selection_box = None


        self.drag_x = 0

        self.drag_y = 0



        self.draw_grid()



        self.bind(

            "<Button-1>",

            self.click

        )


        self.bind(

            "<B1-Motion>",

            self.drag

        )


        self.bind(

            "<Delete>",

            self.delete_selected

        )


        self.bind(

            "<BackSpace>",

            self.delete_selected

        )



    # =========================
    # GRILLE E-INK
    # =========================


    def draw_grid(self):


        step = 20


        for x in range(

            0,

            UIStyle.EINK_WIDTH,

            step

        ):


            self.create_line(

                x,

                0,

                x,

                UIStyle.EINK_HEIGHT,

                fill="#eeeeee"

            )



        for y in range(

            0,

            UIStyle.EINK_HEIGHT,

            step

        ):


            self.create_line(

                0,

                y,

                UIStyle.EINK_WIDTH,

                y,

                fill="#eeeeee"

            )



    # =========================
    # CLIC SOURIS
    # =========================


    def click(self, event):


        self.focus_set()



        items = self.find_overlapping(

            event.x,

            event.y,

            event.x,

            event.y

        )


        # ignorer la grille

        items = [

            i for i in items

            if self.type(i) != "line"

        ]



        if items:


            item = items[-1]



            for obj in self.app.objects:


                if obj.canvas_id == item:


                    self.select_object(obj)



                    self.drag_x = event.x

                    self.drag_y = event.y


                    return



        # création objet texte


        if self.app.current_tool == "text":


            obj = TextObject(

                event.x,

                event.y

            )


            obj.canvas_id = self.create_text(

                event.x,

                event.y,

                text="Texte",

                anchor="nw",

                fill="black"

            )


            self.app.add_object(obj)



        # création image


        elif self.app.current_tool == "image":


            obj = ImageObject(

                event.x,

                event.y

            )


            obj.canvas_id = self.create_rectangle(

                event.x,

                event.y,

                event.x + 32,

                event.y + 32,

                outline="black"

            )


            self.app.add_object(obj)




    # =========================
    # SELECTION
    # =========================


    def select_object(self, obj):


        self.clear_selection()


        self.selected = obj



        bbox = self.bbox(

            obj.canvas_id

        )


        if bbox:


            self.selection_box = self.create_rectangle(

                bbox[0]-3,

                bbox[1]-3,

                bbox[2]+3,

                bbox[3]+3,

                outline=UIStyle.ACCENT,

                width=2

            )



        self.app.properties.show_object(obj)




    def clear_selection(self):


        if self.selection_box:


            self.delete(

                self.selection_box

            )


            self.selection_box = None





    # =========================
    # DEPLACEMENT
    # =========================


    def drag(self, event):


        if self.selected is None:

            return



        dx = event.x - self.drag_x

        dy = event.y - self.drag_y



        self.move(

            self.selected.canvas_id,

            dx,

            dy

        )



        self.selected.x += dx

        self.selected.y += dy



        self.drag_x = event.x

        self.drag_y = event.y



        self.update_selection_box()



        self.app.update_code()




    def update_selection_box(self):


        self.clear_selection()



        if self.selected:


            bbox = self.bbox(

                self.selected.canvas_id

            )


            if bbox:


                self.selection_box = self.create_rectangle(

                    bbox[0]-3,

                    bbox[1]-3,

                    bbox[2]+3,

                    bbox[3]+3,

                    outline=UIStyle.ACCENT,

                    width=2

                )




    # =========================
    # SUPPRESSION
    # =========================


    def delete_selected(self, event=None):


        if self.selected is None:

            return



        self.delete(

            self.selected.canvas_id

        )


        self.app.remove_object(

            self.selected

        )


        self.selected = None


        self.clear_selection()
