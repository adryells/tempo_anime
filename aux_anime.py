from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
from anime import *
class Anime(QMainWindow, Ui_MainWindow):
    def __init__(self,parent = None):
        super().__init__(parent)
        super().setupUi(self)
        self.Calcular.clicked.connect(self.dados_anime)
        self.Resultado.setDisabled(True)
        hn = (self.Duracao - self.Resumo) * self.QuantiaEp
        return hn
    def dados_anime(self):
        self.Resultado.setText('a')
if __name__ == '__main__':
    qt = QApplication(sys.argv)
    new = Anime()
    new.show()
    qt.exec_()
