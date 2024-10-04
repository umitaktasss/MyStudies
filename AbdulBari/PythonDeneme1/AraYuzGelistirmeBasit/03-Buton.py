import sys  


from PyQt5 import QtWidgets,QtGui, QtCore
from PyQt5.QtCore import center


def Pencere():
    
    app = QtWidgets.QApplication(sys.argv)
    #Pencere objesi oluþturuldu
    pencere = QtWidgets.QWidget()
    #Baþlýk
    pencere.setWindowTitle("PyQt5 Ders 3")
    
    buton=QtWidgets.QPushButton("Click!",pencere)
 
   
    etiket1=QtWidgets.QLabel("What the heck is going on? ",pencere)
    
    etiket2=QtWidgets.QLabel(pencere)
    
    
    buton.move(175,50)
    pixmap= QtGui.QPixmap("python.webp")
    

    scaled_pixmap=pixmap.scaled(150,150,aspectRatioMode=True)
    
    etiket2.setPixmap(scaled_pixmap)
    
    
   # Layout yöneticisi oluþturuldu ve bileþenler eklendi
    v_box = QtWidgets.QVBoxLayout()
    v_box.addWidget(etiket1, alignment=QtCore.Qt.AlignCenter)
    v_box.addWidget(etiket2, alignment=QtCore.Qt.AlignCenter)
    v_box.addWidget(buton, alignment=QtCore.Qt.AlignCenter)

    pencere.setLayout(v_box)


   
    pencere.setGeometry(100,100,500,500)
    
    pencere.show()
    
    sys.exit(app.exec_())
     
Pencere()