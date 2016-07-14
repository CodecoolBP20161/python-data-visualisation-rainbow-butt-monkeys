from textbox import TextBox
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import random

class Picture():
    list_of_textboxes = []
    list_of_reserved_coordinates = []
    size = (1366, 768)

    @classmethod
    def add_to_textboxes(self, color, size, name):
        self.list_of_textboxes.append(TextBox(name, color, size))

    @staticmethod
    def randomize():
        x = random.randint(0, 1166)
        y = random.randint(0, 688)
        tp = (x, y)
        return tp

    @classmethod
    def is_overlapping(cls, box1, box2):
        return box1[0][0] < box2[1][0] and \
               box1[1][0] > box2[0][0] and \
               box1[0][1] < box2[1][1] and \
               box1[1][1] > box2[0][1]


    @classmethod
    def put_in_list(self, size):
        if len(self.list_of_reserved_coordinates) == 0:
            tp_xy = Picture.randomize()
            tp = ((tp_xy[0], tp_xy[1]), (tp_xy[0] + size[0], tp_xy[1] + size[1]))
            if tp[1][0] > 1366 or tp[1][1] > 768:
                self.put_in_list(size)
            else:
                self.list_of_reserved_coordinates.append(tp)
                return tp
        else:
            while True:
                good = True
                tp_xy = Picture.randomize()
                tp = ((tp_xy[0], tp_xy[1]), (tp_xy[0] + size[0], tp_xy[1] + size[1]))
                for j in range(len(self.list_of_reserved_coordinates)):
                    if self.is_overlapping(tp, self.list_of_reserved_coordinates[j]):
                        good = False
                if good == True:
                    self.list_of_reserved_coordinates.append(tp)
                    return tp


    @classmethod
    def drawer(self):
        img = Image.new("RGB", self.size, "white")
        draw = ImageDraw.Draw(img)
        for i in self.list_of_textboxes:
            fnt = ImageFont.truetype("beyond_the_mountains.ttf", i.size)
            text_content = i.company_name
            text_size = draw.textsize(text_content, font=fnt)
            temp_coord = Picture.put_in_list(text_size)
            draw.text(temp_coord[0], text_content, font=fnt, fill=i.color)
        img.save('sample-out.png')


class Picture_2():
    list_of_textboxes = []
    list_of_reserved_coordinates = []

    @classmethod
    def add_to_textboxes(self, name, color, size):
        self.list_of_textboxes.append(TextBox(name, color, size))

    @classmethod
    def drawer(self):
        img = Image.new("RGB", (1366, 768), "white")
        draw = ImageDraw.Draw(img)
        for i in self.list_of_textboxes:
            # font = ImageFont.truetype(<font-file>, <font-size>)
            fnt = ImageFont.truetype("beyond_the_mountains.ttf", i.size)

            text_content = i.company_name
            text_size = draw.textsize(text_content)
            # draw.text((x, y),text_content,(r,g,b))
            rand_num1 = random.randint(100, 1200)
            rand_num2 = random.randint(100, 700)
            draw.text((rand_num1, rand_num2), text_content, font=fnt, fill = i.color)
            # draw.text((0, text_size[1]), text_content, **text_options)
        img.save('currency.png')


