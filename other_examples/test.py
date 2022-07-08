#!/usr/bin/env python3

import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class WinDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(WinDialog, self).__init__(parent)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle("Signal & Slot")

        self.propertyWidget = PropertyWidget()

        section_lay = QtWidgets.QHBoxLayout()
        section_label = QtWidgets.QLabel("Name: ")
        section_edit = QtWidgets.QLineEdit('')

        length_lay = QtWidgets.QHBoxLayout()

        length_label = QtWidgets.QLabel("Input a number:     L = ")
        self.length_edit = QtWidgets.QLineEdit()
        self.length_edit.setFocus(True)
        val_lenght = QtGui.QIntValidator(0, 100000, self.length_edit)
        self.length_edit.setValidator(val_lenght)

        thick_lay = QtWidgets.QHBoxLayout()
        thick_label = QtWidgets.QLabel("Input a text: T = ")
        self.thick_edit = QtWidgets.QLineEdit()
        val_thick = QtGui.QIntValidator(0, 100000, self.thick_edit)
        self.thick_edit.setValidator(val_thick)

        section_lay.addWidget(section_label)
        section_lay.addWidget(section_edit)

        length_lay.addWidget(length_label)
        length_lay.addWidget(self.length_edit)
        length_lay.addStretch()

        thick_lay.addWidget(thick_label)
        thick_lay.addWidget(self.thick_edit)
        thick_lay.addStretch()

        VB_lay = QtWidgets.QVBoxLayout()
        VB_lay.addStretch()
        VB_lay.addLayout(length_lay)
        VB_lay.addLayout(thick_lay)
        VB_lay.addStretch()

        buttonBox = QtWidgets.QDialogButtonBox()

        buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel
                                     | QtWidgets.QDialogButtonBox.Ok)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        grid = QtWidgets.QGridLayout(self)
        grid.addLayout(section_lay, 0, 0, 1, 2)
        grid.addLayout(VB_lay, 1, 0)
        grid.addWidget(self.propertyWidget, 2, 0)
        grid.addWidget(buttonBox, 3, 0, 1, 2)

        self.length_edit.textEdited.connect(self.onTextEdited)
        self.thick_edit.textEdited.connect(self.onTextEdited)

    def onTextEdited(self):
        l = self.length_edit.text()
        t = self.thick_edit.text()
        self.propertyWidget.display(l, t)


class PropertyWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(PropertyWidget, self).__init__(parent)
        HB_lay = QtWidgets.QHBoxLayout(self)
        self.Displaylabel = QtWidgets.QLabel('')
        HB_lay.addWidget(self.Displaylabel)
        HB_lay.addStretch()

    def display(self, l, t):
        try:
            L_Display = int(l)
            T_Display = int(t)
            fmt = "L = {}mm\nT = {}mm"
            self.Displaylabel.setText(fmt.format(L_Display, T_Display))
        except ValueError:
            self.Displaylabel.clear()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = WinDialog()
    w.show()
    sys.exit(app.exec_())
