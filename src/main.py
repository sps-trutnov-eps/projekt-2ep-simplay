import sys
from qtpy.QtWidgets import QApplication

from gui.main_window import MainWindow
from obj.time import TimeCount


app = QApplication(sys.argv)
app.setApplicationName("Simplay")
app.setOrganizationName('SPŠ Trutnov')
app.setOrganizationDomain("https://spstrutnov.cz/")

window = MainWindow()

time_count = TimeCount()
app.exec_()
time_count.end()