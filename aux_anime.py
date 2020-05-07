from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtCore
import sys
from anime import *
class Anime(QMainWindow, Ui_MainWindow):
    def __init__(self,parent = None):
        super().__init__(parent)
        super().setupUi(self)
        self.Calcular.clicked.connect(self.dados_anime)
        self.Resultado.setDisabled(True)
        #hn = (self.Duracao - self.Resumo) * self.QuantiaEp
    def dados_anime(self):
        #self.Resultado.setText(self.QuantiaEp.text() + self.Duracao.text() + self.Resumo.text())
        #calculo = str(eval((self.Duracao.text() - self.Resumo.text()) * self.QuantiaEp.text()))
        duracao = int(self.Duracao.text())
        resumo = int(self.Resumo.text())
        quantia = int(self.QuantiaEp.text())
        calculo = (duracao - resumo) * quantia
        self.Resultado.setGeometry(QtCore.QRect(300, 70, 213, 201))
        self.Resultado.setText(str(calculo) + " min")
if __name__ == '__main__':
    qt = QApplication(sys.argv)
    new = Anime()
    new.show()
    qt.exec_()
