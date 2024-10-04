import sys  


from PyQt5 import QtWidgets


def Pencere():
    
    app = QtWidgets.QApplication(sys.argv)
    #Pencere objesi olu�turuldu
    pencere = QtWidgets.QWidget()
    #Ba�l�k
    pencere.setWindowTitle("PyQt5 Ders 1")
    pencere.show()
    sys.exit(app.exec_())

Pencere()
