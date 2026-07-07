from tkinter import messagebox

from style import UIStyle



class AppIntegration:


    def __init__(self, app):

        self.app = app



    def export_lambda(self):


        code = self.app.generator.generate(

            self.app.objects

        )


        filename = self.app.exporter.export_lambda(

            code

        )


        messagebox.showinfo(

            "Export terminé",

            f"Fichier créé :\n{filename}"

        )



    def undo(self):


        if self.app.history.can_undo():


            state = self.app.history.undo()


            self.app.objects = state


            self.app.update_code()



    def redo(self):


        if self.app.history.can_redo():


            state = self.app.history.redo(

                self.app.objects

            )


            if state:

                self.app.objects = state

                self.app.update_code()
