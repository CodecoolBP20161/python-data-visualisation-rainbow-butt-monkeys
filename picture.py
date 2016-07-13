from textbox import TextBox
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import random

class Picture():
    list_of_textboxes = []
    list_of_reserved_coordinates = []

    @classmethod
    def add_to_textboxes(self, color, size, name):
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
            rand_num1 = random.randint(100, 1200)
            rand_num2 = random.randint(100, 700)
            draw.text((rand_num1, rand_num2), text_content, font=fnt, fill = i.color)
            # draw.text(Picture.generate_coords(Picture.list_of_reserved_coordinates, i), text_content, font=fnt, fill=i.color)
        img.save('sample-out.png')

    '''def generate_coords(coords,object):
        max_y=0
        if range(len(coords)) == 0:
            tp = ((0,0),(object.size[0],object.size[1]))
            coords.append(tp)
        else:
            for i in range(len(coords)):
                max_y = coords[i][1][1]
                if i % 5 == 0:
                    max_x = 0
                    if i % 5== 0 and i!=0:
                        for j in range(len(coords)):
                            if coords[j][1][0] > max_x:
                                max_x = coords[j][1][0]
                    max_y = 0
                tp = ((max_x,max_y),((max_x +object.size[0]),(max_y +object.size[1])))
                coords.append(tp)
        return coords'''

