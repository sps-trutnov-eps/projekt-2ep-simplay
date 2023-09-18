from PyQt5 import QtWidgets
import sys

aplikace = QtWidgets.QApplication(sys.argv)
formular = QtWidgets.QWidget()

formular.show()
sys.exit(aplikace.exec_())
