class DesignObject:


    def __init__(
        self,
        obj_type,
        x,
        y
    ):

        self.type = obj_type

        self.x = x

        self.y = y

        self.canvas_id = None



    def move(
        self,
        x,
        y
    ):

        self.x = x

        self.y = y



    def to_dict(self):

        return {

            "type": self.type,

            "x": self.x,

            "y": self.y

        }




# ==================================
# OBJET TEXTE
# ==================================


class TextObject(DesignObject):


    def __init__(
        self,
        x,
        y,
        text="Texte"
    ):


        super().__init__(

            "text",

            x,

            y

        )


        self.value = text


        self.font = "font_value"


        self.align = (

            "TextAlign::TOP_LEFT"

        )


        self.size = 16



    def to_dict(self):


        data = super().to_dict()


        data.update({

            "value": self.value,

            "font": self.font,

            "align": self.align,

            "size": self.size

        })


        return data





# ==================================
# OBJET IMAGE
# ==================================


class ImageObject(DesignObject):


    def __init__(

        self,

        x,

        y,

        image="icon_temp"

    ):


        super().__init__(

            "image",

            x,

            y

        )


        self.image = image



        self.width = 32

        self.height = 32



    def to_dict(self):


        data = super().to_dict()


        data.update({

            "image": self.image,

            "width": self.width,

            "height": self.height

        })


        return data





# ==================================
# OBJET RECTANGLE
# ==================================


class RectangleObject(DesignObject):


    def __init__(

        self,

        x,

        y,

        width=50,

        height=30

    ):


        super().__init__(

            "rectangle",

            x,

            y

        )


        self.width = width

        self.height = height




    def to_dict(self):


        data = super().to_dict()


        data.update({

            "width": self.width,

            "height": self.height

        })


        return data
