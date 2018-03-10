import pytest
import os
from pillowwrap import PillowWrap


def test_init():
    picture = PillowWrap('mem.jpg')
    assert picture.wrap == False
    assert picture.image.size[0] > 0


def test_wrap_text_short():
    picture = PillowWrap('mem.jpg')
    picture.wrap_text('dsdsdsdsds', 20)
    assert len(picture.text) > 0
    assert picture.font_size == 20


def test_wrap_text_long():
    picture = PillowWrap('mem.jpg')
    picture.wrap_text(
        'dsdsdsdsds dsadsa  sadsadsad asds adsa sd asdsdsasadsad', 30)
    assert len(picture.text) > 0
    assert picture.font_size == 30
    assert picture.text_size[0] > picture.image.size[0]
    assert len(picture.twrap) >= 2


def test_draw_text_long():
    picture = PillowWrap('mem.jpg')
    picture.wrap_text(
        'dsdsdsdsds dsadsa  sadsadsad asds adsa sd asdsdsasadsad', 30)
    picture.draw_text()
    assert picture.lines_height > 0

def test_draw_text_short():
    picture = PillowWrap('mem.jpg')
    picture.wrap_text(
        'dsdsdsdsds ', 30)
    picture.draw_text()
    assert picture.lines_height == 0
   
    
def test_save():
    picture = PillowWrap('mem.jpg')
    picture.save("bolek")
    files = os.listdir()
    assert "bolek.jpg" in files
    
        
    
    