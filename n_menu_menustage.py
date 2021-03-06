from n_mygameworld import *
from n_menu_blank import *
from n_menu_creator import *
#from n_menu_main import scr

class Menustage(MyStage):

    def menu_Main(self, pos=0, btn=0):
        self.onscreenstage = self

    def menu_Creator(self, pos=0, btn=0):
        self.onscreenstage = CreatorStage(self)

    def menu_Blank(self, pos=0, btn=0):
        self.onscreenstage = BlankStage(self)

    def menu_Exit(self, pos=0, btn=0):
        exit()

    def __init__(self):
        super().__init__()

        self.background: MyActor = MyActor(("bg.jpg"), pos=(0, 0), anchor=(0, 0))
        self.add_actor(self.background)
        self.background.set_size(1360, 768)

        menuitem2: MyActor = MyActor("playb.png", pos=((1360 - (790/2))/2, 150), anchor=(0, 0))
        menuitem2.set_size(395, 158)
        self.add_actor(menuitem2)
        menuitem2.set_on_mouse_down_listener(self.menu_Blank)

        menuitem3: MyActor = MyActor("goldc.png", pos=((1360 - (803/2))/2, 350), anchor=(0, 0))
        menuitem3.set_size(401, 155)
        self.add_actor(menuitem3)
        menuitem3.set_on_mouse_down_listener(self.menu_Creator)

        menuitem4: MyActor = MyActor("goldx.png", pos=((1360 - (772/2))/2, 550), anchor=(0, 0))
        menuitem4.set_size(386, 161)
        self.add_actor(menuitem4)
        menuitem4.set_on_mouse_down_listener(self.menu_Exit)

        menuitem5: MyActor = MyActor("jateknev.png", pos=((1360 - (1400/2))/2, -100), anchor=(0, 0))
        menuitem5.set_size(720,304)
        self.add_actor(menuitem5)

        self.onscreenstage: MyStage = self

    def tikk(self, timer):
        print("TIKK")

    def draw(self):
        if self == self.onscreenstage:
            super(Menustage, self).draw()
        else:
            self.onscreenstage.draw()

    def update(self, delta_time: float = 0.0166666666666666666666):
        if self == self.onscreenstage:
            super(Menustage, self).update(delta_time)
        else:
            self.onscreenstage.update(delta_time)

    def on_mouse_down(self, pos, button):
        if self == self.onscreenstage:
            super(Menustage, self).on_mouse_down(pos, button)
        else:
            self.onscreenstage.on_mouse_down(pos, button)

    def on_key_down(self, key, mod, unicode):
        if self == self.onscreenstage:
            super().on_key_down(key, mod, unicode)
        else:
            self.onscreenstage.on_key_down(key, mod, unicode)

    def on_key_up(self, key, mod):
        if self == self.onscreenstage:
            super().on_key_up(key, mod)
        else:
            self.onscreenstage.on_key_up(key, mod)


