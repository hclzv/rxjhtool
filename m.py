from PyQt5 import QtCore,QtGui,QtWidgets,uic
import sys
class A(QtWidgets.QMainWindow):
        def __init__(self):
            super().__init__()
            self.resize(680,420)
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = A()
    window.show()
    sys.exit(app.exec_())