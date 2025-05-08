from PyQt5 import QtCore,QtGui,QtWidgets,uic
import sys
from rxjhToolMainCode import Ui_Form
import pyodbc

class A(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.rxjhcode = Ui_Form()
        self.rxjhcode.setupUi(self)
        self.conn = None
        
        self.texts = []


        self.startConn()
        self.setSeceltLocal()
        self.querybbgallcommodity()
        self.singalsManager()


    def singalsManager(self):
        self.rxjhcode.comboBox.currentTextChanged.connect(lambda text : self.queryLocalcommodity(text))
        self.rxjhcode.pushButton_5.clicked.connect(lambda:
                                                   self.addlistview()
                                                   )

    def queryShangDan(self,name):
        if self.conn:
            self.listviewdata = []
            with self.conn.cursor() as cur:
                try:
                    cur.execute('''
                                SELECT t2.FLD_NAME, t2.FLD_DESC, t2.FLD_PID
                                FROM [wp2.0].dbo.TBL_XWWL_SELL AS t1
                                INNER JOIN [bbg2.0].dbo.ITEMSELL AS t2 ON t1.FLD_PID = t2.FLD_PID
                                WHERE t1.FLD_NPCNAME = ?;
                                ''',name)
                    rows = cur.fetchall() 
                    for row in rows:
                        self.listviewdata.append(row[0])
                    self.model = QtCore.QStringListModel(self.listviewdata) 
                    self.rxjhcode.listView.setModel(self.model)
                except Exception as e:
                    QtWidgets.QMessageBox.warning(self,"err",e.args.__str__())

    def startConn(self):
        try:
            self.conn_str = ( r'DRIVER={SQL Server};' r'SERVER=192.168.200.100;' r'DATABASE=he;' r'UID=saa;' r'PWD=sa;')
            self.conn = pyodbc.connect(self.conn_str)
            self.rxjhcode.comboBox_2.setEnabled(True)
            self.rxjhcode.comboBox.setEnabled(True)
            self.rxjhcode.pushButton_5.setEnabled(True)
        except pyodbc.OperationalError as e:
            QtWidgets.QMessageBox.warning(self,"err",e.args.__str__())
        except Exception as e:
            QtWidgets.QMessageBox.warning(self,"err","not error"+" "+e.args.__str__())

    #所有商店NPC名称
    def setSeceltLocal(self):
        sql = '''SELECT FLD_NPCNAME FROM [wp2.0].dbo.TBL_XWWL_SELL'''
        if not self.conn:
            self.startConn()
        else:
            with self.conn.cursor() as cur:
                try:
                    items = []
                    cur.execute(sql)
                    rows = cur.fetchall() 
                    for row in rows:
                        if row[0] not in items:
                            items.append(row[0])
                    self.rxjhcode.comboBox.addItems(items)
                except Exception as e:
                    print(e.args)



    def queryLocalcommodity(self,name):
        if not self.conn:
            self.startConn()
            self.queryLocalcommodity(name=name)
        else:
            with self.conn.cursor() as cur:
                try:
                    curitmes = {}
                    cur.execute("{CALL getSelfCommodityName (?)}",name)
                    # cur.execute("{CALL GetAllNpcCommodity (?)}",name)
                    rows = cur.fetchall() 
                    self.rxjhcode.tableWidget_2.clear()
                    for i,v in enumerate(rows):
                        curitmes.update({v[-1]:v})
                    self.rxjhcode.tableWidget_2.setRowCount(len(curitmes)) 
                    self.rxjhcode.tableWidget_2.setColumnCount(v.__len__()) 
                    for row,(key,values) in enumerate(curitmes.items()):
                        for column,value in enumerate(values): 
                            self.rxjhcode.tableWidget_2.setItem(row,column,QtWidgets.QTableWidgetItem(str(value)))     
                    curitmes.clear()
                    pass
                except Exception as e:
                    QtWidgets.QMessageBox.warning(self,"err",e.args.__str__())

    def querybbgallcommodity(self):
        alls = []
        if self.conn:
            with self.conn.cursor() as cur:
                try:
                    cur.execute('''select * from [bbg2.0].[dbo].ITEMSELL''')
                    datas = cur.fetchall()
                    for data in datas:
                        alls.append(data[2]+" | "+str(data[3]))
                    self.rxjhcode.comboBox_2.addItems(alls)
                except Exception as err:
                    self.conn.rollback()
                    print("err:",err)
                finally:
                    self.conn.commit()
        else:
            self.startConn()
            self.querybbgallcommodity()

    def addlistview(self):
        text = self.rxjhcode.comboBox_2.currentText()
        text = text.split(" | ")
        
        if text[0] not in self.texts:
            self.texts.append(text[0])
            self.listviewmodel =QtCore.QStringListModel(self.texts)
            self.rxjhcode.listView.setModel(self.listviewmodel)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = A()
    window.show()
    sys.exit(app.exec_())