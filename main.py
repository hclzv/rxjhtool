from PyQt5 import QtCore,QtGui,QtWidgets,uic
import sys,datetime,os,time,subprocess,json,threading,psutil
import requests
from typing import List,Dict
from bs4 import BeautifulSoup
from socketserver import BaseServer, TCPServer,DatagramRequestHandler
from http.server import SimpleHTTPRequestHandler,HTTPServer
from functools import partial

class A(QtWidgets.QMainWindow):
        def __init__(self):
            super().__init__()
            mainUi = uic.loadUi("syncui.ui")
            self.setWindowTitle("远程测试工具(P-j) v2024211")
            self.showtext:QtWidgets.QTextEdit = mainUi.textEdit
            self.comboBox:QtWidgets.QComboBox = mainUi.comboBox
            self.lineEdit_2:QtWidgets.QLineEdit = mainUi.lineEdit_2
            self.lineEdit_4:QtWidgets.QLineEdit = mainUi.lineEdit_4

            self.connectbtn:QtWidgets.QPushButton = mainUi.pushButton
            self.scrollAreaWidgetContents:QtWidgets.QWidget = mainUi.scrollAreaWidgetContents
            self.pushButton_4 :QtWidgets.QPushButton= mainUi.pushButton_4
            self.pushButton_3 :QtWidgets.QPushButton= mainUi.pushButton_3
            self.pushButton_8 :QtWidgets.QPushButton= mainUi.pushButton_8 #http start
            self.pushButton_9 :QtWidgets.QPushButton= mainUi.pushButton_9 #http stop
            self.pushButton_10 :QtWidgets.QPushButton= mainUi.pushButton_10 #http stop
            self.widget_4:QtWidgets.QWidget = mainUi.widget_4
            self.label_3:QtWidgets.QLabel = mainUi.label_3
            self.label_4:QtWidgets.QLabel = mainUi.label_4
            self.mainApp = None
            self.progressBar :QtWidgets.QProgressBar= mainUi.progressBar
            self.widget_4.setHidden(True)

            self.serverSoftwareList:List[str] = []
            self.curQWidgets:List[QtWidgets.QWidget] = []
            self.scrollAreaWidgetContentsVbox = QtWidgets.QVBoxLayout()
            self.names : List[str] = []

            self.t = T(self.names,None,self.comboBox.currentText())
            self.t.finished.connect(self.tfinish)
            self.t.py.connect(self.setPrb)

            self.scrollAreaWidgetContents.setLayout(self.scrollAreaWidgetContentsVbox)
            self.connectbtn.clicked.connect(self.init)
            self.pushButton_3.clicked.connect(self.startApp)
            self.pushButton_4.clicked.connect(self.tStart)
            self.resize(880,620)
            self.loadjson()
            self.clickedsManage()

            self.setCentralWidget(mainUi)

        def init(self):
            self.getServerSoftware(self.comboBox.currentText())
            
        def clickedsManage(self):
            self.pushButton_10.clicked.connect(lambda:subprocess.run(f"explorer {self.lineEdit_2.text()}"))
            self.lineEdit_2.textChanged.connect(lambda text:self.pushButton_10.setEnabled(True) if os.path.isdir(text) else self.pushButton_10.setEnabled(False))
            def setrul(text):
                self.t.url = text
            self.comboBox.currentTextChanged.connect(lambda text:setrul(text))
            self.pushButton_8.clicked.connect(self.httpStart)
            self.pushButton_9.clicked.connect(self.httpStop)

        def tfinish(self):
            self.widget_4.setHidden(True)
            self.progressBar.setValue(0)
            self.pushButton_4.setToolTip("下载完成 ")

        def httpinit(self):
            httpdirectory = self.lineEdit_4.text()
            self.hsv_is_run = False
            if httpdirectory.__len__() <1 and not os.path.isdir(httpdirectory):
                httpdirectory = os.getcwd()
            self.hsv = HTTPServer(("",8000),partial(H,httpdirectory))

        def httpStart(self):
            self.httpinit()
            if not self.hsv_is_run:
                self.hsvTh = threading.Thread(target=self.hsv.serve_forever)
                self.hsvTh.start()
                self.label_4.setText("http服务运行中..http://0.0.0.0:8000")
                self.infoappend("http服务器已启动 http://0.0.0.0:8000")
                self.hsv_is_run = True
 
        def httpStop(self):
            if self.hsv_is_run: 
                self.hsv.shutdown()
                self.hsvTh.join()
                self.label_4.setText("http服务未运行")
                self.infoappend("http服务器已停止")
                self.hsv_is_run = False
   
        def loadjson(self):
            with open("server.json") as fp:
                data:Dict = json.load(fp)
            self.comboBox.addItems([url for url in data.values()])

        def tStart(self):
            self.progressBar.setMaximum(self.names.__len__())
            print(self.names)
            if not self.t.isRunning() and self.names.__len__() >= 1:
                self.widget_4.setHidden(False)
                self.t.url = self.comboBox.currentText()
                self.t.savepath = self.lineEdit_2.text()
                self.t.start()
                self.pushButton_4.setEnabled(False)
                self.pushButton_4.setToolTip("下载中..."+datetime.datetime.now().strftime('%Y-%m-%d-%H_%M_%S'))

        def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
            if self.t.isRunning():
                self.t.terminate()
           
        def startApp(self):
            self.tStart()
            def f():
                startPath = None
                root = os.getcwd()
                if self.mainApp:
                    app = self.mainApp
                    app = str(app).lstrip().rstrip()
                    root = self.lineEdit_2.text().__len__()
                    if root != 0:
                        startPath =  os.path.join(self.lineEdit_2.text(),app)
                    else:
                        startPath = os.path.join(os.getcwd(),app)
                    if startPath:
                        def start():
                            if os.path.isdir(startPath):
                                subprocess.run(f'''{startPath}''')
                                self.infoappend(f"{app} 进程已启动")
                        t = threading.Thread(target=start)
                        t.start()

            self.t.finished.connect(f)

        def setPrb(self,int,str):
            self.progressBar.setValue(int)

        def infoappend(self,mes):
            self.showtext.insertPlainText(f"\n时间: {datetime.datetime.now().strftime('%Y-%m-%d-%H_%M_%S')} :{mes} ")

        def getServerSoftware(self,url):
            self.infoappend("刷新成功")
            text =  requests.get(url).text
            soup = BeautifulSoup(text, 'html.parser')
            li_elements = soup.find_all('li')
            li_texts = [li.text for li in li_elements]
            for li in li_texts:
                 self.serverSoftwareList.append(li)

            
            def added(c:QtWidgets.QCheckBox,name:str):
                if c.isChecked() and c not in self.names:
                    self.names.append(name)
                elif c in self.names:
                    self.names.remove(name)

                if self.names:
                    self.pushButton_4.setEnabled(True)
                else:
                    self.pushButton_4.setEnabled(False)
            
            def radidck(c:QtWidgets.QRadioButton,cke:QtWidgets.QCheckBox,name:str):
                if c.isChecked():
                    mainApp = c.text()[11:]
                    self.label_3.setText(f"启动程序: {mainApp} ")
                    self.mainApp = mainApp
                    self.pushButton_4.setEnabled(True)
                    self.pushButton_3.setEnabled(True)
                    cke.setChecked(True)
                else:
                    self.label_3.setText(f"未设置启动程序")
                    self.mainApp = None

            for ii,i in enumerate(self.serverSoftwareList):
                curBtn = QtWidgets.QPushButton(f"下载 (下载)")
                curBtn.setSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,QtWidgets.QSizePolicy.Policy.MinimumExpanding)
                curCheck = QtWidgets.QCheckBox(f"文件:{ii} : {i}")
                maincurCheck = QtWidgets.QRadioButton(f"设置程序为入口{ii} : {i}")
                curCheck.clicked.connect(lambda b,cc=curCheck,name=i:added(cc,name))
                maincurCheck.clicked.connect(lambda c,ria=maincurCheck,cke=curCheck,name=i:radidck(ria,cke,name))
                curHox = QtWidgets.QHBoxLayout()
                curHox.addWidget(maincurCheck)
                curHox.addWidget(curCheck)
                curHox.addWidget(curBtn)
                self.curQWidgets.append(curHox)
                self.scrollAreaWidgetContentsVbox.addLayout(curHox)

class S(DatagramRequestHandler):
    def __init__(self, request, client_address, server: BaseServer) -> None:
        super().__init__(request, client_address, server)

    def handle(self) -> None:
        return super().handle()

class T(QtCore.QThread):
    py = QtCore.pyqtSignal([int,str])
    ms = QtCore.pyqtSignal(str)

    def __init__(self,ls:List[str],savepath=None,url=None):
        super().__init__()    
        self.ls = ls
        self.savepath = savepath
        self.url = url

    def run(self) -> None:
        for index,i in enumerate(self.ls):
            dlurl = self.url+i
            p = self.download(dlurl,i)
            self.py.emit(index+1,"文件下载完成: " +i + f"路径: {p}")

    def download(self,url,name):
        root = os.getcwd()
        if self.savepath:
            root = os.path.join(self.savepath,name)
        else:
            root = os.path.join(root,name)
        for i in range(3):
            if os.path.isfile(root):
                self.kill(name)
                time.sleep(5)
                os.remove(root)
                self.ms.emit(f"{root} 文件已替换")
            else:
                with open(root,"wb") as fp:  
                    fp.write(requests.get(url).content)
                break
        return root
        
    def kill(self,app):
        ps = psutil.pids()
        for p in ps:
            try:
                if psutil.Process(p).name() == app:
                    psutil.Process(p).kill()
                    self.ms.emit(f"{psutil.Process(p).name()} 进程已结束")
            except psutil.NoSuchProcess as err:
                pass

class H(SimpleHTTPRequestHandler):

    def __init__(self,directory, *ar,**kw) -> None:
        self.directory = directory
        super().__init__(directory=self.directory,*ar,**kw)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = A()
    window.show()
    sys.exit(app.exec_())