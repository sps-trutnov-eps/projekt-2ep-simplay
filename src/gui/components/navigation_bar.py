from qtpy.QtWidgets import *
from qtpy.QtCore import *
from qtpy.QtGui import *

class NavigationBar(QWidget):
    """
    Vlastní komponenta navigačního panelu (Title Bar).
    Zajišťuje ovládání okna (minimalizace, maximalizace, zavření) 
    a umožňuje přesunování bezrámového okna tažením.
    """

    def __init__(self, MainWindow, parent_layout):
        super(NavigationBar, self).__init__()
        self.parent_layout = parent_layout
        self.MainWindow = MainWindow
        self._drag_pos = QPoint()

        # Nastavení rozvržení a vizuálního stylu panelu
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.navigationWidget = QWidget(self)
        self.navigationWidget.setObjectName(u"navigationWidget")
        self.navigationWidget.setMinimumSize(QSize(0, 30))
        self.navigationWidget.setStyleSheet(u"background-color: #28262C; margin: 0")
        self.horizontalLayout = QHBoxLayout(self.navigationWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        
        # Titulek aplikace
        self.title = QLabel(self.navigationWidget)
        self.title.setObjectName(u"title")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        self.title.setFont(font)
        self.title.setStyleSheet(u"color: #FEFEFE; margin: 0 5;")

        self.horizontalLayout.addWidget(self.title)

        # Pružná mezera pro odsunutí tlačítek doprava
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(self.horizontalSpacer)

        # Kontejner pro ovládací tlačítka
        self.buttonsWidget = QWidget(self.navigationWidget)
        self.buttonsWidget.setObjectName(u"buttonsWidget")
        self.horizontalLayout_2 = QHBoxLayout(self.buttonsWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        
        # Tlačítko minimalizace
        self.minimizeButton = QPushButton(self.buttonsWidget)
        self.minimizeButton.setObjectName(u"minimizeButton")
        self.minimizeButton.setStyleSheet(u"border: none; margin: 0 2;")
        icon = QIcon()
        icon.addFile(u"assets/icons/chevron-down.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeButton.setIcon(icon)
        self.horizontalLayout_2.addWidget(self.minimizeButton)

        # Tlačítko maximalizace / obnovení
        self.restoreButton = QPushButton(self.buttonsWidget)
        self.restoreButton.setObjectName(u"restoreButton")
        self.restoreButton.setStyleSheet(u"border: none; margin: 0 2;")
        icon1 = QIcon()
        icon1.addFile(u"assets/icons/maximize-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreButton.setIcon(icon1)
        self.horizontalLayout_2.addWidget(self.restoreButton)

        # Tlačítko zavření
        self.closeButton = QPushButton(self.buttonsWidget)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setStyleSheet(u"border: none; margin: 0 2;")
        icon2 = QIcon()
        icon2.addFile(u"assets/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeButton.setIcon(icon2)
        self.horizontalLayout_2.addWidget(self.closeButton)

        self.horizontalLayout.addWidget(self.buttonsWidget)

        # Přidání panelu do hlavního rozvržení okna
        self.parent_layout.addWidget(self.navigationWidget)

        self.retranslateUi()
        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        """Nastavení textů a propojení událostí tlačítek."""
        self.title.setText(QCoreApplication.translate("Dialog", u"Simplay", None))
        self.minimizeButton.clicked.connect(lambda: self.MainWindow.showMinimized())
        self.restoreButton.clicked.connect(lambda: self.restore_or_maximize_window())
        self.closeButton.clicked.connect(lambda: self.MainWindow.close())

    def mousePressEvent(self, event):
        """Uloží pozici kliknutí pro umožnění tažení okna."""
        if event.button() == Qt.LeftButton:
            self._drag_pos = event.globalPos() - self.MainWindow.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        """Zajišťuje přesun celého okna při pohybu myší nad panelem."""
        if event.buttons() == Qt.LeftButton:
            self.MainWindow.move(event.globalPos() - self._drag_pos)
            event.accept()

    def updateRestoreButtonIcon(self):
        """Aktualizuje ikonu tlačítka podle toho, zda je okno maximalizované."""
        if self.MainWindow.isMaximized():
            self.restoreButton.setIcon(QIcon("assets/icons/minimize-2.svg"))
        else:
            self.restoreButton.setIcon(QIcon("assets/icons/maximize-2.svg"))

    def restore_or_maximize_window(self):
        """Přepíná mezi maximalizovaným a normálním zobrazením okna."""
        if self.MainWindow.isMaximized():
            self.MainWindow.showNormal()
        else:
            self.MainWindow.showMaximized()
        self.updateRestoreButtonIcon()