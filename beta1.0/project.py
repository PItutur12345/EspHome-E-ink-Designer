import json
import os


from objects import (
    TextObject,
    ImageObject,
    RectangleObject
)



class ProjectManager:



    def __init__(self):


        self.folder = "projects"


        os.makedirs(

            self.folder,

            exist_ok=True

        )




    def save(

        self,

        filename,

        objects

    ):


        path = os.path.join(

            self.folder,

            filename + ".json"

        )



        data = []


        for obj in objects:


            data.append(

                obj.to_dict()

            )



        with open(

            path,

            "w",

            encoding="utf-8"

        ) as file:


            json.dump(

                data,

                file,

                indent=4,

                ensure_ascii=False

            )



        return path





    def load(

        self,

        filename

    ):


        path = os.path.join(

            self.folder,

            filename + ".json"

        )



        if not os.path.exists(path):

            return []



        with open(

            path,

            "r",

            encoding="utf-8"

        ) as file:


            data = json.load(file)



        objects = []



        for item in data:



            if item["type"] == "text":


                obj = TextObject(

                    item["x"],

                    item["y"],

                    item.get(

                        "value",

                        "Texte"

                    )

                )


                obj.font = item.get(

                    "font",

                    "font_value"

                )


                obj.align = item.get(

                    "align",

                    "TextAlign::TOP_LEFT"

                )



            elif item["type"] == "image":


                obj = ImageObject(

                    item["x"],

                    item["y"],

                    item.get(

                        "image",

                        "icon_temp"

                    )

                )



            elif item["type"] == "rectangle":


                obj = RectangleObject(

                    item["x"],

                    item["y"],

                    item.get(

                        "width",

                        50

                    ),

                    item.get(

                        "height",

                        30

                    )

                )



            else:

                continue



            objects.append(obj)



        return objects
