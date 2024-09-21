import sys
from PySide6.QtWidgets import QApplication
from gui import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    weather_app = MainWindow()
    weather_app.show()
    sys.exit(app.exec())
