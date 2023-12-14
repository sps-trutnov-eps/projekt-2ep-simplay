from qtpy.QtWidgets import *
from qtpy.QtCore import *
from qtpy.QtGui import *

from gui.components import NavigationBar


class AddCategoryView(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1134, 844)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setStyleSheet(u"background-color: #322F37;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.navigationBar = NavigationBar(MainWindow, self.verticalLayout)

        self.pageTitle = QLabel(self.centralwidget)
        self.pageTitle.setObjectName(u"pageTitle")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(28)
        self.pageTitle.setFont(font1)
        self.pageTitle.setLayoutDirection(Qt.LeftToRight)
        self.pageTitle.setStyleSheet(u"color: #F5F5F5;")
        self.pageTitle.setAlignment(Qt.AlignCenter)
        self.pageTitle.setMargin(20)

        self.verticalLayout.addWidget(self.pageTitle)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.mainContainer = QWidget(self.centralwidget)
        self.mainContainer.setObjectName(u"mainContainer")
        self.mainContainer.setMinimumSize(QSize(500, 300))
        self.horizontalLayout_3 = QHBoxLayout(self.mainContainer)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.formContainer = QWidget(self.mainContainer)
        self.formContainer.setObjectName(u"formContainer")
        self.formContainer.setMinimumSize(QSize(0, 0))
        self.formContainer.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.formContainer)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.nameEdit = QLineEdit(self.formContainer)
        self.nameEdit.setObjectName(u"nameEdit")
        self.nameEdit.setMinimumSize(QSize(0, 35))
        self.nameEdit.setStyleSheet(u"border: 1px solid #C03E35; border-radius: 5; color: #F5F5F5; padding: 5;")
        self.nameEdit.setMaxLength(64)

        self.verticalLayout_2.addWidget(self.nameEdit)

        self.submitContainer = QWidget(self.formContainer)
        self.submitContainer.setObjectName(u"submitContainer")
        self.horizontalLayout_4 = QHBoxLayout(self.submitContainer)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton = QPushButton(self.submitContainer)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(100, 16777215))
        font2 = QFont()
        font2.setFamily(u"Segoe UI Historic")
        font2.setPointSize(10)
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"margin: 10 0 0 0; height: 35; border: none; background-color: #C03E25; border-radius: 5; color: #FEFEFE;")

        self.horizontalLayout_4.addWidget(self.pushButton)


        self.verticalLayout_2.addWidget(self.submitContainer)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)


        self.horizontalLayout_3.addWidget(self.formContainer)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.mainContainer)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.pageTitle.setText(QCoreApplication.translate("MainWindow", u"Vytvo\u0159it kategorii", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Vytvo\u0159it", None))
    # retranslateUi

