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
        self.kancsi.set_color(135,206,235)
        self.add_actor(self.kancsi)
        self.kancsi.set_x(40)
        self.kancsi.set_y(100)
        self.kancsi.set_fontsize(60)

        self.kancsikep: MyActor = MyActor(("kancsikep.jpg"), pos=(40, 200), anchor=(0, 0))
        self.add_actor(self.kancsikep)
        self.kancsikep.set_size(228,405)

        self.milan: MyLabel = MyLabel()
        self.milan.set_text("Fellner Milán")
        self.milan.set_color(135,206,235)
        self.add_actor(self.milan)
        self.milan.set_x(380)
        self.milan.set_y(100)
        self.milan.set_fontsize(60)

        self.milankep: MyActor = MyActor(("milankep.jpg"), pos=(340, 200), anchor=(0, 0))
        self.add_actor(self.milankep)
        self.milankep.set_width(320)

        self.kele: MyLabel = MyLabel()
        self.kele.set_text("Kele Loránd")
        self.kele.set_color(135,206,235)
        self.add_actor(self.kele)
        self.kele.set_x(700)
        self.kele.set_y(100)
        self.kele.set_fontsize(60)

        self.kelekep: MyActor = MyActor(("kelekep.jpeg"), pos=(680, 200), anchor=(0, 0))
        self.add_actor(self.kelekep)
        self.kelekep.set_size(290,395)

        self.zsuppan: MyLabel = MyLabel()
        self.zsuppan.set_text("Zsuppán Flórián")
        self.zsuppan.set_color(135,206,235)
        self.add_actor(self.zsuppan)
        self.zsuppan.set_x(1010)
        self.zsuppan.set_y(100)
        self.zsuppan.set_fontsize(60)

        self.zsuppankep: MyActor = MyActor(("zsuppankep.png"), pos=(1020, 200), anchor=(0, 0))
        self.add_actor(self.zsuppankep)
        self.zsuppankep.set_size(298,427)
        self.set_on_key_down_listener(self.keydown)
