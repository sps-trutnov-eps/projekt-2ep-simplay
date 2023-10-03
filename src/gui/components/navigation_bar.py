from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from gui.qss import *


class NavigationBar(QWidget):

    def __init__(self, parent_layout):
        super(NavigationBar, self).__init__()
        self.parent_layout = parent_layout


        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.navigationWidget = QWidget(self)
        self.navigationWidget.setObjectName(u"navigationWidget")
        self.navigationWidget.setMinimumSize(QSize(0, 50))
        self.navigationWidget.setStyleSheet(u"background-color: #28262C; margin: 0")
        self.horizontalLayout = QHBoxLayout(self.navigationWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.title = QLabel(self.navigationWidget)
        self.title.setObjectName(u"title")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        self.title.setFont(font)
        self.title.setStyleSheet(u"color: #FEFEFE; margin: 0 5;")

        self.horizontalLayout.addWidget(self.title)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.buttonsWidget = QWidget(self.navigationWidget)
        self.buttonsWidget.setObjectName(u"buttonsWidget")
        self.buttonsWidget.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.buttonsWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.minimizeButton = QPushButton(self.buttonsWidget)
        self.minimizeButton.setObjectName(u"minimizeButton")
        self.minimizeButton.setStyleSheet(u"border: none; margin: 0 2;")
        icon = QIcon()
        icon.addFile(u"assets/icons/chevron-down.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeButton.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.minimizeButton)

        self.restoreButton = QPushButton(self.buttonsWidget)
        self.restoreButton.setObjectName(u"restoreButton")
        self.restoreButton.setStyleSheet(u"border: none; margin: 0 2;")
        icon1 = QIcon()
        icon1.addFile(u"assets/icons/maximize-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreButton.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.restoreButton)

        self.closeButton = QPushButton(self.buttonsWidget)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setStyleSheet(u"border: none; margin: 0 2;")
        icon2 = QIcon()
        icon2.addFile(u"assets/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeButton.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.closeButton)


        self.horizontalLayout.addWidget(self.buttonsWidget)


        self.parent_layout.addWidget(self.navigationWidget)


        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self):
        self.title.setText(QCoreApplication.translate("Dialog", u"Simplay", None))
        self.minimizeButton.setText("")
        self.restoreButton.setText("")
    # retranslateUi