import json,datetime,time
from PyQt5 import QtCore,QtGui,QtWidgets,uic
import sys,os
from androidServerUi import Ui_Form
import androidServer
import uuid

class A(QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()
        self.resize(680,420)
        self.btns = []
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.serverThread = T()
        self.ui.pushButton.clicked.connect(self.serverStart)
        self.serverThread.pyqtSignal_str.connect(self.addServer)
        self.ui.pushButton_3.clicked.connect(self.sendmsg)

        QtCore.QTimer.singleShot(3000,lambda:[print(b.isChecked()) for b in self.btns])

    def serverStart(self):
        self.serverThread.start()
    
    def serverStop(self,filename):
        for btn in self.btns:
            if btn.isChecked():
                server = btn.text()
        print("准备发送的文件: ",filename)
        androidServer.clients.get(server).send_file(filename)

    def sendmsg(self):
        self.qfilediong = QtWidgets.QFileDialog()
        self.qfilediong.setDirectory("d:/")
        self.qfilediong.fileSelected.connect(lambda x:self.serverStop(x))
        self.qfilediong.exec_()
        pass

    def addServer(self,serverid):
        w = QtWidgets.QPushButton(serverid)
        w.setCheckable(True)
        self.btns.append(w)
        self.ui.gridLayout.addWidget(w)

class T(QtCore.QThread):
    pyqtSignal_str =  QtCore.pyqtSignal(str)
    def __init__(self):
        super().__init__()

    def run(self) -> None:
        androidServer.reactor.listenTCP(6353, androidServer.EchoFactory(self.pyqtSignal_str))
        print("Server started on port 6353")
        androidServer.reactor.run(installSignalHandlers=False) 
        # androidServer.reactor.run()

def main():
    pass


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = A()
    window.show()
    sys.exit(app.exec_())
