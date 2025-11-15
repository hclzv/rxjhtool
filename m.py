from PyQt5 import QtCore,QtGui,QtWidgets,uic
import sys
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = QtWidgets.QMainWindow()
    window.show()
    sys.exit(app.exec_())