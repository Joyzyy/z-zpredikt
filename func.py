from main import *

STADIU = 0

class Func(Statistica):
    def maximizeRestore(self):
        global STADIU
        statut = STADIU

        if statut == 0:
            self.showMaximized()

            STADIU = 1

            self.interfataGrafica.drop_shadow_layout.setContentsMargins(0, 0, 0, 0)
            self.interfataGrafica.drop_shadow_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #0e4485, stop:0.55 #092f5d);\n"
"border-radius: 0px;")
            self.interfataGrafica.butonMareste.setToolTip("Revin-o la forma initiala")
        else:
            STADIU = 0

            self.showNormal()

            self.resize(self.width() + 1, self.height() + 1)

            self.interfataGrafica.drop_shadow_layout.setContentsMargins(10, 10, 10, 10)
            self.interfataGrafica.drop_shadow_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #0e4485, stop:0.55 #092f5d);\n"
"border-radius: 5px;")
            self.interfataGrafica.butonMareste.setToolTip("Mareste")

    def something(self):
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.umbra = QGraphicsDropShadowEffect(self)
        self.umbra.setBlurRadius(20)
        self.umbra.setXOffset(0)
        self.umbra.setYOffset(0)
        self.umbra.setColor(QColor(0, 0, 0, 100))

        self.interfataGrafica.drop_shadow_frame.setGraphicsEffect(self.umbra)
        self.interfataGrafica.butonMareste.clicked.connect(lambda: Func.maximizeRestore(self))
        self.interfataGrafica.butonMinimizare.clicked.connect(lambda: self.showMinimized())
        self.interfataGrafica.butonInchide.clicked.connect(lambda: self.close())

        self.prindereDimensiune = QSizeGrip(self.interfataGrafica.frame_grip)
        self.prindereDimensiune.setStyleSheet("QSizeGrip { width: 10px; height: 10px; margin: 5px } QSizeGrip:hover { background-color: rgb(50, 42, 94) }")
        self.prindereDimensiune.setToolTip("Redimensionare fereastra")

    def stadiuReturnat():
        return STADIU
