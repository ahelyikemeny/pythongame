from n_mygameworld import *
from n_menu_menustage import *

class BlankStage(MyStage):

    def back(self, pos, btn):
        self.menu.menu_Main()

    def keydown(self, key, mod, unicode):
        print(key)
        if key == keys.ESCAPE:
            self.menu.menu_Main()

    def keydown(self, key, mod, unicode):
        print(key)
        if key == keys.UP:
            self.menu.menu_Main()
            animate(self.m, pos=(self.m.x + 10) (self.m.y +20))

    def __init__(self, menu: 'Menustage'):
        super().__init__()
        self.m: MyActor = MyActor("m_jerry.png", pos=(300, 300), anchor=(0, 0))
        self.m.set_on_mouse_down_listener(self.back)
        self.add_actor(self.m)
        print(self.m.y)
        self.menu = menu
        self.set_on_key_down_listener(self.keydown)