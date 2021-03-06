# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(702, 702)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.cbb_file = QtWidgets.QComboBox(self.centralwidget)
        self.cbb_file.setMaximumSize(QtCore.QSize(16777215, 30))
        self.cbb_file.setObjectName("cbb_file")
        self.horizontalLayout.addWidget(self.cbb_file)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.cbb_papers = QtWidgets.QComboBox(self.centralwidget)
        self.cbb_papers.setMaximumSize(QtCore.QSize(16777215, 30))
        self.cbb_papers.setObjectName("cbb_papers")
        self.horizontalLayout.addWidget(self.cbb_papers)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.cbb_question_type = QtWidgets.QComboBox(self.centralwidget)
        self.cbb_question_type.setMaximumSize(QtCore.QSize(16777215, 30))
        self.cbb_question_type.setObjectName("cbb_question_type")
        self.horizontalLayout.addWidget(self.cbb_question_type)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.lb_title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lb_title.setFont(font)
        self.lb_title.setText("")
        self.lb_title.setObjectName("lb_title")
        self.verticalLayout.addWidget(self.lb_title)
        self.cb_A = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_A.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cb_A.setFont(font)
        self.cb_A.setObjectName("cb_A")
        self.verticalLayout.addWidget(self.cb_A)
        self.cb_B = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_B.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cb_B.setFont(font)
        self.cb_B.setObjectName("cb_B")
        self.verticalLayout.addWidget(self.cb_B)
        self.cb_C = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_C.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cb_C.setFont(font)
        self.cb_C.setObjectName("cb_C")
        self.verticalLayout.addWidget(self.cb_C)
        self.cb_D = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_D.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cb_D.setFont(font)
        self.cb_D.setObjectName("cb_D")
        self.verticalLayout.addWidget(self.cb_D)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_previous = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_previous.sizePolicy().hasHeightForWidth())
        self.btn_previous.setSizePolicy(sizePolicy)
        self.btn_previous.setMaximumSize(QtCore.QSize(16777215, 25))
        self.btn_previous.setObjectName("btn_previous")
        self.horizontalLayout_2.addWidget(self.btn_previous)
        self.btn_sure = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_sure.sizePolicy().hasHeightForWidth())
        self.btn_sure.setSizePolicy(sizePolicy)
        self.btn_sure.setMaximumSize(QtCore.QSize(16777215, 25))
        self.btn_sure.setObjectName("btn_sure")
        self.horizontalLayout_2.addWidget(self.btn_sure)
        self.btn_next = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_next.sizePolicy().hasHeightForWidth())
        self.btn_next.setSizePolicy(sizePolicy)
        self.btn_next.setMaximumSize(QtCore.QSize(16777215, 25))
        self.btn_next.setObjectName("btn_next")
        self.horizontalLayout_2.addWidget(self.btn_next)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setMaximumSize(QtCore.QSize(40, 25))
        self.lineEdit.setMaxLength(100)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.btn_jump = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_jump.sizePolicy().hasHeightForWidth())
        self.btn_jump.setSizePolicy(sizePolicy)
        self.btn_jump.setMaximumSize(QtCore.QSize(16777215, 25))
        self.btn_jump.setObjectName("btn_jump")
        self.horizontalLayout_2.addWidget(self.btn_jump)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.lb_answer = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_answer.sizePolicy().hasHeightForWidth())
        self.lb_answer.setSizePolicy(sizePolicy)
        self.lb_answer.setMaximumSize(QtCore.QSize(16777215, 15))
        self.lb_answer.setText("")
        self.lb_answer.setObjectName("lb_answer")
        self.verticalLayout.addWidget(self.lb_answer)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 702, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.btn_previous.clicked.connect(MainWindow.onPreviousClicked)
        self.btn_sure.clicked.connect(MainWindow.onSureClicked)
        self.btn_next.clicked.connect(MainWindow.onNextClicked)
        self.cbb_file.currentIndexChanged['QString'].connect(MainWindow.onFilesChanged)
        self.cbb_papers.currentIndexChanged['QString'].connect(MainWindow.onPapersChanged)
        self.cbb_question_type.currentIndexChanged['QString'].connect(MainWindow.onQuestionTypeChanged)
        self.btn_jump.clicked.connect(MainWindow.onJumpClicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "题库选择"))
        self.label.setText(_translate("MainWindow", "试卷选择"))
        self.label_2.setText(_translate("MainWindow", "题型选择"))
        self.cb_A.setText(_translate("MainWindow", "CheckBox"))
        self.cb_B.setText(_translate("MainWindow", "CheckBox"))
        self.cb_C.setText(_translate("MainWindow", "CheckBox"))
        self.cb_D.setText(_translate("MainWindow", "CheckBox"))
        self.btn_previous.setText(_translate("MainWindow", "上一题"))
        self.btn_sure.setText(_translate("MainWindow", "确定"))
        self.btn_next.setText(_translate("MainWindow", "下一题"))
        self.btn_jump.setText(_translate("MainWindow", "跳转"))
