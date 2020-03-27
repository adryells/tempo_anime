# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'anime.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(523, 385)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../Imagens/botart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setStyleSheet("background-color: blue;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Calcular = QtWidgets.QPushButton(self.centralwidget)
        self.Calcular.setGeometry(QtCore.QRect(60, 220, 80, 25))
        self.Calcular.setObjectName("Calcular")
        self.AnimeName = QtWidgets.QLineEdit(self.centralwidget)
        self.AnimeName.setGeometry(QtCore.QRect(40, 60, 113, 25))
        self.AnimeName.setStyleSheet("background-color: orange;")
        self.AnimeName.setObjectName("AnimeName")
        self.QuantiaEp = QtWidgets.QLineEdit(self.centralwidget)
        self.QuantiaEp.setGeometry(QtCore.QRect(40, 100, 113, 25))
        self.QuantiaEp.setStyleSheet("background-color: orange;")
        self.QuantiaEp.setObjectName("QuantiaEp")
        self.Duracao = QtWidgets.QLineEdit(self.centralwidget)
        self.Duracao.setGeometry(QtCore.QRect(40, 140, 113, 25))
        self.Duracao.setStyleSheet("background-color: orange;")
        self.Duracao.setObjectName("Duracao")
        self.Resumo = QtWidgets.QLineEdit(self.centralwidget)
        self.Resumo.setGeometry(QtCore.QRect(40, 180, 113, 25))
        self.Resumo.setStyleSheet("background-color: orange;")
        self.Resumo.setObjectName("Resumo")
        self.Resultado = QtWidgets.QLineEdit(self.centralwidget)
        self.Resultado.setGeometry(QtCore.QRect(300, 70, 113, 101))
        self.Resultado.setStyleSheet("color: rgb(54,56,76); font-size: 40px;")
        self.Resultado.setText("")
        self.Resultado.setAlignment(QtCore.Qt.AlignCenter)
        self.Resultado.setObjectName("Resultado")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Anime Calc"))
        self.Calcular.setText(_translate("MainWindow", "Calcular"))
        self.AnimeName.setPlaceholderText(_translate("MainWindow", "Nome do Anime"))
        self.QuantiaEp.setPlaceholderText(_translate("MainWindow", "Quantidade-eps"))
        self.Duracao.setPlaceholderText(_translate("MainWindow", "Duracao"))
        self.Resumo.setPlaceholderText(_translate("MainWindow", "resumo se houver"))
        self.Resultado.setPlaceholderText(_translate("MainWindow", "?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

