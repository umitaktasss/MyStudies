import sys
import os
from PyQt5.QtCore import QFile

from PyQt5.QtWidgets import QHBoxLayout, QLabel, QWidget, QApplication, QTextEdit, QLabel, QPushButton, QVBoxLayout,QFileDialog

from PyQt5.QtWidgets import QAction,qApp,QMainWindow

class Notepad(QWidget):
    
    def __init__(self):
        
        super().__init__()
        
        self.init_ui()
        
    def init_ui(self):
        self.yazi_alani= QTextEdit()
        self.temizle = QPushButton("Delete")
        self.ac=QPushButton("Open")
        self.kaydet = QPushButton("Save")
        
        h_box = QHBoxLayout()
        h_box.addWidget(self.temizle)
        h_box.addWidget(self.ac)
        h_box.addWidget(self.kaydet)
        
        v_box = QVBoxLayout()
        v_box.addWidget(self.yazi_alani)
        v_box.addLayout(h_box)
        
        self.setLayout(v_box)
        
        self.setWindowTitle("NotePad")
        self.temizle.clicked.connect(self.yaziyi_temizle)
        
        self.ac.clicked.connect(self.dosya_ac)
        self.kaydet.clicked.connect(self.dosya_kaydet)

    
    def yaziyi_temizle(self):
        self.yazi_alani.clear()
    def dosya_ac(self):
        dosya_ismi = QFileDialog.getOpenFileName(self,"HOME",os.getenv("Desktop"))
        with open(dosya_ismi[0],"r") as file:
            self.yazi_alani.setText(file.read())


    def dosya_kaydet(self):
        dosya_ismi = QFileDialog.getSaveFileName(self,"Dosya Kaydet",os.getenv("HOME"))
        
        with open (dosya_ismi[0],"w") as file:
            
            file.write(self.yazi_alani.toPlainText())
            


class Menu(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.pencere = Notepad()
        
        self.setCentralWidget(self.pencere)
        
        self.menuleri_olustur()
    
    def menuleri_olustur(self):
        menubar=self.menuBar()
        
        dosya = menubar.addMenu("Dosya")
        
        dosya_ac= QAction("Open File", self)
        dosya_ac.setShortcut("Ctrl+O")
        dosya_kaydet = QAction("Save File",self)
        dosya_kaydet.setShortcut("Ctrl+S")
        temizle = QAction("Delete",self)
        temizle.setShortcut("Ctrl+D")
        cikis=QAction("Exit",self)
        cikis.setShortcut("Ctrl+Q")
        
        dosya.addAction(dosya_ac)
        dosya.addAction(dosya_kaydet)
        dosya.addAction(temizle)
        dosya.addAction(cikis)
        

        dosya.triggered.connect(self.response)

        self.setWindowTitle("Text Editor")
        
        self.show()
    
    def response(self,action):
        if action.text() == "Open File":
            self.pencere.dosya_ac()
        elif action.text() == "Save File":
            self.pencere.dosya_kaydet()
        elif action.text() == "Delete":
            self.pencere.yaziyi_temizle()
        elif action.text() == "Exit":
            qApp.quit()
app = QApplication(sys.argv)

menu = Menu()
sys.exit(app.exec_())