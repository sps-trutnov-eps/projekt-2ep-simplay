class MainWindow(Ui_MainWindow):
    
    def __init__(self) -> None:
        super().__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setMinimumSize(600, 400)
        self.init_gui()
        self.show()