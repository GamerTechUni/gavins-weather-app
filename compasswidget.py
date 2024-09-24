import sys
from PySide6.QtCore import Qt, Signal, Slot, Property, QSize, QPoint
from PySide6.QtWidgets import QWidget, QApplication, QSpinBox, QVBoxLayout
from PySide6.QtGui import QPainter, QPalette, QFont, QFontMetricsF, QPen, QPolygon


class CompassWidget(QWidget):
    """
    I do not know how to document this, just ported it
    to QT6, removing features that
    didn't work
    """

    angleChanged = Signal(float)

    def __init__(self, parent=None):

        QWidget.__init__(self, parent)

        self._angle = 0.0
        self._margins = 10
        self._point_text = {0: "N", 45: "NE", 90: "E", 135: "SE", 180: "S",
                            225: "SW", 270: "W", 315: "NW"}

    def paintEvent(self, event):

        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # painter.fillRect(event.rect(), self.palette().brush(QPalette.Window))
        self.drawMarkings(painter)
        self.drawNeedle(painter)

        painter.end()

    def drawMarkings(self, painter):

        painter.save()
        painter.translate(self.width()/2, self.height()/2)
        scale = min((self.width() - self._margins)/120.0,
                    (self.height() - self._margins)/120.0)
        painter.scale(scale, scale)

        font = QFont(self.font())
        font.setPixelSize(10)

        painter.setFont(font)
        painter.setPen(self.palette().color(QPalette.Shadow))

        i = 0
        while i < 360:

            if i % 45 == 0:
                painter.drawLine(0, -40, 0, -50)
            else:
                painter.drawLine(0, -45, 0, -50)

            painter.rotate(15)
            i += 15

        painter.restore()

    def drawNeedle(self, painter):

        painter.save()
        painter.translate(self.width()/2, self.height()/2)
        painter.rotate(self._angle)
        scale = min((self.width() - self._margins)/120.0,
                    (self.height() - self._margins)/120.0)
        painter.scale(scale, scale)

        painter.setPen(QPen(Qt.NoPen))
        painter.setBrush(self.palette().brush(QPalette.Shadow))

        painter.drawPolygon(
            QPolygon([QPoint(-10, 0), QPoint(0, -45), QPoint(10, 0),
                      QPoint(0, 45), QPoint(-10, 0)])
        )

        painter.setBrush(self.palette().brush(QPalette.Highlight))

        painter.drawPolygon(
            QPolygon([QPoint(-5, -25), QPoint(0, -45), QPoint(5, -25),
                      QPoint(0, -30), QPoint(-5, -25)])
        )

        painter.restore()

    def sizeHint(self):

        return QSize(150, 150)

    def angle(self):
        return self._angle

    @Slot(float)
    def setAngle(self, angle):

        if angle != self._angle:
            self._angle = angle
            self.angleChanged.emit(angle)
            self.update()

    angle = Property(float, angle, setAngle)


if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = QWidget()
    compass = CompassWidget()
    spinBox = QSpinBox()
    spinBox.setRange(0, 359)
    spinBox.valueChanged.connect(compass.setAngle)

    layout = QVBoxLayout()
    layout.addWidget(compass)
    layout.addWidget(spinBox)
    window.setLayout(layout)

    window.show()
    sys.exit(app.exec())
