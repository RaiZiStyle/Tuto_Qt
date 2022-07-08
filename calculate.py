#!/usr/bin/env python3

from __future__ import division
from math import *
import sys
# import time
from PyQt5.QtCore import Qt
# from PyQt5.QtGui import QApli
from PyQt5.QtWidgets import QDialog, QTextBrowser, QLineEdit, QVBoxLayout, QApplication


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.browser = QTextBrowser()
        self.lineedit = QLineEdit("Type an expression and press Enter")
        self.lineedit.selectAll()
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(self.lineedit)
        self.setLayout(layout)
        self.lineedit.setFocus()
        # self.connec
        # self.connect(self.lineedit, SIGNAL("returnPressed()"),
        #              self.updateUi)
        self.update(self.lineedit, SIGNAL("returnPressed()"),
                     self.updateUi)
        self.setWindowTitle("Calculate")

    # def keyPressEvent(self, e) -> None:
    #     if e.key()  == Qt.Key_enter:
    #         self

    def updateUi(self):
        try:
            text = str(self.lineedit.text())
            self.browser.append("%s = <b>%s</b>" % (text, eval(text)))
        except:
            self.browser.append("<font color=red>%s is invalid!</font>" % text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()
