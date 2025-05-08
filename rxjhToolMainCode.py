# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designermqLfgv.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *  # type: ignore
from PyQt5.QtGui import *  # type: ignore
from PyQt5.QtWidgets import *  # type: ignore


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(809, 418)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_5 = QGroupBox(Form)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_7 = QPushButton(self.groupBox_5)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.pushButton_7)

        self.label = QLabel(self.groupBox_5)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.label)

        self.comboBox = QComboBox(self.groupBox_5)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.comboBox)

        self.line = QFrame(self.groupBox_5)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.label_2 = QLabel(self.groupBox_5)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.label_2)

        self.comboBox_2 = QComboBox(self.groupBox_5)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.comboBox_2)

        self.pushButton_5 = QPushButton(self.groupBox_5)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.pushButton_5)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addWidget(self.groupBox_5)

        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox = QGroupBox(self.groupBox_2)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.listView = QListView(self.groupBox)
        self.listView.setObjectName(u"listView")
        self.listView.setDragDropMode(QAbstractItemView.DragDrop)
        self.listView.setDefaultDropAction(Qt.MoveAction)

        self.horizontalLayout_3.addWidget(self.listView)


        self.horizontalLayout_2.addWidget(self.groupBox)

        self.groupBox_3 = QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout = QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton = QPushButton(self.groupBox_3)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_3 = QPushButton(self.groupBox_3)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.groupBox_3)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout.addWidget(self.pushButton_4)

        self.pushButton_2 = QPushButton(self.groupBox_3)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout.addWidget(self.pushButton_2)


        self.horizontalLayout_2.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.groupBox_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.tableWidget_2 = QTableWidget(self.groupBox_4)
        if (self.tableWidget_2.columnCount() < 3):
            self.tableWidget_2.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setDragDropMode(QAbstractItemView.DragDrop)
        self.tableWidget_2.setDefaultDropAction(Qt.MoveAction)

        self.horizontalLayout_4.addWidget(self.tableWidget_2)


        self.horizontalLayout_2.addWidget(self.groupBox_4)


        self.verticalLayout_2.addWidget(self.groupBox_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Form", u"GroupBox", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"\u767b\u5f55", None))
        self.label.setText(QCoreApplication.translate("Form", u"NPC:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"\u5e73\u5341\u6307", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"\u5200\u5251\u7b11", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"\u91d1\u9999\u7389", None))

        self.label_2.setText(QCoreApplication.translate("Form", u"\u88c5\u5907: ", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"\u6dfb\u52a0\u88c5\u5907", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"GroupBox", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u672a\u6dfb\u52a0\u88c5\u5907", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"\u4fee\u6539", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u6e05\u7a7a<-", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"<-", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"\u5237\u65b0", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u5e94\u7528", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Form", u"\u5546\u5e97\u73b0\u6709\u88c5\u5907", None))
        ___qtablewidgetitem = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"\u540d\u79f0", None));
        ___qtablewidgetitem2 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"\u5546\u5e97\u4f4d\u7f6e", None));
    # retranslateUi

