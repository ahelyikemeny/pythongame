

from n_mygameworld import *
from n_menu_menustage import *
class BlankStage(MyStage):
    background = pygame.image.load("images\\auto.png")
    def back(self, pos, btn):
        self.menu.menu_Main()

    def keydown(self, key, mod, unicode):
        print(key)
        if key == keys.ESCAPE:
            self.menu.menu_Main()
        if key == keys.UP:
            if self.m.y == 504:
                animate(self.m, pos=(300,240))
            if self.m.y == 240:
                animate(self.m, pos=(300, -24))
        if key == keys.DOWN:
            if self.m.y == 240:
                animate(self.m, pos=(300, 504))
            if self.m.y == -24:
                animate(self.m, pos=(300, 240))


    def __init__(self, menu: 'Menustage'):
        super().__init__()
        #screen.blit("background",(0,0))
        self.m: MyActor = MyActor("auto.png", pos=(300, 504), anchor=(0, 0))
        self.m.set_on_mouse_down_listener(self.back)
        self.add_actor(self.m)
        self.menu = menu
        self.set_on_key_down_listener(self.keydown)