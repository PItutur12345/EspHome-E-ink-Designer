import os

from datetime import datetime



class ExportManager:



    def __init__(self):


        self.folder = "exports"


        os.makedirs(

            self.folder,

            exist_ok=True

        )





    def export_lambda(

        self,

        code,

        filename="screen_lambda"

    ):


        path = os.path.join(

            self.folder,

            filename + ".yaml"

        )



        with open(

            path,

            "w",

            encoding="utf-8"

        ) as file:



            file.write(

                "# ESPHome E-Ink Designer\n"

            )


            file.write(

                "# Généré le : "

                + datetime.now().strftime(

                    "%d/%m/%Y %H:%M"

                )

                + "\n\n"

            )


            file.write(

                "lambda: |-\n"

            )



            for line in code.splitlines():


                file.write(

                    "  "

                    + line

                    + "\n"

                )



        return path





    def export_text(

        self,

        code,

        filename="screen_code"

    ):


        path = os.path.join(

            self.folder,

            filename + ".txt"

        )



        with open(

            path,

            "w",

            encoding="utf-8"

        ) as file:


            file.write(code)



        return path
