from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class AddCategoryDialog(QDialog):

    def __init__(self, parent=None) -> None:
        super(AddCategoryDialog, self).__init__(parent)

        self.setMinimumHeight(200)
        self.setMinimumWidth(300)
        self.initUi()
        self.exec_()


    def initUi(self):
        header_widget = QWidget(self)
        header_layout = QVBoxLayout(header_widget)
        header_widget.setLayout(header_layout)

        buttons_widget = QWidget(self)                                                  # Buttons
        buttons_layout = QVBoxLayout(buttons_widget)
        minimize_button = QPushButton(buttons_widget)                                       # Minimize button
        minimize_button.setIcon(QIcon("assets/icons/chevron-down.svg"))
        buttons_layout.addWidget(minimize_button)
        restore_button = QPushButton(buttons_widget)                                        # Restore button
        restore_button.setIcon(QIcon("assets/icons/maximize-2.svg"))
        buttons_layout.addWidget(restore_button)
        close_button = QPushButton(buttons_widget)                                          # Close button
        close_button.setIcon(QIcon("assets/icons/x.svg"))
        buttons_layout.addWidget(close_button)
        buttons_widget.setLayout(buttons_layout)
        