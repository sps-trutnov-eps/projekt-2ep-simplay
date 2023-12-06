from Custom_Widgets.Widgets import *
from qtpy.QtCore import *
import os

from gui.views import *
from Obj.game import *
from Obj.security import *
from Obj.time import *
from Obj.category import *

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
        category_manager = CategoryManager(game_manager)

        # Adding default games to list

        game1 = Game("0", "RPS", "data\\rps.exe")                                  
        game_manager.games.append(game1)

        game2 = Game("1", "TicTacToe", "data\\tictactoe.exe")
        game_manager.games.append(game2)

        game3 = Game("2", "Hangman", "data\hangman.exe")
        game_manager.games.append(game3)

        self.fillGamesWidget(game_manager)

        self.HomeView.setupUi(self.MainWindow)
        
        self.HomeView.addGameBtn.clicked.connect(lambda: self.addGame(game_manager))
        self.HomeView.usersBtn.clicked.connect(self.setupSetPasswordView)
        self.HomeView.rmvCtgrBtn.clicked.connect(lambda: self.addCategory(category_manager))

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

    def addCategory(self, category_manager: CategoryManager) -> None:
        name = QInputDialog.getText(self.HomeView.centralwidget, "Přidat kategorii", "Název kategorie")
        name = name[0]
        
        if (len(name) > 0):
            category_manager.addCategory(name)

        self.fillCategoriesWidget(category_manager)


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


    def fillCategoriesWidget(self, category_manager: CategoryManager) -> None:
        for category in category_manager.getCategories():
            categoryWidget = QWidget()
            categoryWidgetLayout = QHBoxLayout(categoryWidget)

            for game in category.getGames():
                gameWidget = QWidget(categoryWidget)                                       # Main game widget
                gameWidget.setStyleSheet(u"background-color: #28262C")
                gameWidget.setMaximumWidth(100)
                gameWidget.setMinimumHeight(130)
                gameWidget.setContentsMargins(QMargins(5, 5, 5, 5))
                gameWidget.setCursor(QCursor(Qt.PointingHandCursor))
                
                layout = QVBoxLayout(gameWidget)


                title = QLabel(gameWidget)
                title.setText(game.getName())
                title.setFont(self.gameFont)
                title.setStyleSheet(u"color: #FEFEFE")
                layout.addWidget(title)
                
                subtitle = QLabel(gameWidget)
                subtitle.setText(game.getUUID())
                subtitle.setFont(self.gameSubFont)
                subtitle.setStyleSheet(u"color: #28262C")
                layout.addWidget(subtitle)

            
                button = QPushButton(gameWidget)
                button.setText("Spustit")
                button.setStyleSheet(u"height: 35; border: none; background-color: #C03E25; border-radius: 5; color: #FEFEFE;")
                layout.addWidget(button)
                button.clicked.connect(game.run)


                layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
                game.setLayout(layout)



                categoryWidgetLayout.addWidget(gameWidget)
            # Game


            self.HomeView.categories[category.getName()] = categoryWidget


            self.HomeView.setupUi(self.MainWindow)


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