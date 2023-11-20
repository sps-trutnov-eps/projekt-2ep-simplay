from Custom_Widgets.Widgets import *
from qtpy.QtCore import *
import os

from gui.views import *
from Obj.game import *
from Obj.security import *
from Obj.time import *
from Obj.add_category import *

class Ui_MainWindow(object):

    def __init__(self, MainWindow) -> None:
        self.MainWindow = MainWindow
        self.EncodingManager = EncodingManager()

        password_file = ""
        with open("data/password.txt", 'r', encoding="utf-8") as f:
            password_file = f.readline()

        if (len(password_file) > 0):
            self.setupLockedScreenView()
        else:
            self.setupHomeView()

        
    def setupHomeView(self) -> None:
        self.HomeView = HomeView()
        game_manager = GameManager()
        self.fillGamesWidget(game_manager)

        self.HomeView.setupUi(self.MainWindow)
        
        self.HomeView.addGameBtn.clicked.connect(lambda: self.addGame(game_manager))
        self.HomeView.usersBtn.clicked.connect(self.setupSetPasswordView)

    def setupLockedScreenView(self) -> None:
        self.LockedScreenView = LockedScreenView()
        self.LockedScreenView.setupUi(self.MainWindow)

        self.LockedScreenView.pushButton.clicked.connect(lambda: self.checkPassword(self.LockedScreenView.lineEdit.text()))

    def setupAddCategoryView(self) -> None: 
        self.AddCategoryView = AddCategoryView()
        self.AddCategoryView.setupUi(self.MainWindow)

    def setupSetPasswordView(self) -> None:
        self.SetPasswordView = SetPasswordView()
        self.SetPasswordView.setupUi(self.MainWindow)

        self.SetPasswordView.pushButton.clicked.connect(lambda: self.setPassword(self.SetPasswordView.lineEdit.text()))

    def setupPlayedTimeView(self) -> None:
        self.PlayedTimeView = PlayedTimeView()
        self.PlayedTimeView.setupUi(self.MainWindow)

    
    def addGame(self, game_manager) -> None:
        path = QFileDialog.getOpenFileName(filter="Podporované formáty (*.py; *.exe)")
        path = path[0]
        
        if (type(path) == str and len(path) > 0):
            name = os.path.basename(path)
            game_manager.addGame(name, path)
            self.setupHomeView()


    def fillGamesWidget(self, game_manager: GameManager) -> None:
        self.gameFont = QFont()
        self.gameFont.setFamily(u"Segoe UI")
        self.gameFont.setPointSize(12)

        self.gameSubFont = QFont()
        self.gameSubFont.setFamily(u"Segoe UI")
        self.gameSubFont.setPointSize(10)

        for game in game_manager.getGames():
            self.game = QWidget()
            self.game.setStyleSheet(u"background-color: #28262C")
            self.game.setMaximumWidth(100)
            self.game.setMinimumHeight(130)
            self.game.setContentsMargins(QMargins(5, 5, 5, 5))
            self.game.setCursor(QCursor(Qt.PointingHandCursor))

            self.layout = QVBoxLayout(self.game)
            self.title = QLabel(self.game)
            self.title.setText(game.getName())
            self.title.setFont(self.gameFont)
            self.title.setStyleSheet(u"color: #FEFEFE")
            self.layout.addWidget(self.title)
            self.subtitle = QLabel(self.game)
            self.subtitle.setText(game.getUUID())
            self.subtitle.setFont(self.gameSubFont)
            self.subtitle.setStyleSheet(u"color: #28262C")
            self.layout.addWidget(self.subtitle)

            self.button = QPushButton(self.game)
            self.button.setText("Spustit")
            self.button.setStyleSheet(u"height: 35; border: none; background-color: #C03E25; border-radius: 5; color: #FEFEFE;")
            self.layout.addWidget(self.button)
            self.button.clicked.connect(game.run)

            self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.game.setLayout(self.layout)

            self.HomeView.games["game" + game.getUUID()] = self.game

        # Zde naházej hry do listu self.HomeView.games
        #self.game = QWidget()
        #self.game.setStyleSheet(u"background-color: #28262C")
        #self.game.setMaximumWidth(100)
        #self.game.setMinimumHeight(130)
        #self.game.setContentsMargins(QMargins(5, 5, 5, 5))
        #self.game.setCursor(QCursor(Qt.PointingHandCursor))

        #self.layout = QVBoxLayout(self.game)
        #self.title = QLabel(self.game)
        #self.title.setText(game.getName())
        #self.title.setFont(self.gameFont)
        #self.title.setStyleSheet(u"color: #FEFEFE")
        #self.layout.addWidget(self.title)
        #self.subtitle = QLabel(self.game)
        #self.subtitle.setText(game.getUUID())
        #self.subtitle.setFont(self.gameSubFont)
        #self.subtitle.setStyleSheet(u"color: #28262C")
        #self.layout.addWidget(self.subtitle)

        #self.button = QPushButton(self.game)
        #self.button.setText("Spustit")
        #self.button.setStyleSheet(u"height: 35; border: none; background-color: #C03E25; border-radius: 5; color: #FEFEFE;")
        #self.layout.addWidget(self.button)
        #self.button.clicked.connect(game.run)

        #self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        #self.game.setLayout(self.layout)

        #self.HomeView.games["game" + game.getUUID()] = self.game
        # Atd.

    def setPassword(self, password: str) -> None:
        encoded_password = self.EncodingManager.encrypt(password)

        with open("data/password.txt", 'w', encoding="utf-8") as f:
            if (len(password) > 0):
                f.write(encoded_password)

        self.setupHomeView()

    def checkPassword(self, password: str) -> bool:
        password_file = ""
        with open("data/password.txt", 'r', encoding="utf-8") as f:
            password_file = f.readline()

        if (password == self.EncodingManager.decrypt(password_file)):
            self.setupHomeView()
            return True

        self.setupLockedScreenView()
        return False