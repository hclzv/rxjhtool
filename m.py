from PyQt5 import QtCore,QtGui,QtWidgets,uic
import sys
class A(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        layout = QtWidgets.QHBoxLayout()

        for i in range(10):
            btn = QtWidgets.QPushButton(f"btn {i}")
            btn.clicked.connect(lambda checked, x=i: QtWidgets.QMessageBox.information(self,"titile",x.__str__()))
            layout.addWidget(btn)
        self.setLayout(layout)



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = A()
    window.show()
    sys.exit(app.exec_())