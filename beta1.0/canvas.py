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

            highlightthickness=1

        )


        self.app = app

        self.selected = None

        self.drag_x = 0
        self.drag_y = 0


        self.bind(
            "<Button-1>",
            self.click
        )

        self.bind(
            "<B1-Motion>",
            self.drag
        )

        self.bind(
            "<ButtonRelease-1>",
            self.release
        )

        self.bind(
            "<Delete>",
            self.delete_selected
        )



    def click(self, event):

        # recherche d'un objet existant

        items = self.find_overlapping(

            event.x,

            event.y,

            event.x,

            event.y

        )


        if items:


            item = items[-1]


            for obj in self.app.objects:


                if obj.canvas_id == item:

                    self.selected = obj

                    self.drag_x = event.x

                    self.drag_y = event.y


                    self.app.properties.show_object(obj)

                    return



        # création d'un nouvel objet

        if self.app.current_tool == "text":


            obj = TextObject(

                event.x,

                event.y

            )


            obj.canvas_id = self.create_text(

                event.x,

                event.y,

                text="Texte",

                anchor="nw"

            )


            self.app.add_object(obj)



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



    def drag(self, event):

        if self.selected:


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


            self.app.update_code()

            self.app.properties.show_object(

                self.selected

            )



    def release(self, event):

        self.selected = None



    def delete_selected(self, event=None):

        if self.selected:


            self.delete(

                self.selected.canvas_id

            )


            self.app.remove_object(

                self.selected

            )


            self.selected = None
