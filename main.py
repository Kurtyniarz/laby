import sys

from PyQt5 import QtWidgets
from kalkulator import Ui_MainWindow


class CalcUi(QtWidgets.QMainWindow):
    def __init__(self):
        super(CalcUi, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.doClean.clicked.connect(lambda: self.doCleanInputs())
        self.ui.doCalc.clicked.connect(lambda: self.makeCalc())
        self.show()

    def doCleanInputs(self):
        self.ui.input_a.setText('')
        self.ui.input_b.setText('')
        self.ui.output.setText('')

    def makeCalc(self):
        a = float(self.ui.input_a.text())
        b = float(self.ui.input_b.text())
        try:
            if self.ui.check_dodaj.isChecked():
                calc = a + b
                self.ui.output.setText(str(calc))
            elif self.ui.check_odejmij.isChecked():
                calc = a - b
                self.ui.output.setText(str(calc))
            elif self.ui.check_mnoz.isChecked():
                calc = a * b
                self.ui.output.setText(str(calc))
            elif self.ui.check_dziel.isChecked():
                if b == 0.0 or b == 0 or b == '0':
                    self.ui.output.setText('Nie dziel przez 0!')
                else:
                    calc = a / b
                    self.ui.output.setText(str(calc))
        except error as e:
            print(e)


def main():
    App = QtWidgets.QApplication(sys.argv)
    AppUI = CalcUi()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
