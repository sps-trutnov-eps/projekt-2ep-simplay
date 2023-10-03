from gui.ui import Ui_MainWindow


class MainWindow(Ui_MainWindow):
    
    def __init__(self) -> None:
        super(MainWindow, self).__init__()

        self.setMinimumSize(600, 400)
        self.show()