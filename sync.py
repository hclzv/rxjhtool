# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'syncuiHMXApy.ui'
##
## Created by: Qt User Interface Compiler version 5.15.5
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
        Form.resize(923, 524)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_15 = QHBoxLayout(Form)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.widget_4 = QWidget(Form)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout = QVBoxLayout(self.widget_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.widget_4)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_12 = QHBoxLayout(self.tab)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.groupBox_4 = QGroupBox(self.tab)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy2)
        self.groupBox_4.setCheckable(False)
        self.groupBox_4.setChecked(False)
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.groupBox_9 = QGroupBox(self.groupBox_4)
        self.groupBox_9.setObjectName(u"groupBox_9")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox_9.sizePolicy().hasHeightForWidth())
        self.groupBox_9.setSizePolicy(sizePolicy3)
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_9)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.widget_6 = QWidget(self.groupBox_9)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lineEdit = QLineEdit(self.widget_6)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_8.addWidget(self.lineEdit)

        self.pushButton_5 = QPushButton(self.widget_6)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy4)

        self.horizontalLayout_8.addWidget(self.pushButton_5)


        self.verticalLayout_8.addWidget(self.widget_6)

        self.scrollArea_2 = QScrollArea(self.groupBox_9)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy5)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 230, 332))
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_8.addWidget(self.scrollArea_2)


        self.horizontalLayout_6.addWidget(self.groupBox_9)

        self.groupBox_5 = QGroupBox(self.groupBox_4)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setEnabled(True)
        sizePolicy.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox_7 = QGroupBox(self.groupBox_5)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setEnabled(True)
        sizePolicy.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy)
        self.groupBox_7.setCheckable(False)
        self.groupBox_7.setChecked(False)
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.widget_5 = QWidget(self.groupBox_7)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy6)
        self.horizontalLayout_7 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_8 = QLabel(self.widget_5)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_7.addWidget(self.label_8)

        self.label_5 = QLabel(self.widget_5)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_7.addWidget(self.label_5)

        self.spinBox = QSpinBox(self.widget_5)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimum(2000)
        self.spinBox.setMaximum(10000)
        self.spinBox.setSingleStep(1)

        self.horizontalLayout_7.addWidget(self.spinBox)

        self.pushButton_6 = QPushButton(self.widget_5)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout_7.addWidget(self.pushButton_6)

        self.pushButton_11 = QPushButton(self.widget_5)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setEnabled(False)

        self.horizontalLayout_7.addWidget(self.pushButton_11)

        self.line_2 = QFrame(self.widget_5)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_7.addWidget(self.line_2)

        self.checkBox_15 = QCheckBox(self.widget_5)
        self.checkBox_15.setObjectName(u"checkBox_15")

        self.horizontalLayout_7.addWidget(self.checkBox_15)


        self.verticalLayout_7.addWidget(self.widget_5)

        self.groupBox_8 = QGroupBox(self.groupBox_7)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setEnabled(True)
        sizePolicy.setHeightForWidth(self.groupBox_8.sizePolicy().hasHeightForWidth())
        self.groupBox_8.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.groupBox_8)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_12 = QPushButton(self.groupBox_8)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setEnabled(False)
        sizePolicy5.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy5)
        self.pushButton_12.setCheckable(True)

        self.gridLayout.addWidget(self.pushButton_12, 0, 1, 1, 1)

        self.pushButton_7 = QPushButton(self.groupBox_8)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy3)
        self.pushButton_7.setCheckable(True)

        self.gridLayout.addWidget(self.pushButton_7, 0, 0, 1, 1)

        self.pushButton_13 = QPushButton(self.groupBox_8)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setEnabled(False)
        sizePolicy5.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy5)
        self.pushButton_13.setCheckable(True)

        self.gridLayout.addWidget(self.pushButton_13, 1, 0, 1, 1)

        self.pushButton_14 = QPushButton(self.groupBox_8)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setEnabled(False)
        sizePolicy5.setHeightForWidth(self.pushButton_14.sizePolicy().hasHeightForWidth())
        self.pushButton_14.setSizePolicy(sizePolicy5)
        self.pushButton_14.setCheckable(True)

        self.gridLayout.addWidget(self.pushButton_14, 1, 1, 1, 1)


        self.verticalLayout_7.addWidget(self.groupBox_8)


        self.verticalLayout_4.addWidget(self.groupBox_7)

        self.groupBox_6 = QGroupBox(self.groupBox_5)
        self.groupBox_6.setObjectName(u"groupBox_6")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy7)
        self.groupBox_6.setCheckable(True)
        self.groupBox_6.setChecked(False)
        self.horizontalLayout_10 = QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.widget_8 = QWidget(self.groupBox_6)
        self.widget_8.setObjectName(u"widget_8")
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy8)
        self.verticalLayout_6 = QVBoxLayout(self.widget_8)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_4 = QLabel(self.widget_8)
        self.label_4.setObjectName(u"label_4")
        sizePolicy7.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy7)

        self.verticalLayout_6.addWidget(self.label_4)

        self.lineEdit_4 = QLineEdit(self.widget_8)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        sizePolicy7.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy7)

        self.verticalLayout_6.addWidget(self.lineEdit_4)


        self.horizontalLayout_10.addWidget(self.widget_8)

        self.widget_9 = QWidget(self.groupBox_6)
        self.widget_9.setObjectName(u"widget_9")
        sizePolicy9 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.MinimumExpanding)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy9)
        self.verticalLayout_5 = QVBoxLayout(self.widget_9)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.pushButton_9 = QPushButton(self.widget_9)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy6.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy6)

        self.verticalLayout_5.addWidget(self.pushButton_9)

        self.pushButton_8 = QPushButton(self.widget_9)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy6.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy6)

        self.verticalLayout_5.addWidget(self.pushButton_8)


        self.horizontalLayout_10.addWidget(self.widget_9)


        self.verticalLayout_4.addWidget(self.groupBox_6)


        self.horizontalLayout_6.addWidget(self.groupBox_5)

        self.groupBox_3 = QGroupBox(self.groupBox_4)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.scrollArea_3 = QScrollArea(self.groupBox_3)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 91, 362))
        self.verticalLayout_10 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.listView = QListView(self.scrollAreaWidgetContents_3)
        self.listView.setObjectName(u"listView")

        self.verticalLayout_10.addWidget(self.listView)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.horizontalLayout_2.addWidget(self.scrollArea_3)


        self.horizontalLayout_6.addWidget(self.groupBox_3)


        self.horizontalLayout_12.addWidget(self.groupBox_4)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_13 = QVBoxLayout(self.tab_2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.widget_2 = QWidget(self.tab_2)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(self.widget_2)
        self.widget.setObjectName(u"widget")
        sizePolicy10 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy10)
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        sizePolicy6.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy6)

        self.horizontalLayout.addWidget(self.label)

        self.comboBox = QComboBox(self.widget)
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy11 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy11)

        self.horizontalLayout.addWidget(self.comboBox)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy6.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy6)

        self.horizontalLayout.addWidget(self.pushButton)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy6.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy6)

        self.horizontalLayout.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy10.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy10)

        self.horizontalLayout.addWidget(self.lineEdit_2)

        self.pushButton_10 = QPushButton(self.widget)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setEnabled(False)

        self.horizontalLayout.addWidget(self.pushButton_10)

        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        sizePolicy6.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy6)
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)


        self.verticalLayout_2.addWidget(self.widget)

        self.groupBox = QGroupBox(self.widget_2)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scrollArea = QScrollArea(self.groupBox)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy12 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy12)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 823, 299))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)

        self.widget_3 = QWidget(self.groupBox)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy7.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy7)
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButtonclear = QPushButton(self.widget_3)
        self.pushButtonclear.setObjectName(u"pushButtonclear")

        self.horizontalLayout_3.addWidget(self.pushButtonclear)

        self.line_3 = QFrame(self.widget_3)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_3)

        self.label_3 = QLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.pushButton_4 = QPushButton(self.widget_3)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.pushButton_4)

        self.pushButton_3 = QPushButton(self.widget_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.widget_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.pushButton_2)


        self.verticalLayout_3.addWidget(self.widget_3, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.groupBox)


        self.verticalLayout_13.addWidget(self.widget_2)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.horizontalLayout_9 = QHBoxLayout(self.tab_3)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.groupBox_2 = QGroupBox(self.tab_3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy13 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy13)
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.textEdit = QTextEdit(self.groupBox_2)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy14 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy14.setHorizontalStretch(0)
        sizePolicy14.setVerticalStretch(0)
        sizePolicy14.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy14)

        self.horizontalLayout_4.addWidget(self.textEdit)


        self.horizontalLayout_9.addWidget(self.groupBox_2)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_12 = QVBoxLayout(self.tab_4)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.progressBar = QProgressBar(self.tab_4)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.verticalLayout_12.addWidget(self.progressBar)

        self.groupBox_17 = QGroupBox(self.tab_4)
        self.groupBox_17.setObjectName(u"groupBox_17")
        sizePolicy.setHeightForWidth(self.groupBox_17.sizePolicy().hasHeightForWidth())
        self.groupBox_17.setSizePolicy(sizePolicy)
        self.horizontalLayout_11 = QHBoxLayout(self.groupBox_17)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_18 = QLabel(self.groupBox_17)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_11.addWidget(self.label_18)

        self.doubleSpinBox = QDoubleSpinBox(self.groupBox_17)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setMinimum(2.000000000000000)
        self.doubleSpinBox.setValue(2.000000000000000)

        self.horizontalLayout_11.addWidget(self.doubleSpinBox)

        self.line_8 = QFrame(self.groupBox_17)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.VLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_11.addWidget(self.line_8)

        self.label_7 = QLabel(self.groupBox_17)
        self.label_7.setObjectName(u"label_7")
        sizePolicy3.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy3)

        self.horizontalLayout_11.addWidget(self.label_7)

        self.doubleSpinBox_2 = QDoubleSpinBox(self.groupBox_17)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")
        self.doubleSpinBox_2.setMinimum(0.010000000000000)
        self.doubleSpinBox_2.setMaximum(10.000000000000000)
        self.doubleSpinBox_2.setSingleStep(0.100000000000000)
        self.doubleSpinBox_2.setValue(0.010000000000000)

        self.horizontalLayout_11.addWidget(self.doubleSpinBox_2)

        self.line_5 = QFrame(self.groupBox_17)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_11.addWidget(self.line_5)

        self.label_9 = QLabel(self.groupBox_17)
        self.label_9.setObjectName(u"label_9")
        sizePolicy15 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy15.setHorizontalStretch(0)
        sizePolicy15.setVerticalStretch(0)
        sizePolicy15.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy15)

        self.horizontalLayout_11.addWidget(self.label_9)

        self.pushButton_30 = QPushButton(self.groupBox_17)
        self.pushButton_30.setObjectName(u"pushButton_30")

        self.horizontalLayout_11.addWidget(self.pushButton_30)

        self.spinBox_2 = QSpinBox(self.groupBox_17)
        self.spinBox_2.setObjectName(u"spinBox_2")
        sizePolicy7.setHeightForWidth(self.spinBox_2.sizePolicy().hasHeightForWidth())
        self.spinBox_2.setSizePolicy(sizePolicy7)
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setMaximum(9999)

        self.horizontalLayout_11.addWidget(self.spinBox_2)

        self.line_7 = QFrame(self.groupBox_17)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_11.addWidget(self.line_7)

        self.pushButton_16 = QPushButton(self.groupBox_17)
        self.pushButton_16.setObjectName(u"pushButton_16")
        sizePolicy3.setHeightForWidth(self.pushButton_16.sizePolicy().hasHeightForWidth())
        self.pushButton_16.setSizePolicy(sizePolicy3)

        self.horizontalLayout_11.addWidget(self.pushButton_16)

        self.pushButton_15 = QPushButton(self.groupBox_17)
        self.pushButton_15.setObjectName(u"pushButton_15")
        sizePolicy3.setHeightForWidth(self.pushButton_15.sizePolicy().hasHeightForWidth())
        self.pushButton_15.setSizePolicy(sizePolicy3)

        self.horizontalLayout_11.addWidget(self.pushButton_15)


        self.verticalLayout_12.addWidget(self.groupBox_17)

        self.groupBox_13 = QGroupBox(self.tab_4)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_13)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.groupBox_23 = QGroupBox(self.groupBox_13)
        self.groupBox_23.setObjectName(u"groupBox_23")
        self.verticalLayout_18 = QVBoxLayout(self.groupBox_23)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.tabWidget_2 = QTabWidget(self.groupBox_23)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setMinimumSize(QSize(0, 261))
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.horizontalLayout_14 = QHBoxLayout(self.tab_5)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.groupBox_18 = QGroupBox(self.tab_5)
        self.groupBox_18.setObjectName(u"groupBox_18")
        self.verticalLayout_20 = QVBoxLayout(self.groupBox_18)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.widget_12 = QWidget(self.groupBox_18)
        self.widget_12.setObjectName(u"widget_12")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_14 = QLabel(self.widget_12)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_13.addWidget(self.label_14)

        self.comboBox_2 = QComboBox(self.widget_12)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_13.addWidget(self.comboBox_2)


        self.verticalLayout_20.addWidget(self.widget_12)

        self.widget_14 = QWidget(self.groupBox_18)
        self.widget_14.setObjectName(u"widget_14")
        self.horizontalLayout_18 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_10 = QLabel(self.widget_14)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_18.addWidget(self.label_10)

        self.comboBox_3 = QComboBox(self.widget_14)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.horizontalLayout_18.addWidget(self.comboBox_3)


        self.verticalLayout_20.addWidget(self.widget_14)

        self.widget_15 = QWidget(self.groupBox_18)
        self.widget_15.setObjectName(u"widget_15")
        self.horizontalLayout_21 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_11 = QLabel(self.widget_15)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_21.addWidget(self.label_11)

        self.comboBox_4 = QComboBox(self.widget_15)
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.horizontalLayout_21.addWidget(self.comboBox_4)


        self.verticalLayout_20.addWidget(self.widget_15)

        self.widget_16 = QWidget(self.groupBox_18)
        self.widget_16.setObjectName(u"widget_16")
        self.horizontalLayout_22 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_12 = QLabel(self.widget_16)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_22.addWidget(self.label_12)

        self.comboBox_5 = QComboBox(self.widget_16)
        self.comboBox_5.setObjectName(u"comboBox_5")

        self.horizontalLayout_22.addWidget(self.comboBox_5)


        self.verticalLayout_20.addWidget(self.widget_16)

        self.widget_17 = QWidget(self.groupBox_18)
        self.widget_17.setObjectName(u"widget_17")
        self.horizontalLayout_23 = QHBoxLayout(self.widget_17)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_13 = QLabel(self.widget_17)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_23.addWidget(self.label_13)

        self.comboBox_6 = QComboBox(self.widget_17)
        self.comboBox_6.setObjectName(u"comboBox_6")

        self.horizontalLayout_23.addWidget(self.comboBox_6)


        self.verticalLayout_20.addWidget(self.widget_17)


        self.horizontalLayout_14.addWidget(self.groupBox_18)

        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.horizontalLayout_27 = QHBoxLayout(self.tab_6)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.groupBox_25 = QGroupBox(self.tab_6)
        self.groupBox_25.setObjectName(u"groupBox_25")
        self.verticalLayout_19 = QVBoxLayout(self.groupBox_25)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.widget_18 = QWidget(self.groupBox_25)
        self.widget_18.setObjectName(u"widget_18")
        self.horizontalLayout_25 = QHBoxLayout(self.widget_18)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.radioButton_doubleClick = QRadioButton(self.widget_18)
        self.radioButton_doubleClick.setObjectName(u"radioButton_doubleClick")

        self.horizontalLayout_25.addWidget(self.radioButton_doubleClick)

        self.radioButton_click = QRadioButton(self.widget_18)
        self.radioButton_click.setObjectName(u"radioButton_click")

        self.horizontalLayout_25.addWidget(self.radioButton_click)

        self.radioButton_5 = QRadioButton(self.widget_18)
        self.radioButton_5.setObjectName(u"radioButton_5")

        self.horizontalLayout_25.addWidget(self.radioButton_5)

        self.radioButton_6 = QRadioButton(self.widget_18)
        self.radioButton_6.setObjectName(u"radioButton_6")

        self.horizontalLayout_25.addWidget(self.radioButton_6)


        self.verticalLayout_19.addWidget(self.widget_18, 0, Qt.AlignTop)

        self.widget_11 = QWidget(self.groupBox_25)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_24 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_15 = QLabel(self.widget_11)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_24.addWidget(self.label_15)

        self.radioButton_left = QRadioButton(self.widget_11)
        self.radioButton_left.setObjectName(u"radioButton_left")

        self.horizontalLayout_24.addWidget(self.radioButton_left)

        self.radioButton_right = QRadioButton(self.widget_11)
        self.radioButton_right.setObjectName(u"radioButton_right")

        self.horizontalLayout_24.addWidget(self.radioButton_right)


        self.verticalLayout_19.addWidget(self.widget_11, 0, Qt.AlignTop)

        self.pushButton_17 = QPushButton(self.groupBox_25)
        self.pushButton_17.setObjectName(u"pushButton_17")

        self.verticalLayout_19.addWidget(self.pushButton_17)

        self.line_6 = QFrame(self.groupBox_25)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_19.addWidget(self.line_6)

        self.widget_19 = QWidget(self.groupBox_25)
        self.widget_19.setObjectName(u"widget_19")
        self.horizontalLayout_26 = QHBoxLayout(self.widget_19)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.checkBox = QCheckBox(self.widget_19)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout_26.addWidget(self.checkBox)

        self.label_16 = QLabel(self.widget_19)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_26.addWidget(self.label_16)

        self.spinBox_3 = QSpinBox(self.widget_19)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setMaximum(9999)

        self.horizontalLayout_26.addWidget(self.spinBox_3)

        self.label_17 = QLabel(self.widget_19)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_26.addWidget(self.label_17)

        self.spinBox_4 = QSpinBox(self.widget_19)
        self.spinBox_4.setObjectName(u"spinBox_4")
        self.spinBox_4.setMaximum(9999)

        self.horizontalLayout_26.addWidget(self.spinBox_4)


        self.verticalLayout_19.addWidget(self.widget_19)

        self.pushButton_27 = QPushButton(self.groupBox_25)
        self.pushButton_27.setObjectName(u"pushButton_27")

        self.verticalLayout_19.addWidget(self.pushButton_27)


        self.horizontalLayout_27.addWidget(self.groupBox_25, 0, Qt.AlignTop)

        self.tabWidget_2.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.horizontalLayout_28 = QHBoxLayout(self.tab_7)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.groupBox_24 = QGroupBox(self.tab_7)
        self.groupBox_24.setObjectName(u"groupBox_24")
        self.gridLayout_2 = QGridLayout(self.groupBox_24)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget_10 = QWidget(self.groupBox_24)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_19 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.radioButton_up = QRadioButton(self.widget_10)
        self.radioButton_up.setObjectName(u"radioButton_up")

        self.horizontalLayout_19.addWidget(self.radioButton_up)

        self.radioButton_down = QRadioButton(self.widget_10)
        self.radioButton_down.setObjectName(u"radioButton_down")

        self.horizontalLayout_19.addWidget(self.radioButton_down)


        self.gridLayout_2.addWidget(self.widget_10, 0, 0, 1, 1, Qt.AlignTop)

        self.pushButton_23 = QPushButton(self.groupBox_24)
        self.pushButton_23.setObjectName(u"pushButton_23")

        self.gridLayout_2.addWidget(self.pushButton_23, 8, 0, 1, 1, Qt.AlignTop)

        self.pushButton_28 = QPushButton(self.groupBox_24)
        self.pushButton_28.setObjectName(u"pushButton_28")
        self.pushButton_28.setCheckable(True)

        self.gridLayout_2.addWidget(self.pushButton_28, 3, 0, 1, 1, Qt.AlignTop)

        self.pushButton_25 = QPushButton(self.groupBox_24)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setCheckable(True)

        self.gridLayout_2.addWidget(self.pushButton_25, 2, 0, 1, 1, Qt.AlignTop)

        self.line_4 = QFrame(self.groupBox_24)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_4, 7, 0, 1, 1, Qt.AlignTop)

        self.pushButton_26 = QPushButton(self.groupBox_24)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setCheckable(True)

        self.gridLayout_2.addWidget(self.pushButton_26, 6, 0, 1, 1, Qt.AlignTop)


        self.horizontalLayout_28.addWidget(self.groupBox_24)

        self.tabWidget_2.addTab(self.tab_7, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.horizontalLayout_29 = QHBoxLayout(self.tab_8)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.groupBox_16 = QGroupBox(self.tab_8)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.verticalLayout_22 = QVBoxLayout(self.groupBox_16)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.widget_13 = QWidget(self.groupBox_16)
        self.widget_13.setObjectName(u"widget_13")
        self.horizontalLayout_16 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.lineEdit_3 = QLineEdit(self.widget_13)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_16.addWidget(self.lineEdit_3)

        self.pushButton_29 = QPushButton(self.widget_13)
        self.pushButton_29.setObjectName(u"pushButton_29")

        self.horizontalLayout_16.addWidget(self.pushButton_29)


        self.verticalLayout_22.addWidget(self.widget_13, 0, Qt.AlignTop)

        self.widget_20 = QWidget(self.groupBox_16)
        self.widget_20.setObjectName(u"widget_20")
        self.verticalLayout_21 = QVBoxLayout(self.widget_20)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.pushButton_21 = QPushButton(self.widget_20)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setCheckable(False)

        self.verticalLayout_21.addWidget(self.pushButton_21)

        self.pushButton_22 = QPushButton(self.widget_20)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setCheckable(False)

        self.verticalLayout_21.addWidget(self.pushButton_22)

        self.checkBox_2 = QCheckBox(self.widget_20)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setMinimumSize(QSize(215, 0))

        self.verticalLayout_21.addWidget(self.checkBox_2)


        self.verticalLayout_22.addWidget(self.widget_20, 0, Qt.AlignTop)


        self.horizontalLayout_29.addWidget(self.groupBox_16, 0, Qt.AlignTop)

        self.tabWidget_2.addTab(self.tab_8, "")

        self.verticalLayout_18.addWidget(self.tabWidget_2, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_5.addWidget(self.groupBox_23, 0, Qt.AlignRight)

        self.groupBox_10 = QGroupBox(self.groupBox_13)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.verticalLayout_15 = QVBoxLayout(self.groupBox_10)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.widget_7 = QWidget(self.groupBox_10)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_17 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.pushButton_18 = QPushButton(self.widget_7)
        self.pushButton_18.setObjectName(u"pushButton_18")

        self.horizontalLayout_17.addWidget(self.pushButton_18)

        self.pushButton_19 = QPushButton(self.widget_7)
        self.pushButton_19.setObjectName(u"pushButton_19")

        self.horizontalLayout_17.addWidget(self.pushButton_19)

        self.pushButton_20 = QPushButton(self.widget_7)
        self.pushButton_20.setObjectName(u"pushButton_20")

        self.horizontalLayout_17.addWidget(self.pushButton_20)

        self.pushButton_24 = QPushButton(self.widget_7)
        self.pushButton_24.setObjectName(u"pushButton_24")

        self.horizontalLayout_17.addWidget(self.pushButton_24)


        self.verticalLayout_15.addWidget(self.widget_7)

        self.tabWidget_3 = QTabWidget(self.groupBox_10)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.horizontalLayout_30 = QHBoxLayout(self.tab_9)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.listView_2 = QListView(self.tab_9)
        self.listView_2.setObjectName(u"listView_2")
        self.listView_2.setMinimumSize(QSize(336, 0))

        self.horizontalLayout_30.addWidget(self.listView_2)

        self.tabWidget_3.addTab(self.tab_9, "")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.horizontalLayout_31 = QHBoxLayout(self.tab_10)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.listView_3 = QListView(self.tab_10)
        self.listView_3.setObjectName(u"listView_3")

        self.horizontalLayout_31.addWidget(self.listView_3)

        self.tabWidget_3.addTab(self.tab_10, "")

        self.verticalLayout_15.addWidget(self.tabWidget_3)


        self.horizontalLayout_5.addWidget(self.groupBox_10)


        self.verticalLayout_12.addWidget(self.groupBox_13)

        self.tabWidget.addTab(self.tab_4, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.horizontalLayout_15.addWidget(self.widget_4)


        self.retranslateUi(Form)
        self.checkBox_15.clicked.connect(self.groupBox_3.setVisible)

        self.tabWidget.setCurrentIndex(3)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Form", u"\u8f85\u52a9\u529f\u80fd", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("Form", u"\u9009\u62e9\u6587\u4ef6", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u9ed8\u8ba4\u76ee\u5f55", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u76ee\u5f55", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Form", u"\u670d\u52a1\u5668", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("Form", u"C/S\u7aef", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u670d\u52a1\u5668: ", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u7aef\u53e3\u53f7: ", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"\u542f\u52a8\u670d\u52a1\u5668", None))
        self.pushButton_11.setText(QCoreApplication.translate("Form", u"\u505c\u6b62", None))
        self.checkBox_15.setText(QCoreApplication.translate("Form", u"\u5728\u7ebf\u4e3b\u673a", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("Form", u"\u6d4b\u8bd5\u63a7\u5236", None))
        self.pushButton_12.setText(QCoreApplication.translate("Form", u"\u6d4b\u8bd52(192.168.1.2)", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"\u6d4b\u8bd51(192.168.1.1)", None))
        self.pushButton_13.setText(QCoreApplication.translate("Form", u"\u6d4b\u8bd53(192.168.1.3)", None))
        self.pushButton_14.setText(QCoreApplication.translate("Form", u"\u6d4b\u8bd54(192.168.1.4)", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("Form", u"HTTP\u670d\u52a1\u5668", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("Form", u"\u679a\u4e3e\u7684\u8def\u5f84:\u4f8b\u5982c: \u9ed8\u8ba4\u5f53\u524d\u76ee\u5f55", None))
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"\u505c\u6b62", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"\u542f\u52a8", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"\u5728\u7ebf\u4e3b\u673a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"\u8fdc\u7a0b\u6d4b\u8bd5", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u670d\u52a1\u5668\u5730\u5740:", None))
#if QT_CONFIG(tooltip)
        self.pushButton.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>\u5237\u65b0\u8fde\u63a5\u5de6\u4fa7\u670d\u52a1\u5668</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u4e0b\u8f7d\u5217\u8868", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u4fdd\u5b58\u76ee\u5f55:", None))
        self.lineEdit_2.setText(QCoreApplication.translate("Form", u"C:\\Users\\john\\Desktop", None))
        self.pushButton_10.setText(QCoreApplication.translate("Form", u"\u6253\u5f00\u4fdd\u5b58\u76ee\u5f55", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u670d\u52a1\u5668\u6587\u4ef6", None))
        self.pushButtonclear.setText(QCoreApplication.translate("Form", u"\u6e05\u7a7a\u9009\u4e2d", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u8bf7\u8bbe\u7f6e\u542f\u52a8\u7a0b\u5e8f", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"\u4e0b\u8f7d\u9009\u4e2d", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u4e0b\u8f7d\u5e76\u4e3b\u7a0b\u5e8f(\u5165\u53e3)", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u505c\u6b62", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"\u540c\u6b65\u6587\u4ef6", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"\u4fe1\u606f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Form", u"\u4fe1\u606f", None))
        self.groupBox_17.setTitle(QCoreApplication.translate("Form", u"\u521d\u59cb\u5316", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"\u521d\u59cb\u5316\u7b49\u5f85\u65f6\u95f4", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u63a7\u5236\u64cd\u4f5c\u5ef6\u65f6", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u6b21\u6570: ", None))
        self.pushButton_30.setText(QCoreApplication.translate("Form", u"\u6570\u5b57\u8303\u56f4", None))
        self.pushButton_16.setText(QCoreApplication.translate("Form", u"\u83b7\u53d6\u9f20\u6807\u4f4d\u7f6e", None))
        self.pushButton_15.setText(QCoreApplication.translate("Form", u"\u542f\u52a8(\u8bf7\u5207\u6362\u82f1\u6587)", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("Form", u"\u63a7\u5236", None))
        self.groupBox_23.setTitle(QCoreApplication.translate("Form", u"\u8f93\u5165", None))
        self.groupBox_18.setTitle(QCoreApplication.translate("Form", u"Fn\u952e", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"F1-F12:", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"\u6570\u5b57\u952e:", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"\u82f1\u6587\u5b57\u6bcd:", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"\u7b26\u53f7:", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"\u5176\u4ed6", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("Form", u"\u952e\u76d8\u5b57\u7b26", None))
        self.groupBox_25.setTitle(QCoreApplication.translate("Form", u"\u9f20\u6807\u63a7\u5236", None))
        self.radioButton_doubleClick.setText(QCoreApplication.translate("Form", u"\u53cc", None))
        self.radioButton_click.setText(QCoreApplication.translate("Form", u"\u5355", None))
        self.radioButton_5.setText(QCoreApplication.translate("Form", u"\u6309", None))
        self.radioButton_6.setText(QCoreApplication.translate("Form", u"\u62ac", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"\u70b9\u51fb:", None))
        self.radioButton_left.setText(QCoreApplication.translate("Form", u"\u5de6", None))
        self.radioButton_right.setText(QCoreApplication.translate("Form", u"\u53f3", None))
        self.pushButton_17.setText(QCoreApplication.translate("Form", u"\u6dfb\u52a0\u9f20\u6807\u52a8\u4f5c", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"\u79fb\u52a8", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"\u79fb\u52a8\u5230:", None))
        self.label_17.setText(QCoreApplication.translate("Form", u",", None))
        self.pushButton_27.setText(QCoreApplication.translate("Form", u"\u6dfb\u52a0\u79fb\u52a8\u5750\u6807", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), QCoreApplication.translate("Form", u"\u9f20\u6807\u8f93\u5165", None))
        self.groupBox_24.setTitle(QCoreApplication.translate("Form", u"\u63a7\u5236\u952e", None))
        self.radioButton_up.setText(QCoreApplication.translate("Form", u"\u62ac\u8d77", None))
        self.radioButton_down.setText(QCoreApplication.translate("Form", u"\u6309\u4e0b", None))
        self.pushButton_23.setText(QCoreApplication.translate("Form", u"\u6dfb\u52a0\u63a7\u5236", None))
        self.pushButton_28.setText(QCoreApplication.translate("Form", u"alt", None))
        self.pushButton_25.setText(QCoreApplication.translate("Form", u"crtl", None))
        self.pushButton_26.setText(QCoreApplication.translate("Form", u"shift", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), QCoreApplication.translate("Form", u"\u63a7\u5236\u952e", None))
        self.groupBox_16.setTitle(QCoreApplication.translate("Form", u"\u6587\u8f93\u5165", None))
        self.pushButton_29.setText(QCoreApplication.translate("Form", u"\u6dfb\u52a0", None))
        self.pushButton_21.setText(QCoreApplication.translate("Form", u"\u7528\u6237\u5bc6\u7801\u8f93\u51651(\u8bf7\u5207\u6362\u82f1\u6587\u8f93\u5165\u6cd5)", None))
        self.pushButton_22.setText(QCoreApplication.translate("Form", u"\u7528\u6237\u5bc6\u7801\u8f93\u51652(\u8bf7\u5207\u6362\u82f1\u6587\u8f93\u5165\u6cd5)", None))
        self.checkBox_2.setText(QCoreApplication.translate("Form", u"\u56de\u8f66", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), QCoreApplication.translate("Form", u"\u6587\u672c\u8f93\u5165", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("Form", u"\u73b0\u5728", None))
        self.pushButton_18.setText(QCoreApplication.translate("Form", u"\u5220\u9664", None))
        self.pushButton_19.setText(QCoreApplication.translate("Form", u"\u4e0a\u79fb", None))
        self.pushButton_20.setText(QCoreApplication.translate("Form", u"\u4e0b\u79fb", None))
        self.pushButton_24.setText(QCoreApplication.translate("Form", u"\u6e05\u7a7a", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_9), QCoreApplication.translate("Form", u"\u73b0\u5728", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_10), QCoreApplication.translate("Form", u"\u5386\u53f2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("Form", u"\u81ea\u52a8\u5316\u63a7\u5236", None))
    # retranslateUi

