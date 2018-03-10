import textwrap
from PIL import Image, ImageFont, ImageDraw


class PillowWrap(object):
    def __init__(self, picture):
        self.picture = picture
        self.wrap = False
        self.image = Image.open(picture)

    def wrap_text(self, text, font_size):
        self.text = text
        self.font = ImageFont.truetype('arial.ttf', font_size)
        self.font_size = font_size
        self.text_size = self.font.getsize(text)

        if self.text_size[0] > self.image.size[0]:
            self.wrap = True
            ratio = (self.image.size[0] * 100) / self.text_size[0]
            font_width = int((len(text) * ratio) / 100)
            self.twrap = textwrap.wrap(self.text, width=font_width)
            return self.twrap

    def draw_text(self):
        text_position_x = 0
        text_position_y = 0
        draw = ImageDraw.Draw(self.image)
        self.lines_height = 0
        if self.wrap:
            for text in self.twrap:
                draw.text((text_position_x, text_position_y +
                           self.lines_height), text, (0, 0, 0), font=self.font)
                self.lines_height += self.text_size[1]
        else:
            draw.text((text_position_x, text_position_y +
                      self.lines_height), self.text, (0, 0, 0), font=self.font)

    def save(self, newname):
        self.newname = newname
        self.image.save(self.newname + '.jpg', "JPEG")



