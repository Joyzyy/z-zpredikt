import sys, platform
from PyQt5.QtCore import (
    QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent
)
from PyQt5.QtGui import (
    QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient
)
from PyQt5.QtWidgets import *

from PyQt5.QtChart import *

from ui import Ui_MainWindow
from func import *

class Statistica(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.interfataGrafica = Ui_MainWindow()
        self.interfataGrafica.setupUi(self)

        def mutaFereastra(event):
            if Func.stadiuReturnat() == 1:
                Func.maximizeRestore(self)
            
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()
            
        self.interfataGrafica.title_bar.mouseMoveEvent = mutaFereastra

        Func.something(self)

        self.show()
    
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

if __name__ == "__main__":
    proiectStatistica = QApplication(sys.argv)
    fereastraPrincipala = Statistica()
    sys.exit(proiectStatistica.exec_())
