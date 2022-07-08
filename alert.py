#!/usr/bin/env python3

import sys
import time
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


def main(default_time: str = time.strftime("%H:%M", time.localtime()), default_message: str = "Hello World"):
    app = QApplication(sys.argv)

    try:
        due = QTime.currentTime()
        # if len(sys.argv) < 2:
        #     raise ValueError
        if len(sys.argv) < 2 and default_time:
            hours, mins = default_time.split(":")
        else:
            hours, mins = sys.argv[1].split(":")
        due = QTime(int(hours), int(mins))
        if not due.isValid():
            raise ValueError
        if len(sys.argv) > 2:
            message = " ".join(sys.argv[2:])
        else:
            message = default_message
    except ValueError:
        message = "Usage: alert.pyw HH:MM [optional message]"  # 24hr clock

    while QTime.currentTime() < due:
        time.sleep(20)  # 20 seconds

    label = QLabel("<font color=red size=72><b>" + message + "</b></font>")
    label.setWindowFlags(Qt.SplashScreen)
    label.show()
    QTimer.singleShot(60000, app.quit)  # 1 minute
    app.exec_()


if __name__ == '__main__':
    main()
