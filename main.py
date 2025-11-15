import uuid
import string
import pydirectinput
from PyQt5 import QtCore,QtGui,QtWidgets
import sys,datetime,os,time,subprocess,json,threading,psutil
import requests
from typing import List,Dict,Callable
from bs4 import BeautifulSoup
from socketserver import TCPServer,StreamRequestHandler
from http.server import SimpleHTTPRequestHandler,HTTPServer
from functools import partial
import sync
from urllib.parse import urljoin
import appsqlite
from selectcode import Ui_GroupBox
class A(QtWidgets.QWidget):
    clidata = QtCore.pyqtSignal(str)
    pyqtSignalsocket = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.mainUi = sync.Ui_Form()
        self.mainUi.setupUi(self)
        self.setWindowTitle("远程测试工具(P-j) v2024211")

        self.mainApp = None

        self.serverSoftwareList:List[str] = []
        self.curQWidgets:List[QtWidgets.QWidget] = []
        self.scrollAreaWidgetContentsVbox = QtWidgets.QVBoxLayout()
        self.names : List[str] = []
        self.chckes:List[QtWidgets.QCheckBox] = []
        self.radios:List[QtWidgets.QRadioButton] = []

        self.t = T(self.names,None,self.mainUi.comboBox.currentText(),self.mainUi.progressBar)
        self.t.finished.connect(self.tfinish)
        self.t.py.connect(self.setPrb)
        self.t.filelength.connect(self.setPrb1)
        self.clidata.connect(self.infoappend)
        self.clidata.connect(self.adroidEx) # android 
        self.pyqtSignalsocket.connect(self.livehostmanager)

        self.mainUi.scrollAreaWidgetContents.setLayout(self.scrollAreaWidgetContentsVbox)
        self.mainUi.pushButton.clicked.connect(self.init)
        self.mainUi.pushButton_3.clicked.connect(self.startApp)
        self.mainUi.pushButton_4.clicked.connect(self.tStart)
        # self.loadjson()
        self.sockets = []
        self.initlivehostmanager()
        self.clickedsManage()

        self.uiInit()
        QtCore.QTimer.singleShot(3000,self.apploaded)

    def apploaded(self):
        try:
            self.loadsqlite3()
            QtWidgets.QMessageBox.information(self,"数据库","历史数据库加载完成")
        except Exception as e:
            QtWidgets.QMessageBox.warning(self,"数据库",f"历史数据库错误: {e}")
    def init(self):
        self.getServerSoftware(self.mainUi.comboBox.currentText())

    def uiInit(self):
        mouseController = {self.mainUi.radioButton_doubleClick:"double",
                            self.mainUi.radioButton_click:"one",
                            self.mainUi.radioButton_down:"down",
                            self.mainUi.radioButton_up:"up",
                            self.mainUi.radioButton_left:"left",
                            self.mainUi.radioButton_right:"right",
                            self.mainUi.checkBox:"move",
                            self.mainUi.spinBox_3:"x",
                            self.mainUi.spinBox_4:"y"}
        self.listView_2_data = []
        self.pMaximun = 0
        self.keyRuns = ["click","press","rightClick","up","down","doubleClick","moveTo"]
        self.valueRuns:Dict[float,Dict] = {} #{1:{:}}
        self.listView_2_model = QtCore.QStringListModel(self.listView_2_data)
        fnkey = ['space','enter','tab','backspace','up','down','left','right','delete','insert']
        self.mainUi.lineEdit_2.setText(os.getcwd())
        self.mainUi.doubleSpinBox.setValue(5.00)
        self.mainUi.comboBox_2.addItems([f"f{i}" for i in range(1,13)])
        self.mainUi.comboBox_3.addItems([i.__str__() for i in range(10)])
        self.mainUi.comboBox_4.addItems([s for s in string.ascii_letters])
        self.mainUi.comboBox_5.addItems([s for s in string.punctuation])

        self.mainUi.comboBox_6.addItems([s for s in fnkey])

        def setlistView_2(press=None,clear:bool=False,moveTo:bool=False):
            if clear:
                if QtWidgets.QMessageBox.question(self,"清空","清空步骤?",QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No) == QtWidgets.QMessageBox.Yes:
                    self.listView_2_data.clear()
                    self.listView_2_model.setStringList(self.listView_2_data)
                    self.mainUi.listView_2.setModel(self.listView_2_model)
                    self.valueRuns.clear()
            else:
                if self.mainUi.radioButton_left.isChecked(): #鼠标左
                    text = mouseController.get(self.mainUi.radioButton_left)
                    self.valueRuns.update({uuid.uuid1():{"left":1}})
                    self.listView_2_model.setStringList(self.listView_2_data)
                    self.mainUi.listView_2.setModel(self.listView_2_model)
                    self.listView_2_data.append(text)
        
                elif self.mainUi.radioButton_right.isChecked(): #鼠标右
                    text = mouseController.get(self.mainUi.radioButton_right)
                    self.valueRuns.clear({uuid.uuid1():{"doubleClick":0}})
                    self.listView_2_model.setStringList(self.listView_2_data)
                    self.mainUi.listView_2.setModel(self.listView_2_model)
                    self.listView_2_data.append(text)

                elif moveTo: #鼠标移动
                    x = self.mainUi.spinBox_3.value().__str__() #x
                    y = self.mainUi.spinBox_4.value().__str__() #y
                    text = x+" , "+ y
                    self.listView_2_data.append(text)
                    self.valueRuns.update({uuid.uuid1():{"moveTo":[x,y]}})
                    self.listView_2_model.setStringList(self.listView_2_data)
                    self.mainUi.listView_2.setModel(self.listView_2_model)
            if press:
                self.listView_2_data.append(press)
                self.valueRuns.update({uuid.uuid1():{"press":press}})
                self.listView_2_model.setStringList(self.listView_2_data)
                self.mainUi.listView_2.setModel(self.listView_2_model)

        
        def lineEdit_3Text():
            for t in self.mainUi.lineEdit_3.text():
                self.listView_2_data.append(t)
                self.valueRuns.update({uuid.uuid1():{"press":t}})
                self.listView_2_model.setStringList(self.listView_2_data)
                self.mainUi.listView_2.setModel(self.listView_2_model)


        self.mainUi.pushButton_29.clicked.connect(lineEdit_3Text)
        self.mainUi.comboBox_2.textActivated.connect(lambda text:setlistView_2(text))
        self.mainUi.comboBox_3.textActivated.connect(lambda text:setlistView_2(text))
        self.mainUi.comboBox_4.textActivated.connect(lambda text:setlistView_2(text))
        self.mainUi.comboBox_5.textActivated.connect(lambda text:setlistView_2(text))
        self.mainUi.comboBox_6.textActivated.connect(lambda text:setlistView_2(text))

        self.mainUi.pushButton_24.clicked.connect(lambda clicked:setlistView_2(None,True)) #键盘输入

        self.mainUi.pushButton_17.clicked.connect(lambda clicked:setlistView_2()) #鼠标
        self.mainUi.pushButton_23.clicked.connect(lambda clicked:setlistView_2())
        self.mainUi.pushButton_27.clicked.connect(lambda clicked:setlistView_2(moveTo=True))

        def run():
            for index,data in self.valueRuns.items():
                if data.get("press"):
                    pydirectinput.press(data.get("press")) # 键盘输入
                elif data.get("click"):
                    pydirectinput.click()
                elif data.get("left"):
                    pydirectinput.click()
                elif data.get("rightClick"):
                    pydirectinput.rightClick() #鼠标左键单击一次
                elif data.get("up"):
                    pydirectinput.keyUp(data.get("up")) 
                elif data.get("down"):
                    pydirectinput.keyDown(data.get("down"))
                elif data.get("doubleClick"):
                    pydirectinput.doubleClick()
                elif data.get("moveTo"):
                    pydirectinput.moveTo(int(data.get("moveTo")[0]),int(data.get("moveTo")[1]))
                time.sleep(self.mainUi.doubleSpinBox_2.value())
            self.infoappend(f"完成数据: {data.values()} 的执行")

        def startRun():
            time.sleep(self.mainUi.doubleSpinBox.value())
            for i in range(self.mainUi.spinBox_2.value()):
                run()
            QtWidgets.QMessageBox.information(self,"成功","运行完成")
            

        def getposition():
            def getp():
                QtWidgets.QMessageBox.information(self,"成功","当前鼠标位置\n"+pydirectinput.position().__str__())
                self.infoappend(pydirectinput.position().__str__())
            QtCore.QTimer.singleShot(3000,getp)

        self.mainUi.pushButton_15.clicked.connect(lambda:self.startQTimter(startRun)) #开始
        self.mainUi.pushButton_16.clicked.connect(getposition) #获取鼠标位置

    def loadsqlite3(self):
        self.sql3 = appsqlite.Sql()
        self.sql3.createtab()
        r = self.sql3.query()
        if r != []:
            for i in r:
                self.infoappend(mes=i[-1],time=i[-2],appLoader=True)
                
    def clickedsManage(self):
        self.mainUi.pushButton_10.clicked.connect(lambda:subprocess.run(f"explorer {self.mainUi.lineEdit_2.text()}"))
        self.mainUi.lineEdit_2.textChanged.connect(lambda text:self.mainUi.pushButton_10.setEnabled(True) if os.path.isdir(text) else self.mainUi.pushButton_10.setEnabled(False))
        def setrul(text):
            self.t.url = text
        self.mainUi.comboBox.currentTextChanged.connect(lambda text:setrul(text))
        self.mainUi.pushButton_8.clicked.connect(self.httpStart)
        self.mainUi.pushButton_9.clicked.connect(self.httpStop)
        self.mainUi.pushButton_6.clicked.connect(lambda :self.startQTimter(self.sockerServerStart))
        self.mainUi.pushButton_11.clicked.connect(lambda:self.startQTimter(self.sockerServerStop))
        self.mainUi.pushButton_22.clicked.connect(lambda clicked,btn=self.mainUi.pushButton_22 :self.startControl(btn))
        self.mainUi.pushButton_21.clicked.connect(lambda clicked,btn=self.mainUi.pushButton_21 :self.startControl(btn))
        self.mainUi.pushButton_30.clicked.connect(lambda clicked:self.setint1())

        def clear():
            [c.setChecked(False) for c in self.chckes]
            [c1.setChecked(False) for c1 in self.radios]
            self.mainUi.label_3.setText("未设置启动程序")
            self.names.clear()
            self.listView_2_data.clear()
            self.listView_2_model.setStringList(self.listView_2_data)
            self.mainUi.listView_2.setModel(self.listView_2_model)

        self.mainUi.pushButtonclear.clicked.connect(clear)


    def setint1(self):
        a = Ui_GroupBox()
        show = QtWidgets.QDialog()
        a.setupUi(show)
        show.exec_()
        if a.number:
            self.mainUi.spinBox_2.setValue(int(a.number))

    def sockerServerStart(self):
        self.sockerRun = None

        self.tcpServer = TCPServer(("",self.mainUi.spinBox.value()),S)
        self.tcpServer.a = self # 
        if not self.sockerRun:
            th = threading.Thread(target=self.tcpServer.serve_forever)
            th.start()
            self.sockerRun = True
            self.mainUi.pushButton_11.setEnabled(True)
            self.mainUi.pushButton_6.setEnabled(False)
            self.infoappend("服务器已启动")

    def sockerServerStop(self):
        if self.sockerRun:
            self.tcpServer.shutdown()
            self.mainUi.pushButton_11.setEnabled(False)
            self.mainUi.pushButton_6.setEnabled(True)
            self.infoappend("服务器已停止")

    def tfinish(self):
        self.mainUi.progressBar.setValue(0)
        self.mainUi.progressBar.setHidden(True)
        self.mainUi.pushButton_4.setToolTip("下载完成 ")
        if self.names:
            self.mainUi.pushButton_4.setEnabled(True)
            self.mainUi.pushButton_3.setEnabled(True)

    def httpinit(self):
        httpdirectory = self.mainUi.lineEdit_4.text()
        self.hsv_is_run = False
        if httpdirectory.__len__() <1 and not os.path.isdir(httpdirectory):
            httpdirectory = os.getcwd()
        self.hsv = HTTPServer(("",8000),partial(H,httpdirectory))

    def httpStart(self):
        self.httpinit()
        if not self.hsv_is_run:
            self.hsvTh = threading.Thread(target=self.hsv.serve_forever)
            self.hsvTh.start()
            self.mainUi.label_4.setText("http服务运行中..http://0.0.0.0:8000")
            self.infoappend("http服务器已启动 http://0.0.0.0:8000")
            self.hsv_is_run = True

    def httpStop(self):
        if self.hsv_is_run: 
            self.hsv.shutdown()
            self.hsvTh.join()
            self.mainUi.label_4.setText("http服务未运行")
            self.infoappend("http服务器已停止")
            self.hsv_is_run = False

    def loadjson(self):
        file = os.path.isfile("jsons/server.json")
        if file:
            with open("jsons/server.json") as fp:
                data:Dict = json.load(fp)
            self.mainUi.comboBox.addItems([url for url in data.values()])
        else:
            QtWidgets.QMessageBox(self,"文件错误","jsons/server.json 文件错误或不存在")

    def tStart(self):
        self.mainUi.progressBar.setMaximum(self.names.__len__())
        if not self.t.isRunning() and self.names.__len__() >= 1:
            self.mainUi.widget_4.setHidden(False)
            self.mainUi.progressBar.setHidden(False)
            self.t.url = self.mainUi.comboBox.currentText()
            self.t.savepath = self.mainUi.lineEdit_2.text()
            self.t.start()
            self.mainUi.pushButton_4.setEnabled(False)
            self.mainUi.pushButton_3.setEnabled(False)
            self.mainUi.pushButton_4.setToolTip("下载中..."+datetime.datetime.now().strftime('%Y-%m-%d-%H_%M_%S'))

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        if self.t.isRunning():
            self.t.terminate()
        
    def startApp(self):
        self.tStart()
        def start(startPath=None):
            if os.path.isfile(startPath):
                subprocess.run(f'''{startPath}''')
                self.infoappend(f"{startPath} 已启动")
        
        def f():
            root = os.getcwd()
            if self.mainApp:
                app = self.mainApp
                app = str(app).lstrip().rstrip()
                root = self.mainUi.lineEdit_2.text().__len__()
                if root != 0:
                    startPath =  os.path.join(self.mainUi.lineEdit_2.text(),app)
                else:
                    startPath = os.path.join(os.getcwd(),app)
                if startPath:
                        t = threading.Thread(target=start,args=(startPath,))
                        t.start()
        self.t.finished.connect(f)

    def setPrb(self,int,str):
        self.mainUi.progressBar.setValue(int)
        self.infoappend(mes=str)

    def setPrb1(self,int):
        self.mainUi.progressBar.setValue(int)

    def adroidEx(self,mes:str):
        time.sleep(self.mainUi.doubleSpinBox.value())

        def start(mes=None):
            for m in mes:
                pydirectinput.press(m)
                time.sleep(self.mainUi.doubleSpinBox_2.value())
            pydirectinput.press("1")
            pydirectinput.press("enter")
            self.infoappend("android 数据接收执行完成"+f" : {mes}")
            QtWidgets.QMessageBox.information(self,"完成",f"Android {mes} 数据执行完成")
        try:
            item = json.loads(mes) 
            d = item.get("android-move")
            if d:
                start(d)
        except ValueError as err:
            start(mes=mes)

    def infoappend(self,mes,time=None,showQme=False,appLoader=False):
        if appLoader:
            pass
        else:
            self.sql3.inster(messages=mes)
        if time:
            self.mainUi.textEdit.insertPlainText(f"T: {time} :{mes} \n")
        else:
            self.mainUi.textEdit.insertPlainText(f"T: {datetime.datetime.now().strftime('%Y-%m-%d-%H_%M_%S')} :{mes} \n")
        if showQme:
            QtWidgets.QMessageBox.information(self,"完成",f"{mes}运行成功")
    
    def livehostmanager(self,host:str):
        if host not in self.sockets:
            self.sockets.append(host)
            self.socketsModel.setStringList(self.sockets)

    def initlivehostmanager(self):
        self.socketsModel = QtCore.QStringListModel(self.sockets)
        self.socketsModel.setStringList(self.sockets)
        self.mainUi.listView.setModel(self.socketsModel)

    def getServerSoftware(self,url):
        self.infoappend("刷新成功")
        try:

            text =  requests.get(url,timeout=2).text
            soup = BeautifulSoup(text, 'html.parser')
            li_elements = soup.find_all('li')
            li_texts = [li.text for li in li_elements]
            for li in li_texts:
                self.serverSoftwareList.append(li)
        except requests.exceptions.ConnectionError as her:
            self.infoappend(her.__str__())
            QtWidgets.QMessageBox.warning(self,"网络错误",her.__str__())
        except Exception as err:
            self.infoappend(err.__str__())
            QtWidgets.QMessageBox.warning(self,"网络错误",err.__str__())
    

        
        def added(c:QtWidgets.QCheckBox,name:str):
            if c.isChecked() and name not in self.names:
                self.names.append(name.lstrip().rstrip())
            elif name in self.names:
                self.names.remove(name.lstrip().rstrip())

            if self.names:
                self.mainUi.pushButton_4.setEnabled(True)
            else:
                self.mainUi.pushButton_4.setEnabled(False)
        
        def radidck(c:QtWidgets.QRadioButton,cke:QtWidgets.QCheckBox,name:str):
            if c.isChecked():
                mainApp = c.text()[11:]
                self.mainUi.label_3.setText(f"启动程序: {mainApp} ")
                self.mainApp = mainApp
                self.mainUi.pushButton_4.setEnabled(True)
                self.mainUi.pushButton_3.setEnabled(True)
                cke.setChecked(True)
            else:
                self.mainUi.label_3.setText(f"未设置启动程序")
                self.mainApp = None

        for ii,i in enumerate(self.serverSoftwareList):
            curBtn = QtWidgets.QPushButton(f"下载 (下载)")
            curCheck = QtWidgets.QCheckBox(f"文件:{ii} : {i}")
            maincurCheck = QtWidgets.QRadioButton(f"设置程序为入口{ii} : {i}")
            
            self.chckes.append(curCheck)
            self.radios.append(maincurCheck)
            curCheck.clicked.connect(lambda b,cc=curCheck,name=i:added(cc,name))
            maincurCheck.clicked.connect(lambda c,ria=maincurCheck,cke=curCheck,name=i:radidck(ria,cke,name))
            curHox = QtWidgets.QHBoxLayout()
            curHox.addWidget(maincurCheck)
            curHox.addWidget(curCheck)
            curHox.addWidget(curBtn)
            self.curQWidgets.append(curHox)
            self.scrollAreaWidgetContentsVbox.addLayout(curHox)

    def startControl(self,btn:QtWidgets.QPushButton):
        time.sleep(self.mainUi.doubleSpinBox.value())
        enter = self.mainUi.checkBox_2
        objName2 = "pushButton_22" #2
        objName1 = "pushButton_21" # 3
        file = os.path.isfile("jsons/login.json")
        if file:
            with open("jsons/login.json") as fp:
                data:Dict = json.load(fp)
                def start(text:str):
                    for t in text:
                        time.sleep(self.mainUi.doubleSpinBox_2.value())
                        pydirectinput.press(t)
                    if enter.isChecked():
                        pydirectinput.press("enter")
                if btn.objectName() == objName2:
                    start(data.get("user1"))
                    start(data.get("pass1"))
                    self.infoappend("用户密码:user2 输入完成",True)
                if btn.objectName() == objName1:

                    start(data.get("user"))
                    start(data.get("pass"))
                    self.infoappend("用户密码:user1 输入完成",True)
        else:
            QtWidgets.QMessageBox(self,"文件错误"," jsons/login.json 错误 或不存在")

    def startQTimter(self,fn:Callable):
        QtCore.QTimer.singleShot(1000,fn)

class S(StreamRequestHandler):

    clients = []
    def handle(self) -> None:
        a:A = self.server.a
        b = self.rfile.readline()
        if b: 
            cliectdata = b.decode()
            a.clidata.emit(cliectdata)

class T(QtCore.QThread):
    py = QtCore.pyqtSignal([int,str])
    ms = QtCore.pyqtSignal(str)
    filelength = QtCore.pyqtSignal(int)

    def __init__(self,ls:List[str],savepath=None,url=None,p:QtWidgets.QProgressBar=None):
        super().__init__()    
        self.ls = ls
        self.savepath = savepath
        self.url = url
        self.p = p

    def run(self) -> None:
        for index,i in enumerate(self.ls):
            dlurl = self.url+"/"+i
            try:
                p = self.download(dlurl,i)
                self.py.emit(index+1,"文件下载完成: " +i + f"路径: {p}")
            except Exception as err:
                strerr = f"err: {err.__str__()}| url: {dlurl} | 保存路径: {i}"
                self.py.emit(index+1,strerr)
                

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
                size = requests.head(url).headers.get('Content-Length', 0)
                self.p.setMaximum(int(size))
                with open(root,"wb") as fp:
                    sn = 0
                    r = requests.get(url,stream=True)
                    for cent in r.iter_content(102400):
                        if cent:
                            fp.write(cent)
                            sn = len(cent)+sn 
                            self.filelength.emit(sn)
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