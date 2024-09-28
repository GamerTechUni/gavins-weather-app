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
