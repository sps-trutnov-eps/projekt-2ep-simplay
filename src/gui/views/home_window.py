from qtpy.QtWidgets import *
from qtpy.QtCore import *
from qtpy.QtGui import *


class HomeView(object):        
    def setupUi(self, MainWindow):        
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"HomeWindow")
        MainWindow.resize(1134, 844)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/icons/feather/clock.svg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"*{\n"
"	border:none;\n"
"	background-color transparent;\n"
"    background:none;\n"
"	padding:0;\n"
"	margin: 0;\n"
"	color: none;\n"
"}\n"
"\n"
"#centralwidget {\n"
"	\n"
"	background-color: rgb(60, 58, 65);\n"
"}\n"
"#leftMenuSubcontainer {\n"
"	background-color: rgb(50, 47, 55);\n"
"}\n"
"#leftMenuSubcontainer QPushButton{\n"
"	text-allign: left;\n"
"	padding: 5px 10px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
"#headerContainer {\n"
"	background-color: rgb(50, 47, 55);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuContainer = QWidget(self.centralwidget)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        self.verticalLayout = QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuSubcontainer = QWidget(self.leftMenuContainer)
        self.leftMenuSubcontainer.setObjectName(u"leftMenuSubcontainer")
        self.verticalLayout_2 = QVBoxLayout(self.leftMenuSubcontainer)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.leftMenuSubcontainer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menuBtn = QPushButton(self.frame)
        self.menuBtn.setObjectName(u"menuBtn")
        font = QFont()
        font.setPointSize(15)
        self.menuBtn.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u":/icons/feather/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon1)
        self.menuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.menuBtn, 0, Qt.AlignLeft)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_2 = QFrame(self.leftMenuSubcontainer)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.timeBtn = QPushButton(self.frame_2)
        self.timeBtn.setObjectName(u"timeBtn")
        self.timeBtn.setMinimumSize(QSize(0, 0))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(15)
        self.timeBtn.setFont(font1)
        self.timeBtn.setIcon(icon)
        self.timeBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.timeBtn)

        self.usersBtn = QPushButton(self.frame_2)
        self.usersBtn.setObjectName(u"usersBtn")
        self.usersBtn.setFont(font1)
        icon2 = QIcon()
        icon2.addFile(u":/icons/feather/users.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.usersBtn.setIcon(icon2)
        self.usersBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.usersBtn)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignTop)


        self.verticalLayout.addWidget(self.leftMenuSubcontainer)


        self.horizontalLayout.addWidget(self.leftMenuContainer, 0, Qt.AlignLeft)

        self.mainBodyContainer = QWidget(self.centralwidget)
        self.mainBodyContainer.setObjectName(u"mainBodyContainer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy1)
        self.mainBodyContainer.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.headerContainer = QWidget(self.mainBodyContainer)
        self.headerContainer.setObjectName(u"headerContainer")
        self.horizontalLayout_4 = QHBoxLayout(self.headerContainer)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_5 = QFrame(self.headerContainer)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.minimizeBtn = QPushButton(self.frame_5)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        icon3 = QIcon()
        icon3.addFile(u":/icons/feather/chevron-up.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeBtn.setIcon(icon3)
        self.minimizeBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.minimizeBtn)

        self.maximizeBtn = QPushButton(self.frame_5)
        self.maximizeBtn.setObjectName(u"maximizeBtn")
        icon4 = QIcon()
        icon4.addFile(u":/icons/feather/maximize-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeBtn.setIcon(icon4)
        self.maximizeBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.maximizeBtn)

        self.closeBtn = QPushButton(self.frame_5)
        self.closeBtn.setObjectName(u"closeBtn")
        icon5 = QIcon()
        icon5.addFile(u":/icons/feather/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon5)
        self.closeBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.closeBtn)


        self.horizontalLayout_4.addWidget(self.frame_5, 0, Qt.AlignRight)


        self.verticalLayout_4.addWidget(self.headerContainer, 0, Qt.AlignTop)

        self.mainBodyContent = QWidget(self.mainBodyContainer)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        sizePolicy.setHeightForWidth(self.mainBodyContent.sizePolicy().hasHeightForWidth())
        self.mainBodyContent.setSizePolicy(sizePolicy)
        self.verticalLayout_5 = QVBoxLayout(self.mainBodyContent)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.gameInfo = QWidget(self.mainBodyContent)
        self.gameInfo.setObjectName(u"gameInfo")
        self.Games = QLabel(self.gameInfo)
        self.Games.setObjectName(u"Games")
        self.Games.setGeometry(QRect(10, 10, 61, 31))
        self.Games.setFont(font1)
        self.addGameBtn = QPushButton(self.gameInfo)
        self.addGameBtn.setObjectName(u"addGameBtn")
        self.addGameBtn.setGeometry(QRect(500, 10, 150, 30))
        self.addGameBtn.setMinimumSize(QSize(150, 30))
        self.addGameBtn.setMaximumSize(QSize(150, 30))
        self.addGameBtn.setFont(font1)
        icon6 = QIcon()
        icon6.addFile(u":/icons/feather/plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.addGameBtn.setIcon(icon6)
        self.addGameBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.gameInfo)

        self.gameBox = QWidget(self.mainBodyContent)
        self.gameBox.setObjectName(u"gameBox")

        self.verticalLayout_5.addWidget(self.gameBox)

        self.ctgrInfo = QWidget(self.mainBodyContent)
        self.ctgrInfo.setObjectName(u"ctgrInfo")
        self.Categories = QLabel(self.ctgrInfo)
        self.Categories.setObjectName(u"Categories")
        self.Categories.setGeometry(QRect(10, 10, 111, 41))
        self.Categories.setFont(font1)
        self.addCtgrBtn = QPushButton(self.ctgrInfo)
        self.addCtgrBtn.setObjectName(u"addCtgrBtn")
        self.addCtgrBtn.setGeometry(QRect(500, 10, 150, 30))
        self.addCtgrBtn.setMinimumSize(QSize(150, 30))
        self.addCtgrBtn.setMaximumSize(QSize(150, 30))
        self.addCtgrBtn.setFont(font1)
        icon7 = QIcon()
        icon7.addFile(u":/icons/feather/plus-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.addCtgrBtn.setIcon(icon7)
        self.addCtgrBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.ctgrInfo)

        self.ctgrBox = QWidget(self.mainBodyContent)
        self.ctgrBox.setObjectName(u"ctgrBox")

        self.verticalLayout_5.addWidget(self.ctgrBox)


        self.verticalLayout_4.addWidget(self.mainBodyContent)


        self.horizontalLayout.addWidget(self.mainBodyContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.menuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.menuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.timeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"View time spent on your games", None))
#endif // QT_CONFIG(tooltip)
        self.timeBtn.setText(QCoreApplication.translate("MainWindow", u" Time", None))
#if QT_CONFIG(tooltip)
        self.usersBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Manage who's playing", None))
#endif // QT_CONFIG(tooltip)
        self.usersBtn.setText(QCoreApplication.translate("MainWindow", u" Users", None))
        self.minimizeBtn.setText("")
        self.maximizeBtn.setText("")
        self.closeBtn.setText("")
        self.Games.setText(QCoreApplication.translate("MainWindow", u"Hry", None))
        self.addGameBtn.setText(QCoreApplication.translate("MainWindow", u" P\u0159idat hru", None))
        self.Categories.setText(QCoreApplication.translate("MainWindow", u"Slo\u017eky", None))
        self.addCtgrBtn.setText(QCoreApplication.translate("MainWindow", u" P\u0159idat slo\u017eku", None))
    # retranslateUi
