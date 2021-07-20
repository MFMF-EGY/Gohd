from PyQt5 import QtGui
from PyQt5 import QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()


app = QtWidgets.QApplication([])
win = MainWindow()
win
win.show()
app.exec_()