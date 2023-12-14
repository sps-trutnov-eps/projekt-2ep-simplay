from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *

from gui.components import NavigationBar
from obj.time import TimeCount


class PlayedTimeView(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"background-color: #322F37;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.navigationBar = NavigationBar(MainWindow, self.verticalLayout)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pageTitle = QLabel(self.widget)
        self.pageTitle.setObjectName(u"pageTitle")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(28)
        self.pageTitle.setFont(font1)
        self.pageTitle.setLayoutDirection(Qt.LeftToRight)
        self.pageTitle.setStyleSheet(u"color: #F5F5F5;")
        self.pageTitle.setAlignment(Qt.AlignCenter)
        self.pageTitle.setMargin(20)

        self.verticalLayout_2.addWidget(self.pageTitle)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.mainContainer = QWidget(self.widget)
        self.mainContainer.setObjectName(u"mainContainer")
        self.horizontalLayout_3 = QHBoxLayout(self.mainContainer)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.mainContainer)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(16)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"color: #F5F5F5;")
        self.label.setAlignment(Qt.AlignCenter)
        self.pushButton = QPushButton(self.mainContainer)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(100, 16777215))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"margin: 10 0 0 0; height: 35; border: none; background-color: #C03E25; border-radius: 5; color: #FEFEFE;")
        
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout_2.addWidget(self.mainContainer)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.verticalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pageTitle.setText(QCoreApplication.translate("MainWindow", u"Odehran\u00fd \u010das", None))
        self.label.setText(QCoreApplication.translate("MainWindow", str(TimeCount.getPlayedTime()) + " hodin", None))
        self.pushButton.setText("Zpět")
    # retranslateUi

