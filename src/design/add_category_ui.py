# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_category.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qtpy.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from qtpy.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from qtpy.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget, QVBoxLayout, QSpacerItem)
import resources_rc

class Ui_MainWindow(object):
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
        self.navigationWidget = QWidget(self.centralwidget)
        self.navigationWidget.setObjectName(u"navigationWidget")
        self.navigationWidget.setMinimumSize(QSize(0, 50))
        self.navigationWidget.setStyleSheet(u"background-color: #28262C; margin: 0")
        self.horizontalLayout = QHBoxLayout(self.navigationWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.navigationTitle = QLabel(self.navigationWidget)
        self.navigationTitle.setObjectName(u"navigationTitle")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        self.navigationTitle.setFont(font)
        self.navigationTitle.setStyleSheet(u"color: #FEFEFE; margin: 0 5;")

        self.horizontalLayout.addWidget(self.navigationTitle)

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
        icon.addFile(u":/icons/icons/chevron-down.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeButton.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.minimizeButton)

        self.restoreButton = QPushButton(self.buttonsWidget)
        self.restoreButton.setObjectName(u"restoreButton")
        self.restoreButton.setStyleSheet(u"border: none; margin: 0 2;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/maximize-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreButton.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.restoreButton)

        self.closeButton = QPushButton(self.buttonsWidget)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setStyleSheet(u"border: none; margin: 0 2;")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeButton.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.closeButton)


        self.horizontalLayout.addWidget(self.buttonsWidget)


        self.verticalLayout.addWidget(self.navigationWidget)

        self.pageTitle = QLabel(self.centralwidget)
        self.pageTitle.setObjectName(u"pageTitle")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
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
        font2.setFamilies([u"Segoe UI Historic"])
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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.navigationTitle.setText(QCoreApplication.translate("MainWindow", u"Simplay", None))
        self.minimizeButton.setText("")
        self.restoreButton.setText("")
        self.pageTitle.setText(QCoreApplication.translate("MainWindow", u"Vytvo\u0159it kategorii", None))
        self.nameEdit.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Vytvo\u0159it", None))
    # retranslateUi

