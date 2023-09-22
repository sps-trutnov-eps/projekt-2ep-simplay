import sys
from PyQt5.QtWidgets import QApplication

from gui.main_window import MainWindow


app = QApplication(sys.argv)
app.setApplicationName("Simplay")
app.setOrganizationName('SPŠ Trutnov')
app.setOrganizationDomain("https://spstrutnov.cz/")

window = MainWindow()

app.exec_()