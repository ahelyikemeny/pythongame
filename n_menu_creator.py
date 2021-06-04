from n_mygameworld import *
from n_menu_menustage import *

class CreatorStage(MyStage):

    def back(self, pos, btn):
        self.menu.menu_Main()

    def keydown(self, key, mod, unicode):
        print(key)
        if key == keys.ESCAPE:
            self.menu.menu_Main()

    def __init__(self, menu: 'Creatorstage'):
        super().__init__()
        self.menu: CreatorStage = menu

        self.background: MyActor = MyActor(("creatorbg.jpg"), pos=(0, 0), anchor=(0, 0))
        self.add_actor(self.background)
        self.background.set_size(1360, 768)

        self.menu = menu
        self.kancsi: MyLabel = MyLabel()
        self.kancsi.set_text("Kancsal Máté")
        self.add_actor(self.kancsi)
        self.kancsi.set_x(100)
        self.kancsi.set_y(100)
        self.kancsi.set_fontsize(100)

        self.milan: MyLabel = MyLabel()
        self.milan.set_text("Fellner Milán")
        self.add_actor(self.milan)
        self.milan.set_x(200)
        self.milan.set_y(200)
        self.milan.set_fontsize(100)


        self.kele: MyLabel = MyLabel()
        self.kele.set_text("Kele Loránd")
        self.add_actor(self.kele)
        self.kele.set_x(300)
        self.kele.set_y(300)
        self.kele.set_fontsize(100)

        self.zsuppan: MyLabel = MyLabel()
        self.zsuppan.set_text("Zsuppán Flórián")
        self.add_actor(self.zsuppan)
        self.zsuppan.set_x(400)
        self.zsuppan.set_y(400)
        self.zsuppan.set_fontsize(100)
        self.set_on_key_down_listener(self.keydown)
