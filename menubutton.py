from pyglet import *
import glooey

class MenuLabel(glooey.Label):
    custom_color = '#212F3D'
    custom_font_name = 'Bank Gothic Md BT Medium'
    custom_font_size = '10'
    custom_alignment = 'center'


class MenuButton(glooey.Button):
    Label = MenuLabel
    custom_alignment = fill


    class Base(glooey.Image):
        custom_image = resource.image('Resources/Images/Menu Assets/menubuttonbase.png')
