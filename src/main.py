import sys
from qtpy.QtWidgets import QApplication

from gui.main_window import MainWindow
from obj.time import TimeCount

# Hlavní vstupní bod aplikace
if __name__ == "__main__":
    # Inicializace Qt aplikace
    app = QApplication(sys.argv)
    app.setApplicationName("Simplay")
    app.setOrganizationName('SPŠ Trutnov')
    app.setOrganizationDomain("https://spstrutnov.cz/")

    # Vytvoření a zobrazení hlavního okna
    window = MainWindow()

    #Spuštění měření času stráveného v aplikaci
    time_count = TimeCount()
    
    # Spuštění hlavní smyčky událostí
    app.exec_()
    
    # Uložení naměřeného času při ukončení
    time_count.end()