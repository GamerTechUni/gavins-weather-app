""" The '__main__' file that the program is run from
This file's only purpose is to run functions and classes from
the other files, which starts the program up.

'qtpy', 'PySide6' and 'qdarkstyle' are required modules that need
to be installed
"""

import sys
import os
import qdarkstyle
from qtpy.QtWidgets import QApplication, QMainWindow
from gui import MainWindow

if __name__ == '__main__':
    os.environ['QT_API'] = 'pyside6'
    app = QApplication(sys.argv)
    weather_app = MainWindow()
    app.setStyleSheet(qdarkstyle.load_stylesheet())
    weather_app.show()
    sys.exit(app.exec())
