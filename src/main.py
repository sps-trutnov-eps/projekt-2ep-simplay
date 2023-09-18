import sys
from PyQt5.QtWidgets import QApplication

from gui.window import Window


app = QApplication(sys.argv)
app.setApplicationName("Simplay")
app.setOrganizationName('SPŠ Trutnov')
app.setOrganizationDomain("https://spstrutnov.cz/")

window = Window()

app.exec_()