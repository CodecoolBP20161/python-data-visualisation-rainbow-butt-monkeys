from textbox import TextBox
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

class Picture():
    list_of_textboxes = []
    list_of_reserved_coordinates = []

    @classmethod
    def add_to_textboxes(self, color, size, name):
        self.list_of_textboxes.append(TextBox(name, color, size))

    @classmethod
    def drawer(self):
        '''img = Image.new("RGB", (1366, 768), "Red")
        draw = ImageDraw.Draw(img)
        # font = ImageFont.truetype(<font-file>, <font-size>)
        fnt = ImageFont.truetype("sans-serif.ttf", self.list_of_textboxes[0].size)
        text_options = {
            'fill': (255, 255, 255)
        }
        text_content = self.list_of_textboxes[0].company_name
        text_size = draw.textsize(text_content)
        # draw.text((x, y),text_content,(r,g,b))
        draw.text((0, 0), text_content, font = fnt, **text_options)
        # draw.text((0, text_size[1]), text_content, **text_options)
        # draw.text((text_size[0], 0), text_content, **text_options)
        # draw.text(text_size, text_content, **text_options)
        img.save('sample-out.png')

'''
        img = Image.new("RGB", (1366, 768), "black")
        draw = ImageDraw.Draw(img)
        # font = ImageFont.truetype(<font-file>, <font-size>)
        fnt = ImageFont.truetype("beyond_the_mountains.ttf", 48)
        text_options = {
            'fill': (255, 255, 255)
        }
        text_content = self.list_of_textboxes[0].company_name
        text_size = draw.textsize(text_content)
        # draw.text((x, y),text_content,(r,g,b))
        draw.text((0, 0), text_content, font=fnt, **text_options)
        # draw.text((0, text_size[1]), text_content, **text_options)
        # draw.text((text_size[0], 0), text_content, **text_options)
        # draw.text(text_size, text_content, **text_options)
        img.save('sample-out.png')

