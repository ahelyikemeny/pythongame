from time import *
from n_mygameworld import *
from random import Random
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
                self.m.y = self.m.y - 200
                self.isJumped = True
                self.m.add_timer(timer=self.timer)
                print(self.m.y)



    def keyup(self, key, mod):
        print("UPP")
        if key == keys.SPACE:
            if self.isJumped == True:
                animate(self.m, pos=(self.m.x, 550), duration=(1))
                print(self.m.y)
                self.isJumped = False


    def update(self, deltaTime: float = 0.0166666666666666666666):
        super().update(deltaTime)
        self.m2.x = self.m2.x + 5
        self.cloud.x = self.cloud.x + 2
        self.m5.x = self.m5.x + 3
        self.lorandmadar.x = self.lorandmadar.x + 10
        self.resetrock()
        self.zsuppanauto()
        self.onrockHit()
        self.hptext.set_text("HP: " + str(self.hp))



    def resetrock(self):
        if self.m2.x == 1500:
            self.m2.set_x(0)
        if self.m5.x == 1500:
            self.m5.set_x(0)
        if self.lorandmadar.x == 1500:
            self.lorandmadar.set_x(0)

    def resetcloud(self):
        if self.cloud.x == 1366:
            self.cloud.set_x(0)

    def lose(self):
        self.m.remove_from_stage()
        self.add_actor(self.m4)

    def zsuppanauto(self):
        if self.isJumpedZsuppan == False:
            if self.zsuppan.x - self.m2.x == 50:
                self.zsuppan.set_y(self.zsuppan.y - 200)
                self.isJumpedZsuppan = True
                # print(self.zsuppan.x)
                # print(self.m2.x)
                print(self.zsuppan.x - self.m2.x)
        if self.isJumpedZsuppan == True:
            animate(self.zsuppan, pos=(self.zsuppan.x, self.zsuppan.y + 200), duration=1)
            self.isJumpedZsuppan = False

    def onrockHit(self):
        print(self.hp)
        print(self.m.y)
        print(self.m2.y)
        if self.m.is_on_stage():
            if self.m2.is_on_stage():
                if self.m.y ==   self.m2.y - 50:
                    if self.hp > 0:
                        if self.m.x - 50  == self.m2.x:
                            self.hp = self.hp - 1
                            if self.hp == 0:
                                self.hp = 0
                                music.play_once("uff.mp3")
                                self.lose()
        if self.m.is_on_stage():
            if self.m5.is_on_stage():
                if self.m.y ==   self.m5.y - 50:
                    if self.hp > 0:
                        if self.m.x - 50  == self.m5.x:
                            self.hp = self.hp - 1
                            if self.hp == 0:
                                self.hp = 0
                                self.lose()



    def __init__(self, menu: 'Menustage'):
        super().__init__()
        self.isJumped: bool = False
        self.isJumpedZsuppan: bool = False
        self.hp: int = 3
        self.hptext : MyLabel = MyLabel()
        # screen.blit("background",(0,0))
        self.background: MyActor = MyActor(("background.png"), pos=(0, 0), anchor=(0, 0))
        self.add_actor(self.background)
        self.background.set_size(1360, 768)
        self.m: MyActor = MyActor("kancsibase.png", pos=(300, 550), anchor=(0, 0))
        self.add_actor(self.m)
        self.m.set_width(100)
        self.zsuppan: MyActor = MyActor("zsuppanbase.png", pos=(600, 550), anchor=(0, 0))
        self.add_actor(self.zsuppan)
        self.zsuppan.set_width(100)
        self.m2: MyActor = MyActor("rock.png", pos=(0, 600), anchor=(0, 0))
        self.add_actor(self.m2)
        self.m2.set_height(200)
        self.m2.set_width(300)
        self.sun: MyActor = MyActor("unnamed.png", pos=(1366 - 190, 0), anchor=(0, 0))
        self.lorandmadar: MyActor = MyActor("rock.png", pos=(0, 350), anchor=(0, 0))
        self.add_actor(self.lorandmadar)
        self.lorandmadar.set_height(100)
        self.lorandmadar.set_width(100)
        self.sun : MyActor = MyActor("unnamed.png", pos=(1366 - 190, 0), anchor=(0,0))
        self.add_actor(self.sun)
        self.cloud: MyActor = MyActor("cloud.png", pos=(-20, 50), anchor=(0, 0))
        self.add_actor(self.cloud)
        self.timer: MyTickTimer = MyTickTimer(func=0, interval=2, startdelay=0, repeat=False)
        self.m2.set_height(25)
        self.m2.set_width(50)
        self.menu = menu
        speedMainCar: float = 0.1
        self.set_on_key_down_listener(self.keydown)
        self.set_on_key_up_listener(self.keyup)
        self.m4: MyActor = MyActor("gameover.png", pos=(0, 0), anchor=(0, 0))
        self.m5: MyActor = MyActor("rock.png", pos=(0, 600), anchor=(0, 0))
        self.add_actor(self.m5)
        self.m5.set_height(25)
        self.m5.set_width(50)
        music.play("tokyo.mp3")
        self.add_actor(self.hptext)

