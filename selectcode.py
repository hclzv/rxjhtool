# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerwRPcTU.ui'
##
## Created by: Qt User Interface Compiler version 5.15.5
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *  # type: ignore
from PyQt5.QtGui import *  # type: ignore
from PyQt5.QtWidgets import *  # type: ignore


class Ui_GroupBox(object):

    def __init__(self,number=None) -> None:
        self.number = number


    def setupUi(self, GroupBox):
        if not GroupBox.objectName():
            GroupBox.setObjectName(u"GroupBox")
        GroupBox.resize(905, 43)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GroupBox.sizePolicy().hasHeightForWidth())
        GroupBox.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(GroupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(GroupBox)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(GroupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_7 = QPushButton(GroupBox)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.horizontalLayout.addWidget(self.pushButton_7)

        self.pushButton_3 = QPushButton(GroupBox)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(GroupBox)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(GroupBox)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(GroupBox)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout.addWidget(self.pushButton_6)

        self.pushButton_8 = QPushButton(GroupBox)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.horizontalLayout.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(GroupBox)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.horizontalLayout.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(GroupBox)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.horizontalLayout.addWidget(self.pushButton_10)

        self.pushButton_11 = QPushButton(GroupBox)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.horizontalLayout.addWidget(self.pushButton_11)


        self.retranslateUi(GroupBox)

        QMetaObject.connectSlotsByName(GroupBox)
    # setupUi

    def retranslateUi(self, GroupBox):
        GroupBox.setWindowTitle(QCoreApplication.translate("GroupBox", u"GroupBox", None))
        self.pushButton.setText(QCoreApplication.translate("GroupBox", u"10", None))
        self.pushButton_2.setText(QCoreApplication.translate("GroupBox", u"50", None))
        self.pushButton_7.setText(QCoreApplication.translate("GroupBox", u"100", None))
        self.pushButton_3.setText(QCoreApplication.translate("GroupBox", u"150", None))
        self.pushButton_4.setText(QCoreApplication.translate("GroupBox", u"30", None))
        self.pushButton_5.setText(QCoreApplication.translate("GroupBox", u"80", None))
        self.pushButton_6.setText(QCoreApplication.translate("GroupBox", u"130", None))
        self.pushButton_8.setText(QCoreApplication.translate("GroupBox", u"180", None))
        self.pushButton_9.setText(QCoreApplication.translate("GroupBox", u"300", None))
        self.pushButton_10.setText(QCoreApplication.translate("GroupBox", u"230", None))
        self.pushButton_11.setText(QCoreApplication.translate("GroupBox", u"200", None))
    # retranslateUi
        self.setckecked()

    def setckecked(self):
        numbersBtns = [self.pushButton,
         self.pushButton_2,
         self.pushButton_7,
         self.pushButton_3,
         self.pushButton_4,
         self.pushButton_5,
         self.pushButton_6,
         self.pushButton_8,
         self.pushButton_9,
         self.pushButton_10,
         self.pushButton_11]

        for btn in numbersBtns:
            btn.clicked.connect(lambda clicked,btn=btn:self.setnumber(btn))

    def setnumber(self,btn:QPushButton):
        self.number = btn.text()
        