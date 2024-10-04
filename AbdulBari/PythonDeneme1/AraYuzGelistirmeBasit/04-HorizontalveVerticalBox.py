import sys  


from PyQt5 import QtWidgets,QtGui, QtCore
from PyQt5.QtCore import center


def Pencere():
    
    app = QtWidgets.QApplication(sys.argv)
    okay = QtWidgets.QPushButton("Okay")
    cancel=QtWidgets.QPushButton("Cancel")
    #h_box=QtWidgets.QHBoxLayout()
    #h_box.addWidget(okay)
    #h_box.addWidget(cancel)
    #h_box.addStretch()
    v_box=QtWidgets.QVBoxLayout()
    v_box.addWidget(okay)
    v_box.addStretch()
    v_box.addWidget(cancel)
    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("PyQt5 Ders 4")
    

    pencere.setLayout(v_box)
    pencere.setGeometry(250,250,750,750)
    
    pencere.show()
    
    sys.exit(app.exec_())
    

Pencere()