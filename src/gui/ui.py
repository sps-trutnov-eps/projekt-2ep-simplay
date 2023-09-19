import sys
from PyQt5 import QtWidgets, QtCore, QtGui


class CustomMenu(QtWidgets.QMenu):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setStyleSheet('QMenu{background: rgb(55, 55, 55);} QMenu::item:selected {background: rgb(50, 47, 55);}')
        self.setFixedHeight(100)

        self.visible_lst = []
        self.index = -1
        self.visibleCount = None
        self.maxHeightOfAction = 0

        # -------- Remove Below code if you don't want the arrow ---------------#
        self.topArrow = None
        self.bottomArrow = None
        self.painter = QtGui.QPainter()
        # ---------------------------------------- #

    def actionEvent(self, event):

        if event.type() == QtCore.QEvent.ActionAdded:

            if self.maxHeightOfAction < self.actionGeometry(self.actions()[-1]).height():
                self.maxHeightOfAction = self.actionGeometry(self.actions()[-1]).height()

            self.actions()[-1].setVisible(False) 
            self.updateActions()

        if event.type() == QtCore.QEvent.ActionRemoved:
            super(CustomMenu, self).actionEvent(event)

            if self.index == len(self.actions()):
                self.index -= 1

            if event.action() in self.visible_lst:
                self.visible_lst.remove(event.action())
                self.removed()

        super(CustomMenu, self).actionEvent(event)

    def updateActions(self):

        if self.actions():
            if self.findVisibleCount() > len(self.actions()) and self.index == -1:
                self.visible_lst = self.actions()
                self.updateVisible()

            elif self.findVisibleCount() < len(self.actions()) and self.index == -1:
                self.index += 1
                self.visible_lst = self.actions()[0: self.findVisibleCount()]
                self.updateVisible()

            self.setActiveAction(self.visible_lst[0])

    def removed(self):

        if len(self.actions()) > self.findVisibleCount():
            if self.index < len(self.actions())-2:
                index = self.findIndex(self.visible_lst, self.activeAction())
                self.visible_lst.append(self.actions()[self.index + (index-self.findVisibleCount())-1])

            elif self.index == len(self.actions())-1:
                self.visible_lst.insert(0, self.actions()[-self.findVisibleCount()-1])

            self.updateVisible()

    def findVisibleCount(self): # finds how many QActions will be visible
        visibleWidgets = 0

        if self.actions():

            try:
                visibleWidgets = self.height()//self.maxHeightOfAction

            except ZeroDivisionError:
                pass

        return visibleWidgets

    def mousePressEvent(self, event) -> None:

        if self.topArrow.containsPoint(event.pos(), QtCore.Qt.OddEvenFill) and self.index>0:
            self.scrollUp()

        elif self.bottomArrow.containsPoint(event.pos(), QtCore.Qt.OddEvenFill) and self.index < len(self.actions()) -1:
            self.scrollDown()

        else:
            super(CustomMenu, self).mousePressEvent(event)

    def keyPressEvent(self, event):

        if self.actions():
            if self.activeAction() is None:
                self.setActiveAction(self.actions()[self.index])

            if event.key() == QtCore.Qt.Key_Up:
                self.scrollUp()

            elif event.key() == QtCore.Qt.Key_Down:
                self.scrollDown()

            elif event.key() == QtCore.Qt.Key_Return:
                super(CustomMenu, self).keyPressEvent(event)

    def wheelEvent(self, event):

        if self.actions():

            if self.activeAction() is None:
                self.setActiveAction(self.actions()[self.index])

            delta = event.angleDelta().y()
            if delta < 0:  # scroll down
                self.scrollDown()

            elif delta > 0:  # scroll up
                self.scrollUp()

    def scrollDown(self):

        if self.index < len(self.actions())-1:
            self.index = self.findIndex(self.actions(), self.activeAction()) + 1

            try:
                self.setActiveAction(self.actions()[self.index])
                if self.activeAction() not in self.visible_lst and len(self.actions()) > self.findVisibleCount():
                    self.visible_lst[0].setVisible(False)
                    self.visible_lst.pop(0)
                    self.visible_lst.append(self.actions()[self.index])
                    self.visible_lst[-1].setVisible(True)

            except IndexError:
                pass

    def scrollUp(self):

        if self.findIndex(self.actions(), self.activeAction()) > 0:
            self.index = self.findIndex(self.actions(), self.activeAction()) - 1

            try:
                self.setActiveAction(self.actions()[self.index])

                if self.activeAction() not in self.visible_lst and len(self.actions()) > self.findVisibleCount():
                    self.visible_lst[-1].setVisible(False)
                    self.visible_lst.pop()
                    self.visible_lst.insert(0, self.actions()[self.index])
                    self.visible_lst[0].setVisible(True)

            except IndexError:
                pass

    def updateVisible(self):
        for item in self.visible_lst:
            if not item.isVisible():
                item.setVisible(True)

    def findIndex(self, lst, element):
        for index, item in enumerate(lst):
            if item == element:
                return index
        return -1

    def paintEvent(self, event):  # remove this if you don't want the arrow
        super(CustomMenu, self).paintEvent(event)

        height = int(self.height())
        width = self.width()//2

        topPoints = [QtCore.QPoint(width-5, 7), QtCore.QPoint(width, 2), QtCore.QPoint(width+5, 7)]
        bottomPoints = [QtCore.QPoint(width-5, height-7), QtCore.QPoint(width, height-2), QtCore.QPoint(width+5, height-7)]

        self.topArrow = QtGui.QPolygon(topPoints)
        self.bottomArrow = QtGui.QPolygon(bottomPoints)

        self.painter.begin(self)
        self.painter.setBrush(QtGui.QBrush(QtCore.Qt.white))
        self.painter.setPen(QtCore.Qt.white)

        if len(self.actions()) > self.findVisibleCount():
            if self.index>0:
                self.painter.drawPolygon(self.topArrow)

            if self.index < len(self.actions()) -1:
                self.painter.drawPolygon(self.bottomArrow)

        self.painter.end()


class ExampleWindow(QtWidgets.QWidget):

    def contextMenuEvent(self, event) -> None:

        menu = CustomMenu()

        menu.addAction('Přidat novou složku')
        menu.addAction('2')
        menu.addAction('3')

        menu.exec_(QtGui.QCursor.pos())
