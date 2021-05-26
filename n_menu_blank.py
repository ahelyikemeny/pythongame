
from n_mygameworld import *
from n_menu_menustage import *
class BlankStage(MyStage):
    def back(self, pos, btn):
        self.menu.menu_Main()

    def keydown(self, key, mod, unicode):
        print(key)
        if key == keys.ESCAPE:
            self.menu.menu_Main()
        if key == keys.UP:
            if self.m.y == 504:
                animate(self.m, pos=(self.m.x,240), duration=(0.2))
            if self.m.y == 240:
                animate(self.m, pos=(self.m.x, -24), duration=(0.2))
        if key == keys.DOWN:
            if self.m.y == 240:
                animate(self.m, pos=(self.m.x, 504), duration=(0.2))
            if self.m.y == -24:
                animate(self.m, pos=(self.m.x, 240), duration=(0.2))

    def update(self, deltaTime: float = 0.0166666666666666666666):
        super().update(deltaTime)
        self.m2.x = self.m2.x + 5
        self.hit()

    def hit(self):
        if self.m2.overlaps_with(self.m):
            self.m.remove_from_stage()
            print(self.m2)
###

    def __init__(self, menu: 'Menustage'):
        super().__init__()
        #screen.blit("background",(0,0))
        self.m: MyActor = MyActor("kancsi.png", pos=(300, 504), anchor=(0, 0))
        self.add_actor(self.m)
        self.m.set_width(100)
        self.zsuppán: MyActor = MyActor("auto.png", pos=(300, 504), anchor=(0, 0))
        self.m2: MyActor = MyActor("rock.png", pos=(300, 100), anchor=(0, 0))
        self.add_actor(self.m2)
        self.m2.set_height(200)
        self.m2.set_width(300)
        self.menu = menu
        speedMainCar : float = 0.1
        self.set_on_key_down_listener(self.keydown)