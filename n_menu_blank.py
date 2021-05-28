from time import *
from n_mygameworld import *
from n_menu_menustage import *
class BlankStage(MyStage):
    def back(self, pos, btn):
        self.menu.menu_Main()

    def keydown(self, key, mod, unicode):
        print(key)
        if key == keys.ESCAPE:
            self.menu.menu_Main()
        if key == keys.SPACE:
            if self.isJumped == False:
                self.m.y = self.m.y - 100
                self.isJumped = True
                print(self.m.y)



    def keyup(self, key, mod):
        print("UPP")
        if key == keys.SPACE:
            if self.isJumped == True:
                animate(self.m, pos=(self.m.x, 504), duration=(0.3))
                print(self.m.y)
                self.isJumped = False


    def update(self, deltaTime: float = 0.0166666666666666666666):
        super().update(deltaTime)
        self.m2.x = self.m2.x + 5
        self.hit()
        print(self.isJumped)
        self.resetrock()

    def hit(self):
        if self.m2.overlaps_with(self.m):
            self.m.remove_from_stage()
            print(self.m)

    def resetrock(self):
        if self.m2.x == 1500:
            self.m2.set_x(0)

    def lose(self):
        if self.m.remove_from_stage():
            self.add_actor(self.m4)


    def __init__(self, menu: 'Menustage'):
        super().__init__()
        self.isJumped: bool = False
        #screen.blit("background",(0,0))
        self.background: MyActor = MyActor(("background.png"), pos=(0,0), anchor=(0,0))
        self.add_actor(self.background)
        self.background.set_size(1360,768)
        self.m: MyActor = MyActor("kancsibase.png", pos=(300, 504), anchor=(0, 0))
        self.add_actor(self.m)
        self.m.set_width(100)
        self.zsuppan: MyActor = MyActor("zsuppanbase.png", pos=(400, 504), anchor=(0, 0))
        self.add_actor(self.zsuppan)
        self.zsuppan.set_width(100)
        self.m2: MyActor = MyActor("rock.png", pos=(0, 550), anchor=(0, 0))
        self.add_actor(self.m2)
        self.m2.set_height(25)
        self.m2.set_width(50)
        self.menu = menu
        speedMainCar : float = 0.1
        self.set_on_key_down_listener(self.keydown)
        self.set_on_key_up_listener(self.keyup)
        self.m4: MyActor = MyActor("gameover.png", pos=(0, 0), anchor=(0, 0))
        