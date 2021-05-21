from n_mygameworld import *
from n_menu_menustage import *
from n_menu_gamestage import *

WIDTH = 1360
HEIGHT = 768


def on_key_down(key, mod, unicode):
    menu.on_key_down(key, mod, unicode)


def on_mouse_down(pos, button):
    menu.on_mouse_down(pos, button)


def update(dt):
    menu.update(dt)


def draw():
    screen.clear()
    menu.draw()


menu: Menustage = Menustage()


pgzrun.go()