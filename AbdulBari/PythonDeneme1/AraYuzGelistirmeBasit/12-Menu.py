import sys

from PyQt5.QtWidgets import QApplication,QAction,qApp,QMainWindow


class Menu(QMainWindow):

    def __init__(self):

        super().__init__()

        menubar = self.menuBar()

        dosya = menubar.addMenu("File")
        duzenle = menubar.addMenu("Edit")

        dosya_ac = QAction("Open File",self)

        dosya_ac.setShortcut("Ctrl+O")

        dosya_kaydet = QAction("Save File",self)
        dosya_kaydet.setShortcut("Ctrl+S")
        cikis = QAction("Exit", self)
        cikis.setShortcut("Ctrl+Q")

        dosya.addAction(dosya_ac)
        dosya.addAction(dosya_kaydet)
        dosya.addAction(cikis)


        ara_ve_degistir = duzenle.addMenu("Search and Change")

        ara = QAction("Search",self)

        degistir = QAction("Change",self)

        temizle = QAction("Delete",self)

        ara_ve_degistir.addAction(ara)

        ara_ve_degistir.addAction(degistir)
        duzenle.addAction(temizle)



        cikis.triggered.connect(self.cikis_yap)

        dosya.triggered.connect(self.response)

        self.setWindowTitle("Menu")

        self.show()

    def cikis_yap(self):
        qApp.quit()
    def response(self,action):

        if action.text() == "Open File":
            print("Clicked On Open File")
        elif action.text() == "Save File":
            print("Clicked On Save File")
        elif action.text() == "Exit":
            print("Clicked On Exit")



app = QApplication(sys.argv)

menu = Menu()


sys.exit(app.exec_())