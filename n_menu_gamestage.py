from n_mygameworld import *
from n_menu_menustage import *

class CreatorStage(MyStage):

    def back(self, pos, btn):
        self.menu.menu_Main()

    #def jerrymove(self, pos, btn):
        #animate(self.m, pos=pos)

    def keydown(self, key, mod, unicode):
        print(key)
        if key == keys.ESCAPE:
            self.menu.menu_Main()



    def __init__(self, menu: 'Creatorstage'):
        super().__init__()
        #self.m: MyActor = MyActor("auto.png", pos=(600, 150), anchor=(0, 0))
        #self.m.set_on_mouse_down_listener(self.back)
        #self.add_actor(self.m)
        self.menu: CreatorStage = menu
        #self.set_on_mouse_down_listener(self.jerrymove)

        self.kancsi : MyLabel = MyLabel()
        self.kancsi.set_text("kancsi")
        self.add_actor(self.kancsi)