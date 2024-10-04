import sys  


from PyQt5 import QtWidgets,QtGui
from PyQt5.QtCore import center


def Pencere():
    
    app = QtWidgets.QApplication(sys.argv)
    #Pencere objesi oluþturuldu
    pencere = QtWidgets.QWidget()
    #Baþlýk
    pencere.setWindowTitle("PyQt5 Ders 2")
    etiket1=QtWidgets.QLabel(pencere)
    etiket2=QtWidgets.QLabel(pencere)
    pixmap= QtGui.QPixmap("python.webp")
    scaled_pixmap=pixmap.scaled(150,150,aspectRatioMode=True)
    etiket2.setPixmap(scaled_pixmap)
    etiket1.setText("What the heck is going on ?")
    
    etiket1.move(175,30)
    pencere.setGeometry(100,100,500,500)
    pencere.show()
    sys.exit(app.exec_())
     
Pencere()
