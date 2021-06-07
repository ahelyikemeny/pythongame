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
            print(self.elapsed_time)

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

    def keydown_zsuppan(self, key, mod, unicode):
        print(key)
        if key == keys.ESCAPE:
            self.menu.menu_Main()
        if key == keys.UP:
            print(self.elapsed_time)

            if self.isJumpedZsuppan == False:
                self.zsuppan.y = self.m.y - 200
                self.isJumpedZsuppan = True
                self.zsuppan.add_timer(timer=self.timer)
                print(self.zsuppan.y)

    def keyup_zsuppan(self, key, mod):
        print("UPP")
        if key == keys.UP:
            if self.isJumpedZsuppan == True:
                animate(self.m, pos=(self.m.x, 550), duration=(1))
                print(self.m.y)
                self.isJumpedZsuppan = False

    def update(self, deltaTime: float = 0.0166666666666666666666):
        super().update(deltaTime)
        self.m2.x = self.m2.x + 5
        if self.hp > 0:
            self.points = self.points + 1
        self.cloud.x = self.cloud.x + 2
        self.m5.x = self.m5.x + 3
        self.resetrock()
        self.onrockHit()
        self.hptext.set_text("Kancsi Életerő: " + str(self.hp))
        self.hptextzsuppan.set_text("Zsuppán Életerő: " +str(self.hptextzsuppan))
        if self.isJumped == True:
            self.ido = self.ido + 1
        if self.ido == 200:
            self.lose1()
            animate(self.m, pos = (self.m.x, -300), duration=0.6)

        self.pointsText.set_text("Pontok: " + str(self.points))



    def resetrock(self):
        if self.m2.x == 1500:
            self.m2.set_x(0)
        if self.m5.x == 1500:
            self.m5.set_x(0)

    def resetcloud(self):
        if self.cloud.x == 1366:
            self.cloud.set_x(0)

    def lose(self):
        music.play_once("uff.mp3")
        self.zsuppan.set_x(self.m.x)
        self.add_actor(self.losetext)
        self.losetext.set_text("Elkapott a Jeti")
        self.add_actor(self.m4)
        self.add_actor(self.newGame)
        self.newGame.set_text("Új játék")
        self.points = self.points
        self.remove_on_key_down_listener()
        self.remove_on_key_up_listener()
        self.add_actor(self.rankText)
        if self.points <= 350:
            self.rankText.set_x(550)
            self.rankText.set_text("Gyenge teljesítmény (" + str(self.points) + ")")
        if 1000 > self.points > 350:
            self.rankText.set_x(580)
            self.rankText.set_text("Ez már valami! (" + str(self.points) + ")")
        if 1500 > self.points > 1000:
            self.rankText.set_x(580)
            self.rankText.set_text("Nem vagy szar! (" + str(self.points) + ")")
        if 2000 > self.points > 1500:
            self.rankText.set_x(580)
            self.rankText.set_text("KI EZ AZ NBER?! (" + str(self.points) + ")")
        if self.points > 2000:
            self.rankText.set_x(580)
            self.rankText.set_text("GODLIKE!!!??!!?!?!?! (" + str(self.points) + ")")
        if self.points > 5000:
            self.rankText.set_x(580)
            self.rankText.set_text("Légyszíves mondd már el, hogy mivel csalsz mert eskü érdekel. :) (" + str(self.points) + ")")

        animate(self.m, pos=(1360, self.m.y), duration=(5))
        animate(self.zsuppan, pos=(1360, self.m.y), duration=(5))
        self.m2.remove_from_stage()
        self.m5.remove_from_stage()

    def lose1(self):
        music.play_once("uff.mp3")
        self.zsuppan.set_x(self.m.x)
        self.add_actor(self.losetext)
        self.losetext.set_text("Azt hitted lecsalhatod mi ? ")
        self.m2.remove_from_stage()
        self.m5.remove_from_stage()
        self.zsuppan.remove_from_stage()
        self.remove_on_key_up_listener()
        self.remove_on_key_down_listener()
        self.add_actor(self.newGame)
        self.newGame.set_text("Új játék")
        self.pointsText.remove_from_stage()

    def onrockHit(self):
        print(self.m.x)
        print(self.m5.x)
        if self.m.is_on_stage():
            if self.m2.is_on_stage():
                if self.m.y == self.m2.y - 50:
                    if self.hp > 0:
                        if -50 < self.m.x - self.m2.x <= 50:
                            print("jó az elmélet")
                            self.m2.x = self.m.x + 50
                            self.hp = self.hp - 1
                            if self.hp == 0:
                                self.hp = 0
                                self.lose()
        if self.m.is_on_stage():
            if self.m5.is_on_stage():
                if self.m.y == self.m5.y - 50:
                    if self.hp > 0:
                        if -51 < self.m.x - self.m5.x <= 51:
                            print("jó az elmélet2")
                            self.m5.x = self.m.x + 51
                            self.hp = self.hp - 1
                            if self.hp == 0:
                                self.hp = 0
                                self.lose()



    def __init__(self, menu: 'Menustage'):
        super().__init__()
        self.ido : float = self.elapsed_time
        self.isJumped: bool = False
        self.isJumpedZsuppan : bool = False
        self.hp : int = 3
        self.points : int = 0
        #screen.blit("background",(0,0))
        self.background: MyActor = MyActor(("background.png"), pos=(0,0), anchor=(0,0))
        self.add_actor(self.background)
        self.background.set_size(1360,768)
        self.m: MyActor = MyActor("kancsibase.png", pos=(300, 550), anchor=(0, 0))
        self.add_actor(self.m)
        self.m.set_width(100)
        self.zsuppan: MyActor = MyActor("zsuppanbase2.png", pos=(600, 550), anchor=(0, 0))
        self.add_actor(self.zsuppan)
        self.zsuppan.set_width(100)
        self.m2: MyActor = MyActor("rock.png", pos=(0, 600), anchor=(0, 0))
        self.add_actor(self.m2)
        self.m2.set_height(200)
        self.m2.set_width(300)
        self.sun: MyActor = MyActor("unnamed.png", pos=(1360 - 190, 0), anchor=(0, 0))
        #self.lorandmadar: MyActor = MyActor("rock.png", pos=(0, 350), anchor=(0, 0))
        #self.add_actor(self.lorandmadar)
        #self.lorandmadar.set_height(100)
        #self.lorandmadar.set_width(100)
        self.sun : MyActor = MyActor("unnamed.png", pos=(1360 - 190, 0), anchor=(0,0))
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
        self.set_on_key_down_listener(self.keydown_zsuppan())
        self.set_on_key_up_listener(self.keyup_zsuppan())
        self.m4: MyActor = MyActor("vege.png", pos=((1360 - 666)/2, 0), anchor=(0, 0))
        self.m5: MyActor = MyActor("rock.png", pos=(0, 600), anchor=(0, 0))
        self.add_actor(self.m5)
        self.m5.set_height(25)
        self.m5.set_width(50)
        self.hptext : MyLabel = MyLabel()
        self.hptextzsuppan : MyLabel = MyLabel()
        music.play("tokyo.mp3")
        self.add_actor(self.hptext)
        self.add_actor(self.hptextzsuppan)
        self.losetext: MyLabel = MyLabel()
        self.losetext.set_x(768 - 175)
        self.losetext.set_y(250)
        self.newGame: MyButton = MyButton()
        self.newGame.set_x(768 - 125)
        self.newGame.set_y(300)
        self.newGame.set_on_mouse_down_listener(self.menu.menu_Blank)
        self.pointsText: MyLabel = MyLabel()
        self.pointsText.set_x(0)
        self.pointsText.set_y(50)
        self.add_actor(self.pointsText)
        self.rankText: MyLabel = MyLabel()
        self.rankText.set_y(400)