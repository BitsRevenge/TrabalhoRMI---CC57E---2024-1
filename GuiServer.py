# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GuiServer.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(706, 416)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 0, 691, 371))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(170, 20, 54, 17))
        self.label.setObjectName("label")
        self.lista_grupos = QtWidgets.QListWidget(self.page)
        self.lista_grupos.setGeometry(QtCore.QRect(160, 50, 111, 121))
        self.lista_grupos.setObjectName("lista_grupos")
        self.label_11 = QtWidgets.QLabel(self.page)
        self.label_11.setGeometry(QtCore.QRect(0, 10, 144, 361))
        self.label_11.setMaximumSize(QtCore.QSize(144, 400))
        self.label_11.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_16 = QtWidgets.QLabel(self.page)
        self.label_16.setGeometry(QtCore.QRect(140, 10, 531, 361))
        self.label_16.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.label_18 = QtWidgets.QLabel(self.page)
        self.label_18.setGeometry(QtCore.QRect(0, 190, 144, 61))
        self.label_18.setMaximumSize(QtCore.QSize(144, 400))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_18.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.label_20 = QtWidgets.QLabel(self.page)
        self.label_20.setGeometry(QtCore.QRect(0, 310, 144, 61))
        self.label_20.setMaximumSize(QtCore.QSize(144, 400))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_20.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_20.setText("")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.page)
        self.label_21.setGeometry(QtCore.QRect(0, 250, 144, 61))
        self.label_21.setMaximumSize(QtCore.QSize(144, 400))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_21.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_21.setText("")
        self.label_21.setObjectName("label_21")
        self.label_19 = QtWidgets.QLabel(self.page)
        self.label_19.setGeometry(QtCore.QRect(0, 70, 144, 61))
        self.label_19.setMaximumSize(QtCore.QSize(144, 400))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_19.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);")
        self.label_19.setObjectName("label_19")
        self.gruponame = QtWidgets.QLineEdit(self.page)
        self.gruponame.setGeometry(QtCore.QRect(400, 90, 200, 25))
        self.gruponame.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.gruponame.setFont(font)
        self.gruponame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.gruponame.setText("")
        self.gruponame.setObjectName("gruponame")
        self.label_27 = QtWidgets.QLabel(self.page)
        self.label_27.setGeometry(QtCore.QRect(323, 90, 61, 20))
        self.label_27.setObjectName("label_27")
        self.bt_criargrupo = QtWidgets.QPushButton(self.page)
        self.bt_criargrupo.setGeometry(QtCore.QRect(420, 140, 80, 25))
        self.bt_criargrupo.setMaximumSize(QtCore.QSize(80, 25))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(28, 198, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 198, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 198, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 198, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 198, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 198, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 198, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 198, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 198, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.bt_criargrupo.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(10)
        font.setItalic(True)
        self.bt_criargrupo.setFont(font)
        self.bt_criargrupo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bt_criargrupo.setObjectName("bt_criargrupo")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(440, 70, 81, 17))
        self.label_2.setObjectName("label_2")
        self.ir_config = QtWidgets.QPushButton(self.page)
        self.ir_config.setGeometry(QtCore.QRect(0, 10, 145, 61))
        self.ir_config.setMaximumSize(QtCore.QSize(145, 100))
        self.ir_config.setObjectName("ir_config")
        self.lista_onlines = QtWidgets.QListWidget(self.page)
        self.lista_onlines.setGeometry(QtCore.QRect(220, 220, 151, 141))
        self.lista_onlines.setObjectName("lista_onlines")
        self.label_5 = QtWidgets.QLabel(self.page)
        self.label_5.setGeometry(QtCore.QRect(230, 190, 111, 17))
        self.label_5.setObjectName("label_5")
        self.lista_banidos = QtWidgets.QListWidget(self.page)
        self.lista_banidos.setGeometry(QtCore.QRect(440, 220, 151, 141))
        self.lista_banidos.setObjectName("lista_banidos")
        self.label_13 = QtWidgets.QLabel(self.page)
        self.label_13.setGeometry(QtCore.QRect(450, 190, 111, 17))
        self.label_13.setObjectName("label_13")
        self.label_11.raise_()
        self.label_16.raise_()
        self.label_20.raise_()
        self.label_18.raise_()
        self.label.raise_()
        self.lista_grupos.raise_()
        self.label_21.raise_()
        self.label_19.raise_()
        self.gruponame.raise_()
        self.label_27.raise_()
        self.bt_criargrupo.raise_()
        self.label_2.raise_()
        self.ir_config.raise_()
        self.lista_onlines.raise_()
        self.label_5.raise_()
        self.lista_banidos.raise_()
        self.label_13.raise_()
        self.stackedWidget.addWidget(self.page)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_46 = QtWidgets.QLabel(self.page_3)
        self.label_46.setGeometry(QtCore.QRect(0, 120, 144, 61))
        self.label_46.setMaximumSize(QtCore.QSize(144, 400))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_46.setFont(font)
        self.label_46.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_46.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);")
        self.label_46.setObjectName("label_46")
        self.label_47 = QtWidgets.QLabel(self.page_3)
        self.label_47.setGeometry(QtCore.QRect(0, 240, 144, 61))
        self.label_47.setMaximumSize(QtCore.QSize(144, 400))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_47.setFont(font)
        self.label_47.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_47.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_47.setText("")
        self.label_47.setObjectName("label_47")
        self.label_48 = QtWidgets.QLabel(self.page_3)
        self.label_48.setGeometry(QtCore.QRect(0, 180, 144, 61))
        self.label_48.setMaximumSize(QtCore.QSize(144, 400))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_48.setFont(font)
        self.label_48.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_48.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_48.setText("")
        self.label_48.setObjectName("label_48")
        self.label_49 = QtWidgets.QLabel(self.page_3)
        self.label_49.setGeometry(QtCore.QRect(140, 0, 531, 361))
        self.label_49.setStyleSheet("background-color: rgb(255, 255, 255);;")
        self.label_49.setText("")
        self.label_49.setObjectName("label_49")
        self.label_51 = QtWidgets.QLabel(self.page_3)
        self.label_51.setGeometry(QtCore.QRect(0, 300, 144, 61))
        self.label_51.setMaximumSize(QtCore.QSize(144, 400))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_51.setFont(font)
        self.label_51.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_51.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_51.setText("")
        self.label_51.setObjectName("label_51")
        self.label_3 = QtWidgets.QLabel(self.page_3)
        self.label_3.setGeometry(QtCore.QRect(190, 30, 54, 17))
        self.label_3.setObjectName("label_3")
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(28, 198, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 198, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 198, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 198, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 198, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 198, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 198, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 198, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 198, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(10)
        font.setItalic(True)

        self.ir_config_2 = QtWidgets.QPushButton(self.page_3)
        self.ir_config_2.setGeometry(QtCore.QRect(0, 0, 145, 61))
        self.ir_config_2.setMaximumSize(QtCore.QSize(145, 100))
        self.ir_config_2.setObjectName("ir_config_2")
        self.ir_grupos_2 = QtWidgets.QPushButton(self.page_3)
        self.ir_grupos_2.setGeometry(QtCore.QRect(0, 60, 145, 61))
        self.ir_grupos_2.setMaximumSize(QtCore.QSize(145, 100))
        self.ir_grupos_2.setObjectName("ir_grupos_2")
        self.label_49.raise_()
        self.label_51.raise_()
        self.label_48.raise_()
        self.label_47.raise_()
        self.label_46.raise_()
        self.label_3.raise_()
        self.ir_config_2.raise_()
        self.ir_grupos_2.raise_()
        self.stackedWidget.addWidget(self.page_3)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.lobby_port = QtWidgets.QLineEdit(self.page_2)
        self.lobby_port.setGeometry(QtCore.QRect(370, 160, 200, 25))
        self.lobby_port.setMaximumSize(QtCore.QSize(200, 25))
        self.lobby_port.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lobby_port.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lobby_port.setObjectName("lobby_port")
        self.bt_start = QtWidgets.QPushButton(self.page_2)
        self.bt_start.setGeometry(QtCore.QRect(320, 250, 80, 25))
        self.bt_start.setMaximumSize(QtCore.QSize(80, 25))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(28, 198, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 198, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 198, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 198, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 198, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 198, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 198, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 198, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 198, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.bt_start.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(10)
        font.setItalic(True)
        self.bt_start.setFont(font)
        self.bt_start.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bt_start.setObjectName("bt_start")
        self.ir_grupos = QtWidgets.QPushButton(self.page_2)
        self.ir_grupos.setGeometry(QtCore.QRect(0, 70, 145, 61))
        self.ir_grupos.setMaximumSize(QtCore.QSize(145, 100))
        self.ir_grupos.setObjectName("ir_grupos")
        self.server = QtWidgets.QLineEdit(self.page_2)
        self.server.setGeometry(QtCore.QRect(370, 120, 200, 25))
        self.server.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.server.setFont(font)
        self.server.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.server.setObjectName("server")
        self.label_warning = QtWidgets.QLabel(self.page_2)
        self.label_warning.setGeometry(QtCore.QRect(230, 60, 271, 20))
        self.label_warning.setMaximumSize(QtCore.QSize(271, 20))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_warning.setFont(font)
        self.label_warning.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_warning.setText("")
        self.label_warning.setObjectName("label_warning")
        self.label_6 = QtWidgets.QLabel(self.page_2)
        self.label_6.setGeometry(QtCore.QRect(260, 50, 331, 271))
        self.label_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.page_2)
        self.label_7.setGeometry(QtCore.QRect(260, 80, 331, 251))
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_4 = QtWidgets.QLabel(self.page_2)
        self.label_4.setGeometry(QtCore.QRect(260, 60, 261, 21))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_8 = QtWidgets.QLabel(self.page_2)
        self.label_8.setGeometry(QtCore.QRect(0, 10, 144, 361))
        self.label_8.setMaximumSize(QtCore.QSize(144, 400))
        self.label_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.page_2)
        self.label_9.setGeometry(QtCore.QRect(140, 10, 531, 361))
        self.label_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.page_2)
        self.label_10.setGeometry(QtCore.QRect(0, 10, 144, 61))
        self.label_10.setMaximumSize(QtCore.QSize(144, 400))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_10.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")
        self.label_42 = QtWidgets.QLabel(self.page_2)
        self.label_42.setGeometry(QtCore.QRect(0, 250, 144, 61))
        self.label_42.setMaximumSize(QtCore.QSize(144, 400))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_42.setFont(font)
        self.label_42.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_42.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_42.setText("")
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(self.page_2)
        self.label_43.setGeometry(QtCore.QRect(0, 190, 144, 61))
        self.label_43.setMaximumSize(QtCore.QSize(144, 400))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_43.setFont(font)
        self.label_43.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_43.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_43.setText("")
        self.label_43.setObjectName("label_43")
        self.label_44 = QtWidgets.QLabel(self.page_2)
        self.label_44.setGeometry(QtCore.QRect(0, 310, 144, 61))
        self.label_44.setMaximumSize(QtCore.QSize(144, 400))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_44.setFont(font)
        self.label_44.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_44.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_44.setText("")
        self.label_44.setObjectName("label_44")
        self.label_12 = QtWidgets.QLabel(self.page_2)
        self.label_12.setGeometry(QtCore.QRect(293, 120, 61, 20))
        self.label_12.setObjectName("label_12")
        self.label_14 = QtWidgets.QLabel(self.page_2)
        self.label_14.setGeometry(QtCore.QRect(300, 160, 54, 17))
        self.label_14.setObjectName("label_14")
        self.port = QtWidgets.QLineEdit(self.page_2)
        self.port.setGeometry(QtCore.QRect(370, 200, 200, 25))
        self.port.setMaximumSize(QtCore.QSize(200, 25))
        self.port.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.port.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.port.setObjectName("port")
        self.label_22 = QtWidgets.QLabel(self.page_2)
        self.label_22.setGeometry(QtCore.QRect(300, 200, 54, 17))
        self.label_22.setObjectName("label_22")

        self.bt_parar = QtWidgets.QPushButton(self.page_2)
        self.bt_parar.setGeometry(QtCore.QRect(450, 250, 80, 25))
        self.bt_parar.setMaximumSize(QtCore.QSize(80, 25))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(28, 198, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 198, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 198, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 198, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 198, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 198, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 198, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 198, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 198, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.bt_parar.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(10)
        font.setItalic(True)
        self.bt_parar.setFont(font)
        self.bt_parar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bt_parar.setObjectName("bt_parar")
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.lobby_port.raise_()
        self.bt_start.raise_()
        self.ir_grupos.raise_()
        self.server.raise_()
        self.label_warning.raise_()
        self.label_4.raise_()
        self.label_10.raise_()
        self.label_42.raise_()
        self.label_43.raise_()
        self.label_44.raise_()
        self.label_12.raise_()
        self.label_14.raise_()
        self.port.raise_()
        self.label_22.raise_()
        self.bt_parar.raise_()
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 706, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Grupos"))
        self.label_19.setText(_translate("MainWindow", "      Grupos"))
        self.gruponame.setAccessibleDescription(_translate("MainWindow", "User"))
        self.gruponame.setPlaceholderText(_translate("MainWindow", "user"))
        self.label_27.setText(_translate("MainWindow", "Nome:"))
        self.bt_criargrupo.setText(_translate("MainWindow", "Criar"))
        self.label_2.setText(_translate("MainWindow", "Criar grupo"))
        self.ir_config.setText(_translate("MainWindow", "Config"))
        self.label_5.setText(_translate("MainWindow", "Usuarios Online"))
        self.label_13.setText(_translate("MainWindow", "Usuarios Banidos"))
        self.ir_config_2.setText(_translate("MainWindow", "Config"))
        self.ir_grupos_2.setText(_translate("MainWindow", "Grupos"))
        self.lobby_port.setText(_translate("MainWindow", "25501"))
        self.bt_start.setText(_translate("MainWindow", "Iniciar"))
        self.ir_grupos.setText(_translate("MainWindow", "Grupos"))
        self.server.setAccessibleDescription(_translate("MainWindow", "User"))
        self.server.setText(_translate("MainWindow", "127.0.0.1"))
        self.server.setPlaceholderText(_translate("MainWindow", "user"))
        self.label_4.setText(_translate("MainWindow", "                   Configurações"))
        self.label_10.setText(_translate("MainWindow", "       Config"))
        self.label_12.setText(_translate("MainWindow", "Hostname:"))
        self.label_14.setText(_translate("MainWindow", "RMI-Port:"))
        self.port.setText(_translate("MainWindow", "25500"))
        self.label_22.setText(_translate("MainWindow", "TCP-Port:"))
        self.bt_parar.setText(_translate("MainWindow", "Parar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

