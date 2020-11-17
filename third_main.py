import sys
from random import randint
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QPixmap, QPen

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(590, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.press = QtWidgets.QPushButton(self.centralwidget)
        self.press.setGeometry(QtCore.QRect(204, 72, 121, 41))
        self.press.setStyleSheet("font: 12pt \"MS Reference Specialty\";\n"
                                 "text-decoration: line-through;\n"
                                 "background-color: rgb(0, 139, 208);")
        self.press.setObjectName("press")
        self.for_krug = QtWidgets.QLabel(self.centralwidget)
        self.for_krug.setGeometry(QtCore.QRect(46, 170, 501, 361))
        self.for_krug.setText("")
        self.for_krug.setAlignment(QtCore.Qt.AlignCenter)
        self.for_krug.setObjectName("for_krug")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 590, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Волшебная кнопка"))
        self.press.setText(_translate("MainWindow", "Нажми\n"
                                                    "на меня"))


class Zadacha2(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.for_krug.setPixmap(QPixmap(501, 361))
        self.press.clicked.connect(self.krug)

    def krug(self):
        x, y = [randint(10, 360) for i in range(2)]
        w, h = [randint(10, 100) for i in range(2)]
        # создаем экземпляр QPainter, передавая холст (self.label.pixmap())
        painter = QPainter(self.for_krug.pixmap())
        pen = QPen()
        pen.setWidth(3)
        pen.setColor(QColor(*[randint(0, 255) for i in range(3)]))
        painter.setPen(pen)
        painter.drawEllipse(x, y, w, h)
        painter.end()
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Zadacha2()
    ex.show()
    sys.exit(app.exec_())
