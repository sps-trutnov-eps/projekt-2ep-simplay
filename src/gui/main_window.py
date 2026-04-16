from qtpy.QtWidgets import QMainWindow
from qtpy.QtCore import Qt, QPoint

from gui.ui import Ui_MainWindow


class MainWindow(QMainWindow):
    
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow(self)

        # Frameless window logic
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Dragging support
        self._drag_pos = QPoint()

        self.show()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._drag_pos = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self._drag_pos)
            event.accept()
