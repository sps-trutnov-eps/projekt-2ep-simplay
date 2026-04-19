from qtpy.QtWidgets import QMainWindow
from qtpy.QtCore import Qt, QPoint

from gui.ui import Ui_MainWindow


class MainWindow(QMainWindow):
    """
    Hlavní okno aplikace Simplay.
    Zajišťuje vizuální styl (bezrámové okno) a základní interakci.
    """
    
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow(self)

        # Nastavení bezrámového okna s průhledným pozadím
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Inicializace pozice pro podporu tažení okna myší
        self._drag_pos = QPoint()

        self.show()

    def mousePressEvent(self, event):
        """Uloží počáteční pozici při kliknutí pro následné tažení okna."""
        if event.button() == Qt.LeftButton:
            self._drag_pos = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        """Zajišťuje plynulý pohyb okna při tažení myší."""
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self._drag_pos)
            event.accept()
