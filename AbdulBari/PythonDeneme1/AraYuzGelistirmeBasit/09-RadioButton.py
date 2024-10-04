import sys
from PyQt5.QtWidgets import QLabel, QWidget, QApplication, QRadioButton, QPushButton, QVBoxLayout

class Pencere(QWidget):
    
    def __init__(self):
        
        super().__init__()
        
        self.init_ui()
        
    def init_ui(self):
            
        self.radio_yazisi = QLabel("What language do you like mostly?")
        
        self.java = QRadioButton("Java")
        self.python = QRadioButton("Python")
        self.php = QRadioButton("Php")
        
        self.yazi_alani = QLabel("")
        self.buton = QPushButton("Send")

        v_box = QVBoxLayout()
        v_box.addWidget(self.radio_yazisi)
        v_box.addWidget(self.java)
        v_box.addWidget(self.python)
        v_box.addWidget(self.php)
        v_box.addStretch()
        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.buton)
        
        self.setLayout(v_box)

        # Butona týklama sinyalini fonksiyona baðla
        self.buton.clicked.connect(self.click)
        
        self.setWindowTitle("Radio Button Example")
        self.show()

    def click(self):
        if self.python.isChecked():
            self.yazi_alani.setText("Python")
        elif self.java.isChecked():
            self.yazi_alani.setText("Java")
        elif self.php.isChecked():
            self.yazi_alani.setText("Php")
        else:
            self.yazi_alani.setText("No language selected.")

app = QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())
