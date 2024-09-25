# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QProgressBar, QPushButton, QScrollArea,
    QSizePolicy, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

from compasswidget import CompassWidget
from graphplot import GraphPlot

class Ui_WeatherApp(object):
    def setupUi(self, WeatherApp):
        if not WeatherApp.objectName():
            WeatherApp.setObjectName(u"WeatherApp")
        WeatherApp.resize(975, 813)
        WeatherApp.setStyleSheet(u"\n"
"* {\n"
"  padding: 0px;\n"
"  margin: 0px;\n"
"  border: 0px;\n"
"  border-style: none;\n"
"  border-image: none;\n"
"  outline: 0;\n"
"}\n"
"\n"
"/* specific reset for elements inside QToolBar */\n"
"QToolBar * {\n"
"  margin: 0px;\n"
"  padding: 0px;\n"
"}\n"
"\n"
"/* QWidget ----------------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QWidget {\n"
"  background-color: #19232D;\n"
"  border: 0px solid #455364;\n"
"  padding: 0px;\n"
"  color: #DFE1E2;\n"
"  selection-background-color: #346792;\n"
"  selection-color: #DFE1E2;\n"
"}\n"
"\n"
"QWidget:disabled {\n"
"  background-color: #19232D;\n"
"  color: #788D9C;\n"
"  selection-background-color: #26486B;\n"
"  selection-color: #788D9C;\n"
"}\n"
"\n"
"QWidget::item:selected {\n"
"  background-color: #346792;\n"
"}\n"
"\n"
"QWidget::item:hover:!selected {\n"
"  background-color: #1A72BB;\n"
"}\n"
"\n"
"/* QMainWindow --------------------------------------------"
                        "----------------\n"
"\n"
"This adjusts the splitter in the dock widget, not qsplitter\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qmainwindow\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QMainWindow::separator {\n"
"  background-color: #455364;\n"
"  border: 0px solid #19232D;\n"
"  spacing: 0px;\n"
"  padding: 2px;\n"
"}\n"
"\n"
"QMainWindow::separator:hover {\n"
"  background-color: #60798B;\n"
"  border: 0px solid #1A72BB;\n"
"}\n"
"\n"
"QMainWindow::separator:horizontal {\n"
"  width: 5px;\n"
"  margin-top: 2px;\n"
"  margin-bottom: 2px;\n"
"  image: url(\":/qss_icons/dark/rc/toolbar_separator_vertical.png\");\n"
"}\n"
"\n"
"QMainWindow::separator:vertical {\n"
"  height: 5px;\n"
"  margin-left: 2px;\n"
"  margin-right: 2px;\n"
"  image: url(\":/qss_icons/dark/rc/toolbar_separator_horizontal.png\");\n"
"}\n"
"\n"
"/* QToolTip ---------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples."
                        "html#customizing-qtooltip\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QToolTip {\n"
"  background-color: #346792;\n"
"  color: #DFE1E2;\n"
"  /* If you remove the border property, background stops working on Windows */\n"
"  border: none;\n"
"  /* Remove padding, for fix combo box tooltip */\n"
"  padding: 0px;\n"
"  /* Remove opacity, fix #174 - may need to use RGBA */\n"
"}\n"
"\n"
"/* QStatusBar -------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qstatusbar\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QStatusBar {\n"
"  border: 1px solid #455364;\n"
"  /* Fixes Spyder #9120, #9121 */\n"
"  background: #455364;\n"
"  /* Fixes #205, white vertical borders separating items */\n"
"}\n"
"\n"
"QStatusBar::item {\n"
"  border: none;\n"
"}\n"
"\n"
"QStatusBar QToolTip {\n"
"  background-color: #1A72BB;\n"
"  border: 1px solid #19232D;\n"
"  col"
                        "or: #19232D;\n"
"  /* Remove padding, for fix combo box tooltip */\n"
"  padding: 0px;\n"
"  /* Reducing transparency to read better */\n"
"  opacity: 230;\n"
"}\n"
"\n"
"QStatusBar QLabel {\n"
"  /* Fixes Spyder #9120, #9121 */\n"
"  background: transparent;\n"
"}\n"
"\n"
"/* QCheckBox --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qcheckbox\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QCheckBox {\n"
"  background-color: #19232D;\n"
"  color: #DFE1E2;\n"
"  spacing: 4px;\n"
"  outline: none;\n"
"  padding-top: 4px;\n"
"  padding-bottom: 4px;\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"  border: none;\n"
"}\n"
"\n"
"QCheckBox QWidget:disabled {\n"
"  background-color: #19232D;\n"
"  color: #788D9C;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"  margin-left: 2px;\n"
"  height: 14px;\n"
"  width: 14px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"  image: url(\":/qss_icons/dark/rc/chec"
                        "kbox_unchecked.png\");\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover, QCheckBox::indicator:unchecked:focus, QCheckBox::indicator:unchecked:pressed {\n"
"  border: none;\n"
"  image: url(\":/qss_icons/dark/rc/checkbox_unchecked_focus.png\");\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:disabled {\n"
"  image: url(\":/qss_icons/dark/rc/checkbox_unchecked_disabled.png\");\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"  image: url(\":/qss_icons/dark/rc/checkbox_checked.png\");\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover, QCheckBox::indicator:checked:focus, QCheckBox::indicator:checked:pressed {\n"
"  border: none;\n"
"  image: url(\":/qss_icons/dark/rc/checkbox_checked_focus.png\");\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:disabled {\n"
"  image: url(\":/qss_icons/dark/rc/checkbox_checked_disabled.png\");\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate {\n"
"  image: url(\":/qss_icons/dark/rc/checkbox_indeterminate.png\");\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate:disabled {\n"
"  ima"
                        "ge: url(\":/qss_icons/dark/rc/checkbox_indeterminate_disabled.png\");\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate:focus, QCheckBox::indicator:indeterminate:hover, QCheckBox::indicator:indeterminate:pressed {\n"
"  image: url(\":/qss_icons/dark/rc/checkbox_indeterminate_focus.png\");\n"
"}\n"
"\n"
"/* QGroupBox --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qgroupbox\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QGroupBox {\n"
"  font-weight: bold;\n"
"  border: 1px solid #455364;\n"
"  border-radius: 4px;\n"
"  padding: 2px;\n"
"  margin-top: 6px;\n"
"  margin-bottom: 4px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"  subcontrol-origin: margin;\n"
"  subcontrol-position: top left;\n"
"  left: 4px;\n"
"  padding-left: 2px;\n"
"  padding-right: 4px;\n"
"  padding-top: -4px;\n"
"}\n"
"\n"
"QGroupBox::indicator {\n"
"  margin-left: 2px;\n"
"  margin-top: 2px;\n"
"  padding: 0;\n"
"  he"
                        "ight: 14px;\n"
"  width: 14px;\n"
"}\n"
"\n"
"QGroupBox::indicator:unchecked {\n"
"  border: none;\n"
"  image: url(\":/qss_icons/dark/rc/checkbox_unchecked.png\");\n"
"}\n"
"\n"
"QGroupBox::indicator:unchecked:hover, QGroupBox::indicator:unchecked:focus, QGroupBox::indicator:unchecked:pressed {\n"
"  border: none;\n"
"  image: url(\":/qss_icons/dark/rc/checkbox_unchecked_focus.png\");\n"
"}\n"
"\n"
"QGroupBox::indicator:unchecked:disabled {\n"
"  image: url(\":/qss_icons/dark/rc/checkbox_unchecked_disabled.png\");\n"
"}\n"
"\n"
"QGroupBox::indicator:checked {\n"
"  border: none;\n"
"  image: url(\":/qss_icons/dark/rc/checkbox_checked.png\");\n"
"}\n"
"\n"
"QGroupBox::indicator:checked:hover, QGroupBox::indicator:checked:focus, QGroupBox::indicator:checked:pressed {\n"
"  border: none;\n"
"  image: url(\":/qss_icons/dark/rc/checkbox_checked_focus.png\");\n"
"}\n"
"\n"
"QGroupBox::indicator:checked:disabled {\n"
"  image: url(\":/qss_icons/dark/rc/checkbox_checked_disabled.png\");\n"
"}\n"
"\n"
"/* QRadioButton"
                        " -----------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qradiobutton\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QRadioButton {\n"
"  background-color: #19232D;\n"
"  color: #DFE1E2;\n"
"  spacing: 4px;\n"
"  padding-top: 4px;\n"
"  padding-bottom: 4px;\n"
"  border: none;\n"
"  outline: none;\n"
"}\n"
"\n"
"QRadioButton:focus {\n"
"  border: none;\n"
"}\n"
"\n"
"QRadioButton:disabled {\n"
"  background-color: #19232D;\n"
"  color: #788D9C;\n"
"  border: none;\n"
"  outline: none;\n"
"}\n"
"\n"
"QRadioButton QWidget {\n"
"  background-color: #19232D;\n"
"  color: #DFE1E2;\n"
"  spacing: 0px;\n"
"  padding: 0px;\n"
"  outline: none;\n"
"  border: none;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"  border: none;\n"
"  outline: none;\n"
"  margin-left: 2px;\n"
"  height: 14px;\n"
"  width: 14px;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"  image: url(\":/qss_icons/dark/rc/radio_un"
                        "checked.png\");\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:hover, QRadioButton::indicator:unchecked:focus, QRadioButton::indicator:unchecked:pressed {\n"
"  border: none;\n"
"  outline: none;\n"
"  image: url(\":/qss_icons/dark/rc/radio_unchecked_focus.png\");\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:disabled {\n"
"  image: url(\":/qss_icons/dark/rc/radio_unchecked_disabled.png\");\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"  border: none;\n"
"  outline: none;\n"
"  image: url(\":/qss_icons/dark/rc/radio_checked.png\");\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:hover, QRadioButton::indicator:checked:focus, QRadioButton::indicator:checked:pressed {\n"
"  border: none;\n"
"  outline: none;\n"
"  image: url(\":/qss_icons/dark/rc/radio_checked_focus.png\");\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:disabled {\n"
"  outline: none;\n"
"  image: url(\":/qss_icons/dark/rc/radio_checked_disabled.png\");\n"
"}\n"
"\n"
"/* QMenuBar --------------------------------------------------------"
                        "-------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qmenubar\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QMenuBar {\n"
"  background-color: #455364;\n"
"  padding: 2px;\n"
"  border: 1px solid #19232D;\n"
"  color: #DFE1E2;\n"
"  selection-background-color: #1A72BB;\n"
"}\n"
"\n"
"QMenuBar:focus {\n"
"  border: 1px solid #346792;\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"  background: transparent;\n"
"  padding: 4px;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"  padding: 4px;\n"
"  background: transparent;\n"
"  border: 0px solid #455364;\n"
"  background-color: #1A72BB;\n"
"}\n"
"\n"
"QMenuBar::item:pressed {\n"
"  padding: 4px;\n"
"  border: 0px solid #455364;\n"
"  background-color: #1A72BB;\n"
"  color: #DFE1E2;\n"
"  margin-bottom: 0px;\n"
"  padding-bottom: 0px;\n"
"}\n"
"\n"
"/* QMenu ------------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qmenu\n"
"\n"
"---"
                        "------------------------------------------------------------------------ */\n"
"QMenu {\n"
"  border: 0px solid #455364;\n"
"  color: #DFE1E2;\n"
"  margin: 0px;\n"
"  background-color: #37414F;\n"
"  selection-background-color: #1A72BB;\n"
"}\n"
"\n"
"QMenu::separator {\n"
"  height: 1px;\n"
"  background-color: #60798B;\n"
"  color: #DFE1E2;\n"
"}\n"
"\n"
"QMenu::item {\n"
"  background-color: #37414F;\n"
"  padding: 4px 24px 4px 28px;\n"
"  /* Reserve space for selection border */\n"
"  border: 1px transparent #455364;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"  color: #DFE1E2;\n"
"  background-color: #1A72BB;\n"
"}\n"
"\n"
"QMenu::item:pressed {\n"
"  background-color: #1A72BB;\n"
"}\n"
"\n"
"QMenu::icon {\n"
"  padding-left: 10px;\n"
"  width: 14px;\n"
"  height: 14px;\n"
"}\n"
"\n"
"QMenu::indicator {\n"
"  padding-left: 8px;\n"
"  width: 12px;\n"
"  height: 12px;\n"
"  /* non-exclusive indicator = check box style indicator (see QActionGroup::setExclusive) */\n"
"  /* exclusive indicator = radio button s"
                        "tyle indicator (see QActionGroup::setExclusive) */\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:unchecked {\n"
"  image: url(\":/qss_icons/dark/rc/checkbox_unchecked.png\");\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:unchecked:hover, QMenu::indicator:non-exclusive:unchecked:focus, QMenu::indicator:non-exclusive:unchecked:pressed {\n"
"  border: none;\n"
"  image: url(\":/qss_icons/dark/rc/checkbox_unchecked_focus.png\");\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:unchecked:disabled {\n"
"  image: url(\":/qss_icons/dark/rc/checkbox_unchecked_disabled.png\");\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:checked {\n"
"  image: url(\":/qss_icons/dark/rc/checkbox_checked.png\");\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:checked:hover, QMenu::indicator:non-exclusive:checked:focus, QMenu::indicator:non-exclusive:checked:pressed {\n"
"  border: none;\n"
"  image: url(\":/qss_icons/dark/rc/checkbox_checked_focus.png\");\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:checked:disabled {\n"
"  image: url(\":/qs"
                        "s_icons/dark/rc/checkbox_checked_disabled.png\");\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:indeterminate {\n"
"  image: url(\":/qss_icons/dark/rc/checkbox_indeterminate.png\");\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:indeterminate:disabled {\n"
"  image: url(\":/qss_icons/dark/rc/checkbox_indeterminate_disabled.png\");\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:indeterminate:focus, QMenu::indicator:non-exclusive:indeterminate:hover, QMenu::indicator:non-exclusive:indeterminate:pressed {\n"
"  image: url(\":/qss_icons/dark/rc/checkbox_indeterminate_focus.png\");\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:unchecked {\n"
"  image: url(\":/qss_icons/dark/rc/radio_unchecked.png\");\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:unchecked:hover, QMenu::indicator:exclusive:unchecked:focus, QMenu::indicator:exclusive:unchecked:pressed {\n"
"  border: none;\n"
"  outline: none;\n"
"  image: url(\":/qss_icons/dark/rc/radio_unchecked_focus.png\");\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:unchecked:disabled {\n"
""
                        "  image: url(\":/qss_icons/dark/rc/radio_unchecked_disabled.png\");\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:checked {\n"
"  border: none;\n"
"  outline: none;\n"
"  image: url(\":/qss_icons/dark/rc/radio_checked.png\");\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:checked:hover, QMenu::indicator:exclusive:checked:focus, QMenu::indicator:exclusive:checked:pressed {\n"
"  border: none;\n"
"  outline: none;\n"
"  image: url(\":/qss_icons/dark/rc/radio_checked_focus.png\");\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:checked:disabled {\n"
"  outline: none;\n"
"  image: url(\":/qss_icons/dark/rc/radio_checked_disabled.png\");\n"
"}\n"
"\n"
"QMenu::right-arrow {\n"
"  margin: 5px;\n"
"  padding-left: 12px;\n"
"  image: url(\":/qss_icons/dark/rc/arrow_right.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"}\n"
"\n"
"/* QAbstractItemView ------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qcombobox\n"
"\n"
"-----------------------------------------"
                        "---------------------------------- */\n"
"QAbstractItemView {\n"
"  alternate-background-color: #19232D;\n"
"  color: #DFE1E2;\n"
"  border: 1px solid #455364;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QAbstractItemView QLineEdit {\n"
"  padding: 2px;\n"
"}\n"
"\n"
"/* QAbstractScrollArea ----------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qabstractscrollarea\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QAbstractScrollArea {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #455364;\n"
"  border-radius: 4px;\n"
"  /* fix #159 */\n"
"  padding: 2px;\n"
"  /* remove min-height to fix #244 */\n"
"  color: #DFE1E2;\n"
"}\n"
"\n"
"QAbstractScrollArea:disabled {\n"
"  color: #788D9C;\n"
"}\n"
"\n"
"/* QScrollArea ------------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QScrollArea QWidget QWidget:disa"
                        "bled {\n"
"  background-color: #19232D;\n"
"}\n"
"\n"
"/* QScrollBar -------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qscrollbar\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QScrollBar:horizontal {\n"
"  height: 16px;\n"
"  margin: 2px 16px 2px 16px;\n"
"  border: 1px solid #455364;\n"
"  border-radius: 4px;\n"
"  background-color: #19232D;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"  background-color: #19232D;\n"
"  width: 16px;\n"
"  margin: 16px 2px 16px 2px;\n"
"  border: 1px solid #455364;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"  background-color: #60798B;\n"
"  border: 1px solid #455364;\n"
"  border-radius: 4px;\n"
"  min-width: 8px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"  background-color: #346792;\n"
"  border: #346792;\n"
"  border-radius: 4px;\n"
"  min-width: 8px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:focus {\n"
""
                        "  border: 1px solid #1A72BB;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"  background-color: #60798B;\n"
"  border: 1px solid #455364;\n"
"  min-height: 8px;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"  background-color: #346792;\n"
"  border: #346792;\n"
"  border-radius: 4px;\n"
"  min-height: 8px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:focus {\n"
"  border: 1px solid #1A72BB;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"  margin: 0px 0px 0px 0px;\n"
"  border-image: url(\":/qss_icons/dark/rc/arrow_right_disabled.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: right;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover, QScrollBar::add-line:horizontal:on {\n"
"  border-image: url(\":/qss_icons/dark/rc/arrow_right.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: right;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"  margin: 3px 0px 3px"
                        " 0px;\n"
"  border-image: url(\":/qss_icons/dark/rc/arrow_down_disabled.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on {\n"
"  border-image: url(\":/qss_icons/dark/rc/arrow_down.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"  margin: 0px 3px 0px 3px;\n"
"  border-image: url(\":/qss_icons/dark/rc/arrow_left_disabled.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: left;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on {\n"
"  border-image: url(\":/qss_icons/dark/rc/arrow_left.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: left;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"  margin"
                        ": 3px 0px 3px 0px;\n"
"  border-image: url(\":/qss_icons/dark/rc/arrow_up_disabled.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover, QScrollBar::sub-line:vertical:on {\n"
"  border-image: url(\":/qss_icons/dark/rc/arrow_up.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal {\n"
"  background: none;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"  background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"  background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"  background: none;\n"
"}\n"
"\n"
"/* QTextEdit --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customiz"
                        "ing-specific-widgets\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QTextEdit {\n"
"  background-color: #19232D;\n"
"  color: #DFE1E2;\n"
"  border-radius: 4px;\n"
"  border: 1px solid #455364;\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"  border: 1px solid #1A72BB;\n"
"}\n"
"\n"
"QTextEdit:selected {\n"
"  background: #346792;\n"
"  color: #455364;\n"
"}\n"
"\n"
"/* QPlainTextEdit ---------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QPlainTextEdit {\n"
"  background-color: #19232D;\n"
"  color: #DFE1E2;\n"
"  border-radius: 4px;\n"
"  border: 1px solid #455364;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"  border: 1px solid #1A72BB;\n"
"}\n"
"\n"
"QPlainTextEdit:selected {\n"
"  background: #346792;\n"
"  color: #455364;\n"
"}\n"
"\n"
"/* QSizeGrip --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-"
                        "qsizegrip\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QSizeGrip {\n"
"  background: transparent;\n"
"  width: 12px;\n"
"  height: 12px;\n"
"  image: url(\":/qss_icons/dark/rc/window_grip.png\");\n"
"}\n"
"\n"
"/* QStackedWidget ---------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QStackedWidget {\n"
"  padding: 2px;\n"
"  border: 1px solid #455364;\n"
"  border: 1px solid #19232D;\n"
"}\n"
"\n"
"/* QToolBar ---------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtoolbar\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QToolBar {\n"
"  background-color: #455364;\n"
"  border-bottom: 1px solid #19232D;\n"
"  padding: 1px;\n"
"  font-weight: bold;\n"
"  spacing: 2px;\n"
"}\n"
"\n"
"QToolBar:disabled {\n"
"  /* Fixes #272 */\n"
"  background-color: #455"
                        "364;\n"
"}\n"
"\n"
"QToolBar::handle:horizontal {\n"
"  width: 16px;\n"
"  image: url(\":/qss_icons/dark/rc/toolbar_move_horizontal.png\");\n"
"}\n"
"\n"
"QToolBar::handle:vertical {\n"
"  height: 16px;\n"
"  image: url(\":/qss_icons/dark/rc/toolbar_move_vertical.png\");\n"
"}\n"
"\n"
"QToolBar::separator:horizontal {\n"
"  width: 16px;\n"
"  image: url(\":/qss_icons/dark/rc/toolbar_separator_horizontal.png\");\n"
"}\n"
"\n"
"QToolBar::separator:vertical {\n"
"  height: 16px;\n"
"  image: url(\":/qss_icons/dark/rc/toolbar_separator_vertical.png\");\n"
"}\n"
"\n"
"QToolButton#qt_toolbar_ext_button {\n"
"  background: #455364;\n"
"  border: 0px;\n"
"  color: #DFE1E2;\n"
"  image: url(\":/qss_icons/dark/rc/arrow_right.png\");\n"
"}\n"
"\n"
"/* QAbstractSpinBox -------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QAbstractSpinBox {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #455364;\n"
"  color: #DFE1E2;\n"
""
                        "  /* This fixes 103, 111 */\n"
"  padding-top: 2px;\n"
"  /* This fixes 103, 111 */\n"
"  padding-bottom: 2px;\n"
"  padding-left: 4px;\n"
"  padding-right: 4px;\n"
"  border-radius: 4px;\n"
"  /* min-width: 5px; removed to fix 109 */\n"
"}\n"
"\n"
"QAbstractSpinBox:up-button {\n"
"  background-color: transparent #19232D;\n"
"  subcontrol-origin: border;\n"
"  subcontrol-position: top right;\n"
"  border-left: 1px solid #455364;\n"
"  border-bottom: 1px solid #455364;\n"
"  border-top-left-radius: 0;\n"
"  border-bottom-left-radius: 0;\n"
"  margin: 1px;\n"
"  width: 12px;\n"
"  margin-bottom: -1px;\n"
"}\n"
"\n"
"QAbstractSpinBox::up-arrow, QAbstractSpinBox::up-arrow:disabled, QAbstractSpinBox::up-arrow:off {\n"
"  image: url(\":/qss_icons/dark/rc/arrow_up_disabled.png\");\n"
"  height: 8px;\n"
"  width: 8px;\n"
"}\n"
"\n"
"QAbstractSpinBox::up-arrow:hover {\n"
"  image: url(\":/qss_icons/dark/rc/arrow_up.png\");\n"
"}\n"
"\n"
"QAbstractSpinBox:down-button {\n"
"  background-color: transparent #19232D;\n"
"  "
                        "subcontrol-origin: border;\n"
"  subcontrol-position: bottom right;\n"
"  border-left: 1px solid #455364;\n"
"  border-top: 1px solid #455364;\n"
"  border-top-left-radius: 0;\n"
"  border-bottom-left-radius: 0;\n"
"  margin: 1px;\n"
"  width: 12px;\n"
"  margin-top: -1px;\n"
"}\n"
"\n"
"QAbstractSpinBox::down-arrow, QAbstractSpinBox::down-arrow:disabled, QAbstractSpinBox::down-arrow:off {\n"
"  image: url(\":/qss_icons/dark/rc/arrow_down_disabled.png\");\n"
"  height: 8px;\n"
"  width: 8px;\n"
"}\n"
"\n"
"QAbstractSpinBox::down-arrow:hover {\n"
"  image: url(\":/qss_icons/dark/rc/arrow_down.png\");\n"
"}\n"
"\n"
"QAbstractSpinBox:hover {\n"
"  border: 1px solid #346792;\n"
"  color: #DFE1E2;\n"
"}\n"
"\n"
"QAbstractSpinBox:focus {\n"
"  border: 1px solid #1A72BB;\n"
"}\n"
"\n"
"QAbstractSpinBox:selected {\n"
"  background: #346792;\n"
"  color: #455364;\n"
"}\n"
"\n"
"/* ------------------------------------------------------------------------ */\n"
"/* DISPLAYS ------------------------------------------------"
                        "--------------- */\n"
"/* ------------------------------------------------------------------------ */\n"
"/* QLabel -----------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qframe\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QLabel {\n"
"  background-color: #19232D;\n"
"  border: 0px solid #455364;\n"
"  padding: 2px;\n"
"  margin: 0px;\n"
"  color: #DFE1E2;\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"  background-color: #19232D;\n"
"  border: 0px solid #455364;\n"
"  color: #788D9C;\n"
"}\n"
"\n"
"/* QTextBrowser -----------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qabstractscrollarea\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QTextBrowser {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #455364;\n"
"  color: #DFE1E2;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QT"
                        "extBrowser:disabled {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #455364;\n"
"  color: #788D9C;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QTextBrowser:hover, QTextBrowser:!hover, QTextBrowser:selected, QTextBrowser:pressed {\n"
"  border: 1px solid #455364;\n"
"}\n"
"\n"
"/* QGraphicsView ----------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QGraphicsView {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #455364;\n"
"  color: #DFE1E2;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QGraphicsView:disabled {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #455364;\n"
"  color: #788D9C;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QGraphicsView:hover, QGraphicsView:!hover, QGraphicsView:selected, QGraphicsView:pressed {\n"
"  border: 1px solid #455364;\n"
"}\n"
"\n"
"/* QCalendarWidget --------------------------------------------------------\n"
"\n"
"------------------------------------------------"
                        "--------------------------- */\n"
"QCalendarWidget {\n"
"  border: 1px solid #455364;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QCalendarWidget:disabled {\n"
"  background-color: #19232D;\n"
"  color: #788D9C;\n"
"}\n"
"\n"
"/* QLCDNumber -------------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QLCDNumber {\n"
"  background-color: #19232D;\n"
"  color: #DFE1E2;\n"
"}\n"
"\n"
"QLCDNumber:disabled {\n"
"  background-color: #19232D;\n"
"  color: #788D9C;\n"
"}\n"
"\n"
"/* QProgressBar -----------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qprogressbar\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QProgressBar {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #455364;\n"
"  color: #DFE1E2;\n"
"  border-radius: 4px;\n"
"  text-align: center;\n"
"}\n"
"\n"
"QProgressBar:disabled {\n"
"  backgrou"
                        "nd-color: #19232D;\n"
"  border: 1px solid #455364;\n"
"  color: #788D9C;\n"
"  border-radius: 4px;\n"
"  text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"  background-color: #346792;\n"
"  color: #19232D;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QProgressBar::chunk:disabled {\n"
"  background-color: #26486B;\n"
"  color: #788D9C;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"/* ------------------------------------------------------------------------ */\n"
"/* BUTTONS ---------------------------------------------------------------- */\n"
"/* ------------------------------------------------------------------------ */\n"
"/* QPushButton ------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qpushbutton\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QPushButton {\n"
"  background-color: #455364;\n"
"  color: #DFE1E2;\n"
"  border-radius: 4px;\n"
"  padding: 2px;\n"
"  outline: none;\n"
" "
                        " border: none;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"  background-color: #455364;\n"
"  color: #788D9C;\n"
"  border-radius: 4px;\n"
"  padding: 2px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"  background-color: #60798B;\n"
"  border-radius: 4px;\n"
"  padding: 2px;\n"
"  outline: none;\n"
"}\n"
"\n"
"QPushButton:checked:disabled {\n"
"  background-color: #60798B;\n"
"  color: #788D9C;\n"
"  border-radius: 4px;\n"
"  padding: 2px;\n"
"  outline: none;\n"
"}\n"
"\n"
"QPushButton:checked:selected {\n"
"  background: #60798B;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #54687A;\n"
"  color: #DFE1E2;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: #60798B;\n"
"}\n"
"\n"
"QPushButton:selected {\n"
"  background: #60798B;\n"
"  color: #DFE1E2;\n"
"}\n"
"\n"
"QPushButton::menu-indicator {\n"
"  subcontrol-origin: padding;\n"
"  subcontrol-position: bottom right;\n"
"  bottom: 4px;\n"
"}\n"
"\n"
"QDialogButtonBox QPushButton {\n"
"  /* Issue #194 #248 - Special case of QPushButton inside"
                        " dialogs, for better UI */\n"
"  min-width: 80px;\n"
"}\n"
"\n"
"/* QToolButton ------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtoolbutton\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QToolButton {\n"
"  background-color: #455364;\n"
"  color: #DFE1E2;\n"
"  border-radius: 4px;\n"
"  padding: 2px;\n"
"  outline: none;\n"
"  border: none;\n"
"  /* The subcontrols below are used only in the DelayedPopup mode */\n"
"  /* The subcontrols below are used only in the MenuButtonPopup mode */\n"
"  /* The subcontrol below is used only in the InstantPopup or DelayedPopup mode */\n"
"}\n"
"\n"
"QToolButton:disabled {\n"
"  background-color: #455364;\n"
"  color: #788D9C;\n"
"  border-radius: 4px;\n"
"  padding: 2px;\n"
"}\n"
"\n"
"QToolButton:checked {\n"
"  background-color: #60798B;\n"
"  border-radius: 4px;\n"
"  padding: 2px;\n"
"  outline: none;\n"
"}\n"
"\n"
"QToolButton:checked:disabled"
                        " {\n"
"  background-color: #60798B;\n"
"  color: #788D9C;\n"
"  border-radius: 4px;\n"
"  padding: 2px;\n"
"  outline: none;\n"
"}\n"
"\n"
"QToolButton:checked:hover {\n"
"  background-color: #54687A;\n"
"  color: #DFE1E2;\n"
"}\n"
"\n"
"QToolButton:checked:pressed {\n"
"  background-color: #60798B;\n"
"}\n"
"\n"
"QToolButton:checked:selected {\n"
"  background: #60798B;\n"
"  color: #DFE1E2;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"  background-color: #54687A;\n"
"  color: #DFE1E2;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"  background-color: #60798B;\n"
"}\n"
"\n"
"QToolButton:selected {\n"
"  background: #60798B;\n"
"  color: #DFE1E2;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"0\"] {\n"
"  /* Only for DelayedPopup */\n"
"  padding-right: 2px;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"1\"] {\n"
"  /* Only for MenuButtonPopup */\n"
"  padding-right: 20px;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"1\"]::menu-button {\n"
"  border: none;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"1\"]::menu-button:hover {\n"
"  border: none;\n"
""
                        "  border-left: 1px solid #455364;\n"
"  border-radius: 0;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"2\"] {\n"
"  /* Only for InstantPopup */\n"
"  padding-right: 2px;\n"
"}\n"
"\n"
"QToolButton::menu-button {\n"
"  padding: 2px;\n"
"  border-radius: 4px;\n"
"  width: 12px;\n"
"  border: none;\n"
"  outline: none;\n"
"}\n"
"\n"
"QToolButton::menu-button:hover {\n"
"  border: 1px solid #346792;\n"
"}\n"
"\n"
"QToolButton::menu-button:checked:hover {\n"
"  border: 1px solid #346792;\n"
"}\n"
"\n"
"QToolButton::menu-indicator {\n"
"  image: url(\":/qss_icons/dark/rc/arrow_down.png\");\n"
"  height: 8px;\n"
"  width: 8px;\n"
"  top: 0;\n"
"  /* Exclude a shift for better image */\n"
"  left: -2px;\n"
"  /* Shift it a bit */\n"
"}\n"
"\n"
"QToolButton::menu-arrow {\n"
"  image: url(\":/qss_icons/dark/rc/arrow_down.png\");\n"
"  height: 8px;\n"
"  width: 8px;\n"
"}\n"
"\n"
"QToolButton::menu-arrow:hover {\n"
"  image: url(\":/qss_icons/dark/rc/arrow_down_focus.png\");\n"
"}\n"
"\n"
"/* QCommandLinkButton ---------------"
                        "--------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QCommandLinkButton {\n"
"  background-color: transparent;\n"
"  border: 1px solid #455364;\n"
"  color: #DFE1E2;\n"
"  border-radius: 4px;\n"
"  padding: 0px;\n"
"  margin: 0px;\n"
"}\n"
"\n"
"QCommandLinkButton:disabled {\n"
"  background-color: transparent;\n"
"  color: #788D9C;\n"
"}\n"
"\n"
"/* ------------------------------------------------------------------------ */\n"
"/* INPUTS - NO FIELDS ----------------------------------------------------- */\n"
"/* ------------------------------------------------------------------------ */\n"
"/* QComboBox --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qcombobox\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QComboBox {\n"
"  border: 1px solid #455364;\n"
"  border-radius: 4px;\n"
"  selection-background-col"
                        "or: #346792;\n"
"  padding-left: 4px;\n"
"  padding-right: 4px;\n"
"  /* padding-right = 36; 4 + 16*2 See scrollbar size */\n"
"  /* changed to 4px to fix #239 */\n"
"  /* Fixes #103, #111 */\n"
"  min-height: 1.5em;\n"
"  /* padding-top: 2px;     removed to fix #132 */\n"
"  /* padding-bottom: 2px;  removed to fix #132 */\n"
"  /* min-width: 75px;      removed to fix #109 */\n"
"  /* Needed to remove indicator - fix #132 */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"  border: 1px solid #455364;\n"
"  border-radius: 0;\n"
"  background-color: #19232D;\n"
"  selection-background-color: #346792;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView:hover {\n"
"  background-color: #19232D;\n"
"  color: #DFE1E2;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView:selected {\n"
"  background: #346792;\n"
"  color: #455364;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView:alternate {\n"
"  background: #19232D;\n"
"}\n"
"\n"
"QComboBox:disabled {\n"
"  background-color: #19232D;\n"
"  color: #788D9C;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
""
                        "  border: 1px solid #346792;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"  border: 1px solid #1A72BB;\n"
"}\n"
"\n"
"QComboBox:on {\n"
"  selection-background-color: #346792;\n"
"}\n"
"\n"
"QComboBox::indicator {\n"
"  border: none;\n"
"  border-radius: 0;\n"
"  background-color: transparent;\n"
"  selection-background-color: transparent;\n"
"  color: transparent;\n"
"  selection-color: transparent;\n"
"  /* Needed to remove indicator - fix #132 */\n"
"}\n"
"\n"
"QComboBox::indicator:alternate {\n"
"  background: #19232D;\n"
"}\n"
"\n"
"QComboBox::item {\n"
"  /* Remove to fix #282, #285 and MR #288*/\n"
"  /*&:checked {\n"
"            font-weight: bold;\n"
"        }\n"
"\n"
"        &:selected {\n"
"            border: 0px solid transparent;\n"
"        }\n"
"        */\n"
"}\n"
"\n"
"QComboBox::item:alternate {\n"
"  background: #19232D;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"  subcontrol-origin: padding;\n"
"  subcontrol-position: top right;\n"
"  width: 12px;\n"
"  border-left: 1px solid #455364;\n"
"}\n"
"\n"
""
                        "QComboBox::down-arrow {\n"
"  image: url(\":/qss_icons/dark/rc/arrow_down_disabled.png\");\n"
"  height: 8px;\n"
"  width: 8px;\n"
"}\n"
"\n"
"QComboBox::down-arrow:on, QComboBox::down-arrow:hover, QComboBox::down-arrow:focus {\n"
"  image: url(\":/qss_icons/dark/rc/arrow_down.png\");\n"
"}\n"
"\n"
"/* QSlider ----------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qslider\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QSlider:disabled {\n"
"  background: #19232D;\n"
"}\n"
"\n"
"QSlider:focus {\n"
"  border: none;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"  background: #455364;\n"
"  border: 1px solid #455364;\n"
"  height: 4px;\n"
"  margin: 0px;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"  background: #455364;\n"
"  border: 1px solid #455364;\n"
"  width: 4px;\n"
"  margin: 0px;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:vertical {\n"
" "
                        " background: #346792;\n"
"  border: 1px solid #455364;\n"
"  width: 4px;\n"
"  margin: 0px;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:vertical :disabled {\n"
"  background: #26486B;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"  background: #346792;\n"
"  border: 1px solid #455364;\n"
"  height: 4px;\n"
"  margin: 0px;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"  background: #26486B;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"  background: #9DA9B5;\n"
"  border: 1px solid #455364;\n"
"  width: 8px;\n"
"  height: 8px;\n"
"  margin: -8px 0px;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"  background: #346792;\n"
"  border: 1px solid #346792;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:focus {\n"
"  border: 1px solid #1A72BB;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"  background: #9DA9B5;\n"
"  border: 1px solid #455364;\n"
"  width: 8px;\n"
"  height: 8px;\n"
"  margin: 0 -8px;\n"
"  border-radius: 4px;\n"
""
                        "}\n"
"\n"
"QSlider::handle:vertical:hover {\n"
"  background: #346792;\n"
"  border: 1px solid #346792;\n"
"}\n"
"\n"
"QSlider::handle:vertical:focus {\n"
"  border: 1px solid #1A72BB;\n"
"}\n"
"\n"
"/* QLineEdit --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qlineedit\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QLineEdit {\n"
"  background-color: #19232D;\n"
"  padding-top: 2px;\n"
"  /* This QLineEdit fix  103, 111 */\n"
"  padding-bottom: 2px;\n"
"  /* This QLineEdit fix  103, 111 */\n"
"  padding-left: 4px;\n"
"  padding-right: 4px;\n"
"  border-style: solid;\n"
"  border: 1px solid #455364;\n"
"  border-radius: 4px;\n"
"  color: #DFE1E2;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"  background-color: #19232D;\n"
"  color: #788D9C;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"  border: 1px solid #346792;\n"
"  color: #DFE1E2;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"  border: 1px solid #1A72"
                        "BB;\n"
"}\n"
"\n"
"QLineEdit:selected {\n"
"  background-color: #346792;\n"
"  color: #455364;\n"
"}\n"
"\n"
"/* QTabWiget --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtabwidget-and-qtabbar\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QTabWidget {\n"
"  padding: 2px;\n"
"  selection-background-color: #455364;\n"
"}\n"
"\n"
"QTabWidget QWidget {\n"
"  /* Fixes #189 */\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"  border: 1px solid #455364;\n"
"  border-radius: 4px;\n"
"  margin: 0px;\n"
"  /* Fixes double border inside pane with pyqt5 */\n"
"  padding: 0px;\n"
"}\n"
"\n"
"QTabWidget::pane:selected {\n"
"  background-color: #455364;\n"
"  border: 1px solid #346792;\n"
"}\n"
"\n"
"/* QTabBar ----------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtabwidget-and-qtabbar\n"
"\n"
"------"
                        "--------------------------------------------------------------------- */\n"
"QTabBar, QDockWidget QTabBar {\n"
"  qproperty-drawBase: 0;\n"
"  border-radius: 4px;\n"
"  margin: 0px;\n"
"  padding: 2px;\n"
"  border: 0;\n"
"  /* left: 5px; move to the right by 5px - removed for fix */\n"
"}\n"
"\n"
"QTabBar::close-button, QDockWidget QTabBar::close-button {\n"
"  border: 0;\n"
"  margin: 0;\n"
"  padding: 4px;\n"
"  image: url(\":/qss_icons/dark/rc/window_close.png\");\n"
"}\n"
"\n"
"QTabBar::close-button:hover, QDockWidget QTabBar::close-button:hover {\n"
"  image: url(\":/qss_icons/dark/rc/window_close_focus.png\");\n"
"}\n"
"\n"
"QTabBar::close-button:pressed, QDockWidget QTabBar::close-button:pressed {\n"
"  image: url(\":/qss_icons/dark/rc/window_close_pressed.png\");\n"
"}\n"
"\n"
"QTabBar::tab, QDockWidget QTabBar::tab {\n"
"  /* !selected and disabled ----------------------------------------- */\n"
"  /* selected ------------------------------------------------------- */\n"
"}\n"
"\n"
"QTabBar::tab:top:"
                        "selected:disabled, QDockWidget QTabBar::tab:top:selected:disabled {\n"
"  border-bottom: 3px solid #26486B;\n"
"  color: #788D9C;\n"
"  background-color: #455364;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:selected:disabled, QDockWidget QTabBar::tab:bottom:selected:disabled {\n"
"  border-top: 3px solid #26486B;\n"
"  color: #788D9C;\n"
"  background-color: #455364;\n"
"}\n"
"\n"
"QTabBar::tab:left:selected:disabled, QDockWidget QTabBar::tab:left:selected:disabled {\n"
"  border-right: 3px solid #26486B;\n"
"  color: #788D9C;\n"
"  background-color: #455364;\n"
"}\n"
"\n"
"QTabBar::tab:right:selected:disabled, QDockWidget QTabBar::tab:right:selected:disabled {\n"
"  border-left: 3px solid #26486B;\n"
"  color: #788D9C;\n"
"  background-color: #455364;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected:disabled, QDockWidget QTabBar::tab:top:!selected:disabled {\n"
"  border-bottom: 3px solid #19232D;\n"
"  color: #788D9C;\n"
"  background-color: #19232D;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected:disabled, QDockWidget QTabBar"
                        "::tab:bottom:!selected:disabled {\n"
"  border-top: 3px solid #19232D;\n"
"  color: #788D9C;\n"
"  background-color: #19232D;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected:disabled, QDockWidget QTabBar::tab:left:!selected:disabled {\n"
"  border-right: 3px solid #19232D;\n"
"  color: #788D9C;\n"
"  background-color: #19232D;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected:disabled, QDockWidget QTabBar::tab:right:!selected:disabled {\n"
"  border-left: 3px solid #19232D;\n"
"  color: #788D9C;\n"
"  background-color: #19232D;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected, QDockWidget QTabBar::tab:top:!selected {\n"
"  border-bottom: 2px solid #19232D;\n"
"  margin-top: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected, QDockWidget QTabBar::tab:bottom:!selected {\n"
"  border-top: 2px solid #19232D;\n"
"  margin-bottom: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected, QDockWidget QTabBar::tab:left:!selected {\n"
"  border-left: 2px solid #19232D;\n"
"  margin-right: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected, QDockWid"
                        "get QTabBar::tab:right:!selected {\n"
"  border-right: 2px solid #19232D;\n"
"  margin-left: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:top, QDockWidget QTabBar::tab:top {\n"
"  background-color: #455364;\n"
"  margin-left: 2px;\n"
"  padding-left: 4px;\n"
"  padding-right: 4px;\n"
"  padding-top: 2px;\n"
"  padding-bottom: 2px;\n"
"  min-width: 5px;\n"
"  border-bottom: 3px solid #455364;\n"
"  border-top-left-radius: 4px;\n"
"  border-top-right-radius: 4px;\n"
"}\n"
"\n"
"QTabBar::tab:top:selected, QDockWidget QTabBar::tab:top:selected {\n"
"  background-color: #54687A;\n"
"  border-bottom: 3px solid #259AE9;\n"
"  border-top-left-radius: 4px;\n"
"  border-top-right-radius: 4px;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected:hover, QDockWidget QTabBar::tab:top:!selected:hover {\n"
"  border: 1px solid #1A72BB;\n"
"  border-bottom: 3px solid #1A72BB;\n"
"  /* Fixes spyder-ide/spyder#9766 and #243 */\n"
"  padding-left: 3px;\n"
"  padding-right: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom, QDockWidget QTabBar::tab:bottom {\n"
" "
                        " border-top: 3px solid #455364;\n"
"  background-color: #455364;\n"
"  margin-left: 2px;\n"
"  padding-left: 4px;\n"
"  padding-right: 4px;\n"
"  padding-top: 2px;\n"
"  padding-bottom: 2px;\n"
"  border-bottom-left-radius: 4px;\n"
"  border-bottom-right-radius: 4px;\n"
"  min-width: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:selected, QDockWidget QTabBar::tab:bottom:selected {\n"
"  background-color: #54687A;\n"
"  border-top: 3px solid #259AE9;\n"
"  border-bottom-left-radius: 4px;\n"
"  border-bottom-right-radius: 4px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected:hover, QDockWidget QTabBar::tab:bottom:!selected:hover {\n"
"  border: 1px solid #1A72BB;\n"
"  border-top: 3px solid #1A72BB;\n"
"  /* Fixes spyder-ide/spyder#9766 and #243 */\n"
"  padding-left: 3px;\n"
"  padding-right: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:left, QDockWidget QTabBar::tab:left {\n"
"  background-color: #455364;\n"
"  margin-top: 2px;\n"
"  padding-left: 2px;\n"
"  padding-right: 2px;\n"
"  padding-top: 4px;\n"
"  padding-bottom: 4px;\n"
""
                        "  border-top-left-radius: 4px;\n"
"  border-bottom-left-radius: 4px;\n"
"  min-height: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:left:selected, QDockWidget QTabBar::tab:left:selected {\n"
"  background-color: #54687A;\n"
"  border-right: 3px solid #259AE9;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected:hover, QDockWidget QTabBar::tab:left:!selected:hover {\n"
"  border: 1px solid #1A72BB;\n"
"  border-right: 3px solid #1A72BB;\n"
"  /* Fixes different behavior #271 */\n"
"  margin-right: 0px;\n"
"  padding-right: -1px;\n"
"}\n"
"\n"
"QTabBar::tab:right, QDockWidget QTabBar::tab:right {\n"
"  background-color: #455364;\n"
"  margin-top: 2px;\n"
"  padding-left: 2px;\n"
"  padding-right: 2px;\n"
"  padding-top: 4px;\n"
"  padding-bottom: 4px;\n"
"  border-top-right-radius: 4px;\n"
"  border-bottom-right-radius: 4px;\n"
"  min-height: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:right:selected, QDockWidget QTabBar::tab:right:selected {\n"
"  background-color: #54687A;\n"
"  border-left: 3px solid #259AE9;\n"
"}\n"
"\n"
"QTabBar::tab:righ"
                        "t:!selected:hover, QDockWidget QTabBar::tab:right:!selected:hover {\n"
"  border: 1px solid #1A72BB;\n"
"  border-left: 3px solid #1A72BB;\n"
"  /* Fixes different behavior #271 */\n"
"  margin-left: 0px;\n"
"  padding-left: 0px;\n"
"}\n"
"\n"
"QTabBar QToolButton, QDockWidget QTabBar QToolButton {\n"
"  /* Fixes #136 */\n"
"  background-color: #455364;\n"
"  height: 12px;\n"
"  width: 12px;\n"
"}\n"
"\n"
"QTabBar QToolButton:pressed, QDockWidget QTabBar QToolButton:pressed {\n"
"  background-color: #455364;\n"
"}\n"
"\n"
"QTabBar QToolButton:pressed:hover, QDockWidget QTabBar QToolButton:pressed:hover {\n"
"  border: 1px solid #346792;\n"
"}\n"
"\n"
"QTabBar QToolButton::left-arrow:enabled, QDockWidget QTabBar QToolButton::left-arrow:enabled {\n"
"  image: url(\":/qss_icons/dark/rc/arrow_left.png\");\n"
"}\n"
"\n"
"QTabBar QToolButton::left-arrow:disabled, QDockWidget QTabBar QToolButton::left-arrow:disabled {\n"
"  image: url(\":/qss_icons/dark/rc/arrow_left_disabled.png\");\n"
"}\n"
"\n"
"QTabBar QToolButto"
                        "n::right-arrow:enabled, QDockWidget QTabBar QToolButton::right-arrow:enabled {\n"
"  image: url(\":/qss_icons/dark/rc/arrow_right.png\");\n"
"}\n"
"\n"
"QTabBar QToolButton::right-arrow:disabled, QDockWidget QTabBar QToolButton::right-arrow:disabled {\n"
"  image: url(\":/qss_icons/dark/rc/arrow_right_disabled.png\");\n"
"}\n"
"\n"
"/* QDockWiget -------------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QDockWidget {\n"
"  outline: 1px solid #455364;\n"
"  background-color: #19232D;\n"
"  border: 1px solid #455364;\n"
"  border-radius: 4px;\n"
"  titlebar-close-icon: url(\":/qss_icons/dark/rc/transparent.png\");\n"
"  titlebar-normal-icon: url(\":/qss_icons/dark/rc/transparent.png\");\n"
"}\n"
"\n"
"QDockWidget::title {\n"
"  /* Better size for title bar */\n"
"  padding: 3px;\n"
"  spacing: 4px;\n"
"  border: none;\n"
"  background-color: #455364;\n"
"}\n"
"\n"
"QDockWidget::close-button {\n"
"  icon-size: 12px;\n"
""
                        "  border: none;\n"
"  background: transparent;\n"
"  background-image: transparent;\n"
"  border: 0;\n"
"  margin: 0;\n"
"  padding: 0;\n"
"  image: url(\":/qss_icons/dark/rc/window_close.png\");\n"
"}\n"
"\n"
"QDockWidget::close-button:hover {\n"
"  image: url(\":/qss_icons/dark/rc/window_close_focus.png\");\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed {\n"
"  image: url(\":/qss_icons/dark/rc/window_close_pressed.png\");\n"
"}\n"
"\n"
"QDockWidget::float-button {\n"
"  icon-size: 12px;\n"
"  border: none;\n"
"  background: transparent;\n"
"  background-image: transparent;\n"
"  border: 0;\n"
"  margin: 0;\n"
"  padding: 0;\n"
"  image: url(\":/qss_icons/dark/rc/window_undock.png\");\n"
"}\n"
"\n"
"QDockWidget::float-button:hover {\n"
"  image: url(\":/qss_icons/dark/rc/window_undock_focus.png\");\n"
"}\n"
"\n"
"QDockWidget::float-button:pressed {\n"
"  image: url(\":/qss_icons/dark/rc/window_undock_pressed.png\");\n"
"}\n"
"\n"
"/* QTreeView QListView QTableView -----------------------------------------\n"
""
                        "\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtreeview\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qlistview\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtableview\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QTreeView:branch:selected, QTreeView:branch:hover {\n"
"  background: url(\":/qss_icons/dark/rc/transparent.png\");\n"
"}\n"
"\n"
"QTreeView:branch:has-siblings:!adjoins-item {\n"
"  border-image: url(\":/qss_icons/dark/rc/branch_line.png\") 0;\n"
"}\n"
"\n"
"QTreeView:branch:has-siblings:adjoins-item {\n"
"  border-image: url(\":/qss_icons/dark/rc/branch_more.png\") 0;\n"
"}\n"
"\n"
"QTreeView:branch:!has-children:!has-siblings:adjoins-item {\n"
"  border-image: url(\":/qss_icons/dark/rc/branch_end.png\") 0;\n"
"}\n"
"\n"
"QTreeView:branch:has-children:!has-siblings:closed, QTreeView:branch:closed:has-children:has-siblings {\n"
"  border-image: none;\n"
"  image: url(\":/qss_icons/dark/rc/branch_clo"
                        "sed.png\");\n"
"}\n"
"\n"
"QTreeView:branch:open:has-children:!has-siblings, QTreeView:branch:open:has-children:has-siblings {\n"
"  border-image: none;\n"
"  image: url(\":/qss_icons/dark/rc/branch_open.png\");\n"
"}\n"
"\n"
"QTreeView:branch:has-children:!has-siblings:closed:hover, QTreeView:branch:closed:has-children:has-siblings:hover {\n"
"  image: url(\":/qss_icons/dark/rc/branch_closed_focus.png\");\n"
"}\n"
"\n"
"QTreeView:branch:open:has-children:!has-siblings:hover, QTreeView:branch:open:has-children:has-siblings:hover {\n"
"  image: url(\":/qss_icons/dark/rc/branch_open_focus.png\");\n"
"}\n"
"\n"
"QTreeView::indicator:checked,\n"
"QListView::indicator:checked,\n"
"QTableView::indicator:checked,\n"
"QColumnView::indicator:checked {\n"
"  image: url(\":/qss_icons/dark/rc/checkbox_checked.png\");\n"
"}\n"
"\n"
"QTreeView::indicator:checked:hover, QTreeView::indicator:checked:focus, QTreeView::indicator:checked:pressed,\n"
"QListView::indicator:checked:hover,\n"
"QListView::indicator:checked:focus,\n"
""
                        "QListView::indicator:checked:pressed,\n"
"QTableView::indicator:checked:hover,\n"
"QTableView::indicator:checked:focus,\n"
"QTableView::indicator:checked:pressed,\n"
"QColumnView::indicator:checked:hover,\n"
"QColumnView::indicator:checked:focus,\n"
"QColumnView::indicator:checked:pressed {\n"
"  image: url(\":/qss_icons/dark/rc/checkbox_checked_focus.png\");\n"
"}\n"
"\n"
"QTreeView::indicator:unchecked,\n"
"QListView::indicator:unchecked,\n"
"QTableView::indicator:unchecked,\n"
"QColumnView::indicator:unchecked {\n"
"  image: url(\":/qss_icons/dark/rc/checkbox_unchecked.png\");\n"
"}\n"
"\n"
"QTreeView::indicator:unchecked:hover, QTreeView::indicator:unchecked:focus, QTreeView::indicator:unchecked:pressed,\n"
"QListView::indicator:unchecked:hover,\n"
"QListView::indicator:unchecked:focus,\n"
"QListView::indicator:unchecked:pressed,\n"
"QTableView::indicator:unchecked:hover,\n"
"QTableView::indicator:unchecked:focus,\n"
"QTableView::indicator:unchecked:pressed,\n"
"QColumnView::indicator:unchecked:hover,\n"
""
                        "QColumnView::indicator:unchecked:focus,\n"
"QColumnView::indicator:unchecked:pressed {\n"
"  image: url(\":/qss_icons/dark/rc/checkbox_unchecked_focus.png\");\n"
"}\n"
"\n"
"QTreeView::indicator:indeterminate,\n"
"QListView::indicator:indeterminate,\n"
"QTableView::indicator:indeterminate,\n"
"QColumnView::indicator:indeterminate {\n"
"  image: url(\":/qss_icons/dark/rc/checkbox_indeterminate.png\");\n"
"}\n"
"\n"
"QTreeView::indicator:indeterminate:hover, QTreeView::indicator:indeterminate:focus, QTreeView::indicator:indeterminate:pressed,\n"
"QListView::indicator:indeterminate:hover,\n"
"QListView::indicator:indeterminate:focus,\n"
"QListView::indicator:indeterminate:pressed,\n"
"QTableView::indicator:indeterminate:hover,\n"
"QTableView::indicator:indeterminate:focus,\n"
"QTableView::indicator:indeterminate:pressed,\n"
"QColumnView::indicator:indeterminate:hover,\n"
"QColumnView::indicator:indeterminate:focus,\n"
"QColumnView::indicator:indeterminate:pressed {\n"
"  image: url(\":/qss_icons/dark/rc/checkbox_"
                        "indeterminate_focus.png\");\n"
"}\n"
"\n"
"QTreeView,\n"
"QListView,\n"
"QTableView,\n"
"QColumnView {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #455364;\n"
"  color: #DFE1E2;\n"
"  gridline-color: #455364;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QTreeView:disabled,\n"
"QListView:disabled,\n"
"QTableView:disabled,\n"
"QColumnView:disabled {\n"
"  background-color: #19232D;\n"
"  color: #788D9C;\n"
"}\n"
"\n"
"QTreeView:selected,\n"
"QListView:selected,\n"
"QTableView:selected,\n"
"QColumnView:selected {\n"
"  background-color: #346792;\n"
"  color: #455364;\n"
"}\n"
"\n"
"QTreeView:focus,\n"
"QListView:focus,\n"
"QTableView:focus,\n"
"QColumnView:focus {\n"
"  border: 1px solid #1A72BB;\n"
"}\n"
"\n"
"QTreeView::item:pressed,\n"
"QListView::item:pressed,\n"
"QTableView::item:pressed,\n"
"QColumnView::item:pressed {\n"
"  background-color: #346792;\n"
"}\n"
"\n"
"QTreeView::item:selected:active,\n"
"QListView::item:selected:active,\n"
"QTableView::item:selected:active,\n"
"QColumnView::item:sele"
                        "cted:active {\n"
"  background-color: #346792;\n"
"}\n"
"\n"
"QTreeView::item:selected:!active,\n"
"QListView::item:selected:!active,\n"
"QTableView::item:selected:!active,\n"
"QColumnView::item:selected:!active {\n"
"  color: #DFE1E2;\n"
"  background-color: #37414F;\n"
"}\n"
"\n"
"QTreeView::item:!selected:hover,\n"
"QListView::item:!selected:hover,\n"
"QTableView::item:!selected:hover,\n"
"QColumnView::item:!selected:hover {\n"
"  outline: 0;\n"
"  color: #DFE1E2;\n"
"  background-color: #37414F;\n"
"}\n"
"\n"
"QTableCornerButton::section {\n"
"  background-color: #19232D;\n"
"  border: 1px transparent #455364;\n"
"  border-radius: 0px;\n"
"}\n"
"\n"
"/* QHeaderView ------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qheaderview\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QHeaderView {\n"
"  background-color: #455364;\n"
"  border: 0px transparent #455364;\n"
"  padding: 0;\n"
"  mar"
                        "gin: 0;\n"
"  border-radius: 0;\n"
"}\n"
"\n"
"QHeaderView:disabled {\n"
"  background-color: #455364;\n"
"  border: 1px transparent #455364;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"  background-color: #455364;\n"
"  color: #DFE1E2;\n"
"  border-radius: 0;\n"
"  text-align: left;\n"
"  font-size: 13px;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal {\n"
"  padding-top: 0;\n"
"  padding-bottom: 0;\n"
"  padding-left: 4px;\n"
"  padding-right: 4px;\n"
"  border-left: 1px solid #19232D;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal::first, QHeaderView::section::horizontal::only-one {\n"
"  border-left: 1px solid #455364;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal:disabled {\n"
"  color: #788D9C;\n"
"}\n"
"\n"
"QHeaderView::section::vertical {\n"
"  padding-top: 0;\n"
"  padding-bottom: 0;\n"
"  padding-left: 4px;\n"
"  padding-right: 4px;\n"
"  border-top: 1px solid #19232D;\n"
"}\n"
"\n"
"QHeaderView::section::vertical::first, QHeaderView::section::vertical::only-one {\n"
"  border-top: 1px solid #4553"
                        "64;\n"
"}\n"
"\n"
"QHeaderView::section::vertical:disabled {\n"
"  color: #788D9C;\n"
"}\n"
"\n"
"QHeaderView::down-arrow {\n"
"  /* Those settings (border/width/height/background-color) solve bug */\n"
"  /* transparent arrow background and size */\n"
"  background-color: #455364;\n"
"  border: none;\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  padding-left: 2px;\n"
"  padding-right: 2px;\n"
"  image: url(\":/qss_icons/dark/rc/arrow_down.png\");\n"
"}\n"
"\n"
"QHeaderView::up-arrow {\n"
"  background-color: #455364;\n"
"  border: none;\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  padding-left: 2px;\n"
"  padding-right: 2px;\n"
"  image: url(\":/qss_icons/dark/rc/arrow_up.png\");\n"
"}\n"
"\n"
"/* QToolBox --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtoolbox\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QToolBox {\n"
"  padding: 0px;\n"
"  border: 0px;\n"
"  border: 1px solid #4"
                        "55364;\n"
"}\n"
"\n"
"QToolBox:selected {\n"
"  padding: 0px;\n"
"  border: 2px solid #346792;\n"
"}\n"
"\n"
"QToolBox::tab {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #455364;\n"
"  color: #DFE1E2;\n"
"  border-top-left-radius: 4px;\n"
"  border-top-right-radius: 4px;\n"
"}\n"
"\n"
"QToolBox::tab:disabled {\n"
"  color: #788D9C;\n"
"}\n"
"\n"
"QToolBox::tab:selected {\n"
"  background-color: #60798B;\n"
"  border-bottom: 2px solid #346792;\n"
"}\n"
"\n"
"QToolBox::tab:selected:disabled {\n"
"  background-color: #455364;\n"
"  border-bottom: 2px solid #26486B;\n"
"}\n"
"\n"
"QToolBox::tab:!selected {\n"
"  background-color: #455364;\n"
"  border-bottom: 2px solid #455364;\n"
"}\n"
"\n"
"QToolBox::tab:!selected:disabled {\n"
"  background-color: #19232D;\n"
"}\n"
"\n"
"QToolBox::tab:hover {\n"
"  border-color: #1A72BB;\n"
"  border-bottom: 2px solid #1A72BB;\n"
"}\n"
"\n"
"QToolBox QScrollArea {\n"
"  padding: 0px;\n"
"  border: 0px;\n"
"  background-color: #19232D;\n"
"}\n"
"\n"
"/* QFrame -----"
                        "------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qframe\n"
"https://doc.qt.io/qt-5/qframe.html#-prop\n"
"https://doc.qt.io/qt-5/qframe.html#details\n"
"https://stackoverflow.com/questions/14581498/qt-stylesheet-for-hline-vline-color\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"/* (dot) .QFrame  fix #141, #126, #123 */\n"
".QFrame {\n"
"  border-radius: 4px;\n"
"  border: 1px solid #455364;\n"
"  /* No frame */\n"
"  /* HLine */\n"
"  /* HLine */\n"
"}\n"
"\n"
".QFrame[frameShape=\"0\"] {\n"
"  border-radius: 4px;\n"
"  border: 1px transparent #455364;\n"
"}\n"
"\n"
".QFrame[frameShape=\"4\"] {\n"
"  max-height: 2px;\n"
"  border: none;\n"
"  background-color: #455364;\n"
"}\n"
"\n"
".QFrame[frameShape=\"5\"] {\n"
"  max-width: 2px;\n"
"  border: none;\n"
"  background-color: #455364;\n"
"}\n"
"\n"
"/* QSplitter --------------------------------------------------------------\n"
"\n"
"ht"
                        "tps://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qsplitter\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QSplitter {\n"
"  background-color: #455364;\n"
"  spacing: 0px;\n"
"  padding: 0px;\n"
"  margin: 0px;\n"
"}\n"
"\n"
"QSplitter::handle {\n"
"  background-color: #455364;\n"
"  border: 0px solid #19232D;\n"
"  spacing: 0px;\n"
"  padding: 1px;\n"
"  margin: 0px;\n"
"}\n"
"\n"
"QSplitter::handle:hover {\n"
"  background-color: #9DA9B5;\n"
"}\n"
"\n"
"QSplitter::handle:horizontal {\n"
"  width: 5px;\n"
"  image: url(\":/qss_icons/dark/rc/line_vertical.png\");\n"
"}\n"
"\n"
"QSplitter::handle:vertical {\n"
"  height: 5px;\n"
"  image: url(\":/qss_icons/dark/rc/line_horizontal.png\");\n"
"}\n"
"\n"
"/* QDateEdit, QDateTimeEdit -----------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QDateEdit, QDateTimeEdit {\n"
"  selection-background-color: #346792;\n"
"  border-style: sol"
                        "id;\n"
"  border: 1px solid #455364;\n"
"  border-radius: 4px;\n"
"  /* This fixes 103, 111 */\n"
"  padding-top: 2px;\n"
"  /* This fixes 103, 111 */\n"
"  padding-bottom: 2px;\n"
"  padding-left: 4px;\n"
"  padding-right: 4px;\n"
"  min-width: 10px;\n"
"}\n"
"\n"
"QDateEdit:on, QDateTimeEdit:on {\n"
"  selection-background-color: #346792;\n"
"}\n"
"\n"
"QDateEdit::drop-down, QDateTimeEdit::drop-down {\n"
"  subcontrol-origin: padding;\n"
"  subcontrol-position: top right;\n"
"  width: 12px;\n"
"  border-left: 1px solid #455364;\n"
"}\n"
"\n"
"QDateEdit::down-arrow, QDateTimeEdit::down-arrow {\n"
"  image: url(\":/qss_icons/dark/rc/arrow_down_disabled.png\");\n"
"  height: 8px;\n"
"  width: 8px;\n"
"}\n"
"\n"
"QDateEdit::down-arrow:on, QDateEdit::down-arrow:hover, QDateEdit::down-arrow:focus, QDateTimeEdit::down-arrow:on, QDateTimeEdit::down-arrow:hover, QDateTimeEdit::down-arrow:focus {\n"
"  image: url(\":/qss_icons/dark/rc/arrow_down.png\");\n"
"}\n"
"\n"
"QDateEdit QAbstractItemView, QDateTimeEdit QAbstra"
                        "ctItemView {\n"
"  background-color: #19232D;\n"
"  border-radius: 4px;\n"
"  border: 1px solid #455364;\n"
"  selection-background-color: #346792;\n"
"}\n"
"\n"
"/* QAbstractView ----------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QAbstractView:hover {\n"
"  border: 1px solid #346792;\n"
"  color: #DFE1E2;\n"
"}\n"
"\n"
"QAbstractView:selected {\n"
"  background: #346792;\n"
"  color: #455364;\n"
"}\n"
"\n"
"/* PlotWidget -------------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"PlotWidget {\n"
"  /* Fix cut labels in plots #134 */\n"
"  padding: 0px;\n"
"}")
        self.centralwidget = QWidget(WeatherApp)
        self.centralwidget.setObjectName(u"centralwidget")
        font = QFont()
        font.setFamilies([u"Liberation Sans"])
        self.centralwidget.setFont(font)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.location_input = QLineEdit(self.frame_3)
        self.location_input.setObjectName(u"location_input")
        self.location_input.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.location_input)

        self.location_choices = QComboBox(self.frame_3)
        self.location_choices.setObjectName(u"location_choices")

        self.horizontalLayout.addWidget(self.location_choices)

        self.get_weather_button = QPushButton(self.frame_3)
        self.get_weather_button.setObjectName(u"get_weather_button")

        self.horizontalLayout.addWidget(self.get_weather_button)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout.addWidget(self.frame_3)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.South)
        self.tabWidget.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabWidget.setDocumentMode(False)
        self.overview = QWidget()
        self.overview.setObjectName(u"overview")
        self.horizontalLayout_12 = QHBoxLayout(self.overview)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.left_side = QVBoxLayout()
        self.left_side.setObjectName(u"left_side")
        self.current_temp = QFrame(self.overview)
        self.current_temp.setObjectName(u"current_temp")
        self.current_temp.setFrameShape(QFrame.Shape.Box)
        self.current_temp.setFrameShadow(QFrame.Shadow.Plain)
        self.current_temp.setLineWidth(2)
        self.horizontalLayout_15 = QHBoxLayout(self.current_temp)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.place_overview = QLabel(self.current_temp)
        self.place_overview.setObjectName(u"place_overview")
        font1 = QFont()
        font1.setFamilies([u"Liberation Sans"])
        font1.setPointSize(30)
        font1.setBold(True)
        self.place_overview.setFont(font1)
        self.place_overview.setTextFormat(Qt.TextFormat.PlainText)
        self.place_overview.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.place_overview)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.current_temp_overview = QLabel(self.current_temp)
        self.current_temp_overview.setObjectName(u"current_temp_overview")
        self.current_temp_overview.setMaximumSize(QSize(200, 50))
        font2 = QFont()
        font2.setFamilies([u"Liberation Sans"])
        font2.setPointSize(30)
        self.current_temp_overview.setFont(font2)
        self.current_temp_overview.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.current_temp_overview)

        self.current_day_icon_overview = QLabel(self.current_temp)
        self.current_day_icon_overview.setObjectName(u"current_day_icon_overview")
        self.current_day_icon_overview.setMaximumSize(QSize(100, 100))
        font3 = QFont()
        font3.setFamilies([u"Liberation Sans"])
        font3.setPointSize(35)
        self.current_day_icon_overview.setFont(font3)

        self.horizontalLayout_11.addWidget(self.current_day_icon_overview)


        self.verticalLayout_10.addLayout(self.horizontalLayout_11)

        self.current_condtions_overview = QLabel(self.current_temp)
        self.current_condtions_overview.setObjectName(u"current_condtions_overview")
        font4 = QFont()
        font4.setFamilies([u"Liberation Sans"])
        font4.setPointSize(15)
        self.current_condtions_overview.setFont(font4)
        self.current_condtions_overview.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.current_condtions_overview)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.min_temp_overview = QLabel(self.current_temp)
        self.min_temp_overview.setObjectName(u"min_temp_overview")
        self.min_temp_overview.setFont(font)
        self.min_temp_overview.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.min_temp_overview)

        self.max_temp_overview = QLabel(self.current_temp)
        self.max_temp_overview.setObjectName(u"max_temp_overview")
        self.max_temp_overview.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.max_temp_overview)


        self.verticalLayout_10.addLayout(self.horizontalLayout_10)

        self.feels_like_temp_overview = QLabel(self.current_temp)
        self.feels_like_temp_overview.setObjectName(u"feels_like_temp_overview")
        self.feels_like_temp_overview.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.feels_like_temp_overview)


        self.horizontalLayout_15.addLayout(self.verticalLayout_10)


        self.left_side.addWidget(self.current_temp)

        self.forecast_overview = QFrame(self.overview)
        self.forecast_overview.setObjectName(u"forecast_overview")
        self.forecast_overview.setFrameShape(QFrame.Shape.Box)
        self.forecast_overview.setFrameShadow(QFrame.Shadow.Plain)
        self.forecast_overview.setLineWidth(2)
        self.horizontalLayout_9 = QHBoxLayout(self.forecast_overview)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.day1_overview = QLabel(self.forecast_overview)
        self.day1_overview.setObjectName(u"day1_overview")

        self.verticalLayout_2.addWidget(self.day1_overview)

        self.day2_overview = QLabel(self.forecast_overview)
        self.day2_overview.setObjectName(u"day2_overview")

        self.verticalLayout_2.addWidget(self.day2_overview)

        self.day3_overview = QLabel(self.forecast_overview)
        self.day3_overview.setObjectName(u"day3_overview")

        self.verticalLayout_2.addWidget(self.day3_overview)

        self.day4_overview = QLabel(self.forecast_overview)
        self.day4_overview.setObjectName(u"day4_overview")

        self.verticalLayout_2.addWidget(self.day4_overview)

        self.day5_overview = QLabel(self.forecast_overview)
        self.day5_overview.setObjectName(u"day5_overview")

        self.verticalLayout_2.addWidget(self.day5_overview)


        self.horizontalLayout_9.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, -1, 0, 0)
        self.icon_overview1 = QLabel(self.forecast_overview)
        self.icon_overview1.setObjectName(u"icon_overview1")
        self.icon_overview1.setMaximumSize(QSize(75, 75))
        font5 = QFont()
        font5.setFamilies([u"Liberation Sans"])
        font5.setPointSize(10)
        self.icon_overview1.setFont(font5)
        self.icon_overview1.setPixmap(QPixmap(u"../8a3a0566/sunny.png"))
        self.icon_overview1.setScaledContents(True)
        self.icon_overview1.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_3.addWidget(self.icon_overview1)

        self.icon_chance_of_rain1 = QLabel(self.forecast_overview)
        self.icon_chance_of_rain1.setObjectName(u"icon_chance_of_rain1")
        self.icon_chance_of_rain1.setMaximumSize(QSize(75, 75))
        font6 = QFont()
        font6.setFamilies([u"Liberation Sans"])
        font6.setPointSize(10)
        font6.setBold(True)
        self.icon_chance_of_rain1.setFont(font6)
        self.icon_chance_of_rain1.setStyleSheet(u"color: rgb(85, 170, 255);")
        self.icon_chance_of_rain1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.icon_chance_of_rain1)

        self.icon_overview2 = QLabel(self.forecast_overview)
        self.icon_overview2.setObjectName(u"icon_overview2")
        self.icon_overview2.setMaximumSize(QSize(75, 75))
        self.icon_overview2.setFont(font5)
        self.icon_overview2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_3.addWidget(self.icon_overview2)

        self.icon_chance_of_rain2 = QLabel(self.forecast_overview)
        self.icon_chance_of_rain2.setObjectName(u"icon_chance_of_rain2")
        self.icon_chance_of_rain2.setMaximumSize(QSize(75, 75))
        font7 = QFont()
        font7.setFamilies([u"Noto Sans"])
        font7.setBold(True)
        self.icon_chance_of_rain2.setFont(font7)
        self.icon_chance_of_rain2.setStyleSheet(u"color: rgb(85, 170, 255);")
        self.icon_chance_of_rain2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.icon_chance_of_rain2)

        self.icon_overview3 = QLabel(self.forecast_overview)
        self.icon_overview3.setObjectName(u"icon_overview3")
        self.icon_overview3.setMaximumSize(QSize(75, 75))
        self.icon_overview3.setFont(font5)
        self.icon_overview3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_3.addWidget(self.icon_overview3)

        self.icon_chance_of_rain3 = QLabel(self.forecast_overview)
        self.icon_chance_of_rain3.setObjectName(u"icon_chance_of_rain3")
        self.icon_chance_of_rain3.setMaximumSize(QSize(75, 75))
        self.icon_chance_of_rain3.setFont(font7)
        self.icon_chance_of_rain3.setStyleSheet(u"color: rgb(85, 170, 255);")
        self.icon_chance_of_rain3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.icon_chance_of_rain3)

        self.icon_overview4 = QLabel(self.forecast_overview)
        self.icon_overview4.setObjectName(u"icon_overview4")
        self.icon_overview4.setMaximumSize(QSize(75, 75))
        self.icon_overview4.setFont(font5)
        self.icon_overview4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_3.addWidget(self.icon_overview4)

        self.icon_chance_of_rain4 = QLabel(self.forecast_overview)
        self.icon_chance_of_rain4.setObjectName(u"icon_chance_of_rain4")
        self.icon_chance_of_rain4.setMaximumSize(QSize(75, 75))
        self.icon_chance_of_rain4.setFont(font7)
        self.icon_chance_of_rain4.setStyleSheet(u"color: rgb(85, 170, 255);")
        self.icon_chance_of_rain4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.icon_chance_of_rain4)

        self.icon_overview5 = QLabel(self.forecast_overview)
        self.icon_overview5.setObjectName(u"icon_overview5")
        self.icon_overview5.setMaximumSize(QSize(75, 75))
        self.icon_overview5.setFont(font5)
        self.icon_overview5.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_3.addWidget(self.icon_overview5)

        self.icon_chance_of_rain5 = QLabel(self.forecast_overview)
        self.icon_chance_of_rain5.setObjectName(u"icon_chance_of_rain5")
        self.icon_chance_of_rain5.setMaximumSize(QSize(75, 75))
        self.icon_chance_of_rain5.setFont(font7)
        self.icon_chance_of_rain5.setStyleSheet(u"color: rgb(85, 170, 255);")
        self.icon_chance_of_rain5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.icon_chance_of_rain5)


        self.horizontalLayout_9.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.day1_temp_overview = QLabel(self.forecast_overview)
        self.day1_temp_overview.setObjectName(u"day1_temp_overview")
        self.day1_temp_overview.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_4.addWidget(self.day1_temp_overview)

        self.day2_temp_overview = QLabel(self.forecast_overview)
        self.day2_temp_overview.setObjectName(u"day2_temp_overview")
        self.day2_temp_overview.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_4.addWidget(self.day2_temp_overview)

        self.day3_temp_overview = QLabel(self.forecast_overview)
        self.day3_temp_overview.setObjectName(u"day3_temp_overview")
        self.day3_temp_overview.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_4.addWidget(self.day3_temp_overview)

        self.day4_temp_overview = QLabel(self.forecast_overview)
        self.day4_temp_overview.setObjectName(u"day4_temp_overview")
        self.day4_temp_overview.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_4.addWidget(self.day4_temp_overview)

        self.day5_temp_overview = QLabel(self.forecast_overview)
        self.day5_temp_overview.setObjectName(u"day5_temp_overview")
        self.day5_temp_overview.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_4.addWidget(self.day5_temp_overview)


        self.horizontalLayout_9.addLayout(self.verticalLayout_4)


        self.left_side.addWidget(self.forecast_overview)


        self.horizontalLayout_12.addLayout(self.left_side)

        self.right_side = QVBoxLayout()
        self.right_side.setObjectName(u"right_side")
        self.uv_index = QFrame(self.overview)
        self.uv_index.setObjectName(u"uv_index")
        self.uv_index.setFrameShape(QFrame.Shape.Box)
        self.uv_index.setFrameShadow(QFrame.Shadow.Plain)
        self.uv_index.setLineWidth(2)
        self.horizontalLayout_6 = QHBoxLayout(self.uv_index)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_17 = QLabel(self.uv_index)
        self.label_17.setObjectName(u"label_17")
        font8 = QFont()
        font8.setFamilies([u"Liberation Sans"])
        font8.setPointSize(20)
        self.label_17.setFont(font8)

        self.verticalLayout_5.addWidget(self.label_17)

        self.uv_index_bar = QProgressBar(self.uv_index)
        self.uv_index_bar.setObjectName(u"uv_index_bar")
        self.uv_index_bar.setStyleSheet(u"")
        self.uv_index_bar.setMinimum(0)
        self.uv_index_bar.setMaximum(11)
        self.uv_index_bar.setValue(8)
        self.uv_index_bar.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.uv_index_bar.setTextVisible(False)
        self.uv_index_bar.setOrientation(Qt.Orientation.Horizontal)
        self.uv_index_bar.setInvertedAppearance(False)

        self.verticalLayout_5.addWidget(self.uv_index_bar)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.max_uv_overview = QLabel(self.uv_index)
        self.max_uv_overview.setObjectName(u"max_uv_overview")

        self.horizontalLayout_5.addWidget(self.max_uv_overview)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.sun_protection_recommended_overview = QLabel(self.uv_index)
        self.sun_protection_recommended_overview.setObjectName(u"sun_protection_recommended_overview")

        self.verticalLayout_7.addWidget(self.sun_protection_recommended_overview)

        self.protection_time_overview = QLabel(self.uv_index)
        self.protection_time_overview.setObjectName(u"protection_time_overview")

        self.verticalLayout_7.addWidget(self.protection_time_overview)


        self.horizontalLayout_5.addLayout(self.verticalLayout_7)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)


        self.horizontalLayout_6.addLayout(self.verticalLayout_6)


        self.right_side.addWidget(self.uv_index)

        self.sunrise_and_set = QFrame(self.overview)
        self.sunrise_and_set.setObjectName(u"sunrise_and_set")
        self.sunrise_and_set.setFrameShape(QFrame.Shape.Box)
        self.sunrise_and_set.setFrameShadow(QFrame.Shadow.Plain)
        self.sunrise_and_set.setLineWidth(2)
        self.horizontalLayout_7 = QHBoxLayout(self.sunrise_and_set)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.sunrise_overview = QLabel(self.sunrise_and_set)
        self.sunrise_overview.setObjectName(u"sunrise_overview")

        self.horizontalLayout_4.addWidget(self.sunrise_overview)

        self.sunset_overview = QLabel(self.sunrise_and_set)
        self.sunset_overview.setObjectName(u"sunset_overview")

        self.horizontalLayout_4.addWidget(self.sunset_overview)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_4)


        self.right_side.addWidget(self.sunrise_and_set)

        self.amount_of_rain = QFrame(self.overview)
        self.amount_of_rain.setObjectName(u"amount_of_rain")
        self.amount_of_rain.setFrameShape(QFrame.Shape.Box)
        self.amount_of_rain.setFrameShadow(QFrame.Shadow.Plain)
        self.amount_of_rain.setLineWidth(2)
        self.verticalLayout_11 = QVBoxLayout(self.amount_of_rain)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.rain_graph_overview = GraphPlot(self.amount_of_rain)
        self.rain_graph_overview.setObjectName(u"rain_graph_overview")
        self.rain_graph_overview.setFrameShape(QFrame.Shape.NoFrame)
        self.rain_graph_overview.setFrameShadow(QFrame.Shadow.Plain)
        self.rain_graph_overview.setLineWidth(0)

        self.verticalLayout_11.addWidget(self.rain_graph_overview)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(-1, -1, -1, 0)
        self.label_6 = QLabel(self.amount_of_rain)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_17.addWidget(self.label_6)

        self.forecast_amount_of_rain_overview = QLabel(self.amount_of_rain)
        self.forecast_amount_of_rain_overview.setObjectName(u"forecast_amount_of_rain_overview")

        self.horizontalLayout_17.addWidget(self.forecast_amount_of_rain_overview)

        self.horizontalLayout_17.setStretch(0, 1)
        self.horizontalLayout_17.setStretch(1, 20)

        self.verticalLayout_11.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_4 = QLabel(self.amount_of_rain)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_18.addWidget(self.label_4)

        self.chance_of_rain_overview = QLabel(self.amount_of_rain)
        self.chance_of_rain_overview.setObjectName(u"chance_of_rain_overview")

        self.horizontalLayout_18.addWidget(self.chance_of_rain_overview)

        self.horizontalLayout_18.setStretch(0, 1)
        self.horizontalLayout_18.setStretch(1, 20)

        self.verticalLayout_11.addLayout(self.horizontalLayout_18)


        self.right_side.addWidget(self.amount_of_rain)

        self.wind_speed = QFrame(self.overview)
        self.wind_speed.setObjectName(u"wind_speed")
        self.wind_speed.setFrameShape(QFrame.Shape.Box)
        self.wind_speed.setFrameShadow(QFrame.Shadow.Plain)
        self.wind_speed.setLineWidth(2)
        self.verticalLayout_9 = QVBoxLayout(self.wind_speed)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label = QLabel(self.wind_speed)
        self.label.setObjectName(u"label")
        font9 = QFont()
        font9.setFamilies([u"Liberation Sans"])
        font9.setBold(True)
        self.label.setFont(font9)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.label)

        self.compass_widget = CompassWidget(self.wind_speed)
        self.compass_widget.setObjectName(u"compass_widget")
        self.compass_widget.setMinimumSize(QSize(100, 100))

        self.verticalLayout_9.addWidget(self.compass_widget)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_25 = QLabel(self.wind_speed)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_25)

        self.wind_speed_overview = QLabel(self.wind_speed)
        self.wind_speed_overview.setObjectName(u"wind_speed_overview")
        self.wind_speed_overview.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.wind_speed_overview)


        self.verticalLayout_9.addLayout(self.verticalLayout_8)


        self.right_side.addWidget(self.wind_speed)


        self.horizontalLayout_12.addLayout(self.right_side)

        self.horizontalLayout_12.setStretch(0, 1)
        self.horizontalLayout_12.setStretch(1, 1)
        self.tabWidget.addTab(self.overview, "")
        self.past_weather = QWidget()
        self.past_weather.setObjectName(u"past_weather")
        self.verticalLayout_12 = QVBoxLayout(self.past_weather)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.Highlights = QFrame(self.past_weather)
        self.Highlights.setObjectName(u"Highlights")
        self.Highlights.setFrameShape(QFrame.Shape.NoFrame)
        self.Highlights.setFrameShadow(QFrame.Shadow.Plain)
        self.Highlights.setLineWidth(2)
        self.gridLayout = QGridLayout(self.Highlights)
        self.gridLayout.setObjectName(u"gridLayout")
        self.highest_gust_speed = QFrame(self.Highlights)
        self.highest_gust_speed.setObjectName(u"highest_gust_speed")
        self.highest_gust_speed.setFrameShape(QFrame.Shape.Box)
        self.highest_gust_speed.setFrameShadow(QFrame.Shadow.Plain)
        self.highest_gust_speed.setLineWidth(2)
        self.verticalLayout_19 = QVBoxLayout(self.highest_gust_speed)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.highlights_gust_speed = QLabel(self.highest_gust_speed)
        self.highlights_gust_speed.setObjectName(u"highlights_gust_speed")
        self.highlights_gust_speed.setFont(font4)

        self.horizontalLayout_8.addWidget(self.highlights_gust_speed)

        self.highlights_gust_speed_time = QLabel(self.highest_gust_speed)
        self.highlights_gust_speed_time.setObjectName(u"highlights_gust_speed_time")

        self.horizontalLayout_8.addWidget(self.highlights_gust_speed_time)

        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 20)

        self.verticalLayout_15.addLayout(self.horizontalLayout_8)

        self.label_35 = QLabel(self.highest_gust_speed)
        self.label_35.setObjectName(u"label_35")

        self.verticalLayout_15.addWidget(self.label_35)


        self.verticalLayout_19.addLayout(self.verticalLayout_15)


        self.gridLayout.addWidget(self.highest_gust_speed, 2, 0, 1, 1)

        self.highest_temperature = QFrame(self.Highlights)
        self.highest_temperature.setObjectName(u"highest_temperature")
        self.highest_temperature.setFrameShape(QFrame.Shape.Box)
        self.highest_temperature.setFrameShadow(QFrame.Shadow.Plain)
        self.highest_temperature.setLineWidth(2)
        self.verticalLayout_18 = QVBoxLayout(self.highest_temperature)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.highlights_max_temp = QLabel(self.highest_temperature)
        self.highlights_max_temp.setObjectName(u"highlights_max_temp")
        self.highlights_max_temp.setFont(font4)

        self.horizontalLayout_2.addWidget(self.highlights_max_temp)

        self.highlights_max_temp_time = QLabel(self.highest_temperature)
        self.highlights_max_temp_time.setObjectName(u"highlights_max_temp_time")

        self.horizontalLayout_2.addWidget(self.highlights_max_temp_time)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 20)

        self.verticalLayout_13.addLayout(self.horizontalLayout_2)

        self.label_29 = QLabel(self.highest_temperature)
        self.label_29.setObjectName(u"label_29")

        self.verticalLayout_13.addWidget(self.label_29)


        self.verticalLayout_18.addLayout(self.verticalLayout_13)


        self.gridLayout.addWidget(self.highest_temperature, 1, 0, 1, 1)

        self.amount_of_rain_9am = QFrame(self.Highlights)
        self.amount_of_rain_9am.setObjectName(u"amount_of_rain_9am")
        self.amount_of_rain_9am.setFrameShape(QFrame.Shape.Box)
        self.amount_of_rain_9am.setFrameShadow(QFrame.Shadow.Plain)
        self.amount_of_rain_9am.setLineWidth(2)
        self.verticalLayout_17 = QVBoxLayout(self.amount_of_rain_9am)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.highlights_rain_since_9am = QLabel(self.amount_of_rain_9am)
        self.highlights_rain_since_9am.setObjectName(u"highlights_rain_since_9am")
        self.highlights_rain_since_9am.setFont(font4)

        self.horizontalLayout_13.addWidget(self.highlights_rain_since_9am)

        self.label_37 = QLabel(self.amount_of_rain_9am)
        self.label_37.setObjectName(u"label_37")

        self.horizontalLayout_13.addWidget(self.label_37)

        self.horizontalLayout_13.setStretch(0, 1)
        self.horizontalLayout_13.setStretch(1, 20)

        self.verticalLayout_16.addLayout(self.horizontalLayout_13)

        self.label_38 = QLabel(self.amount_of_rain_9am)
        self.label_38.setObjectName(u"label_38")

        self.verticalLayout_16.addWidget(self.label_38)


        self.verticalLayout_17.addLayout(self.verticalLayout_16)


        self.gridLayout.addWidget(self.amount_of_rain_9am, 2, 1, 1, 1)

        self.lowest_temperature = QFrame(self.Highlights)
        self.lowest_temperature.setObjectName(u"lowest_temperature")
        self.lowest_temperature.setFrameShape(QFrame.Shape.Box)
        self.lowest_temperature.setFrameShadow(QFrame.Shadow.Plain)
        self.lowest_temperature.setLineWidth(2)
        self.horizontalLayout_14 = QHBoxLayout(self.lowest_temperature)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.highlights_min_temp = QLabel(self.lowest_temperature)
        self.highlights_min_temp.setObjectName(u"highlights_min_temp")
        self.highlights_min_temp.setFont(font4)

        self.horizontalLayout_3.addWidget(self.highlights_min_temp)

        self.highlights_min_temp_time = QLabel(self.lowest_temperature)
        self.highlights_min_temp_time.setObjectName(u"highlights_min_temp_time")

        self.horizontalLayout_3.addWidget(self.highlights_min_temp_time)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 20)

        self.verticalLayout_14.addLayout(self.horizontalLayout_3)

        self.label_32 = QLabel(self.lowest_temperature)
        self.label_32.setObjectName(u"label_32")

        self.verticalLayout_14.addWidget(self.label_32)


        self.horizontalLayout_14.addLayout(self.verticalLayout_14)


        self.gridLayout.addWidget(self.lowest_temperature, 1, 1, 1, 1)


        self.verticalLayout_12.addWidget(self.Highlights)

        self.observation_info_table = QTableWidget(self.past_weather)
        self.observation_info_table.setObjectName(u"observation_info_table")
        self.observation_info_table.setFrameShape(QFrame.Shape.Box)
        self.observation_info_table.setFrameShadow(QFrame.Shadow.Plain)
        self.observation_info_table.setLineWidth(2)

        self.verticalLayout_12.addWidget(self.observation_info_table)

        self.tabWidget.addTab(self.past_weather, "")
        self.forecast_weather = QWidget()
        self.forecast_weather.setObjectName(u"forecast_weather")
        self.verticalLayout_20 = QVBoxLayout(self.forecast_weather)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.scrollArea = QScrollArea(self.forecast_weather)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 2036, 211))
        self.horizontalLayout_16 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.forecast_day1 = QFrame(self.scrollAreaWidgetContents)
        self.forecast_day1.setObjectName(u"forecast_day1")
        self.forecast_day1.setMinimumSize(QSize(400, 100))
        self.forecast_day1.setFrameShape(QFrame.Shape.Box)
        self.forecast_day1.setFrameShadow(QFrame.Shadow.Plain)
        self.forecast_day1.setLineWidth(2)
        self.verticalLayout_21 = QVBoxLayout(self.forecast_day1)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.forecast_day1_icon = QLabel(self.forecast_day1)
        self.forecast_day1_icon.setObjectName(u"forecast_day1_icon")
        self.forecast_day1_icon.setFrameShape(QFrame.Shape.NoFrame)
        self.forecast_day1_icon.setMidLineWidth(4)

        self.horizontalLayout_19.addWidget(self.forecast_day1_icon)

        self.forecast_day1_name = QLabel(self.forecast_day1)
        self.forecast_day1_name.setObjectName(u"forecast_day1_name")
        self.forecast_day1_name.setFont(font9)

        self.horizontalLayout_19.addWidget(self.forecast_day1_name)


        self.verticalLayout_21.addLayout(self.horizontalLayout_19)


        self.horizontalLayout_16.addWidget(self.forecast_day1)

        self.forecast_day2 = QFrame(self.scrollAreaWidgetContents)
        self.forecast_day2.setObjectName(u"forecast_day2")
        self.forecast_day2.setMinimumSize(QSize(400, 100))
        self.forecast_day2.setFrameShape(QFrame.Shape.Box)
        self.forecast_day2.setFrameShadow(QFrame.Shadow.Plain)
        self.forecast_day2.setLineWidth(2)
        self.verticalLayout_22 = QVBoxLayout(self.forecast_day2)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.forecast_day2_icon = QLabel(self.forecast_day2)
        self.forecast_day2_icon.setObjectName(u"forecast_day2_icon")

        self.horizontalLayout_20.addWidget(self.forecast_day2_icon)

        self.forecast_day2_name = QLabel(self.forecast_day2)
        self.forecast_day2_name.setObjectName(u"forecast_day2_name")
        self.forecast_day2_name.setFont(font9)

        self.horizontalLayout_20.addWidget(self.forecast_day2_name)


        self.verticalLayout_22.addLayout(self.horizontalLayout_20)


        self.horizontalLayout_16.addWidget(self.forecast_day2)

        self.forecast_day3 = QFrame(self.scrollAreaWidgetContents)
        self.forecast_day3.setObjectName(u"forecast_day3")
        self.forecast_day3.setMinimumSize(QSize(400, 100))
        self.forecast_day3.setFrameShape(QFrame.Shape.Box)
        self.forecast_day3.setFrameShadow(QFrame.Shadow.Plain)
        self.forecast_day3.setLineWidth(2)
        self.verticalLayout_23 = QVBoxLayout(self.forecast_day3)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.forecast_day3_icon = QLabel(self.forecast_day3)
        self.forecast_day3_icon.setObjectName(u"forecast_day3_icon")

        self.horizontalLayout_21.addWidget(self.forecast_day3_icon)

        self.forecast_day3_name = QLabel(self.forecast_day3)
        self.forecast_day3_name.setObjectName(u"forecast_day3_name")
        self.forecast_day3_name.setFont(font9)

        self.horizontalLayout_21.addWidget(self.forecast_day3_name)


        self.verticalLayout_23.addLayout(self.horizontalLayout_21)


        self.horizontalLayout_16.addWidget(self.forecast_day3)

        self.forecast_day4 = QFrame(self.scrollAreaWidgetContents)
        self.forecast_day4.setObjectName(u"forecast_day4")
        self.forecast_day4.setMinimumSize(QSize(400, 100))
        self.forecast_day4.setFrameShape(QFrame.Shape.Box)
        self.forecast_day4.setFrameShadow(QFrame.Shadow.Plain)
        self.forecast_day4.setLineWidth(2)
        self.verticalLayout_24 = QVBoxLayout(self.forecast_day4)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.forecast_day4_icon = QLabel(self.forecast_day4)
        self.forecast_day4_icon.setObjectName(u"forecast_day4_icon")

        self.horizontalLayout_22.addWidget(self.forecast_day4_icon)

        self.forecast_day4_name = QLabel(self.forecast_day4)
        self.forecast_day4_name.setObjectName(u"forecast_day4_name")
        self.forecast_day4_name.setFont(font9)

        self.horizontalLayout_22.addWidget(self.forecast_day4_name)


        self.verticalLayout_24.addLayout(self.horizontalLayout_22)


        self.horizontalLayout_16.addWidget(self.forecast_day4)

        self.forecast_day5 = QFrame(self.scrollAreaWidgetContents)
        self.forecast_day5.setObjectName(u"forecast_day5")
        self.forecast_day5.setMinimumSize(QSize(400, 100))
        self.forecast_day5.setFrameShape(QFrame.Shape.Box)
        self.forecast_day5.setFrameShadow(QFrame.Shadow.Plain)
        self.forecast_day5.setLineWidth(2)
        self.verticalLayout_25 = QVBoxLayout(self.forecast_day5)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.forecast_day5_icon = QLabel(self.forecast_day5)
        self.forecast_day5_icon.setObjectName(u"forecast_day5_icon")

        self.horizontalLayout_23.addWidget(self.forecast_day5_icon)

        self.forecast_day5_name = QLabel(self.forecast_day5)
        self.forecast_day5_name.setObjectName(u"forecast_day5_name")
        self.forecast_day5_name.setFont(font9)

        self.horizontalLayout_23.addWidget(self.forecast_day5_name)


        self.verticalLayout_25.addLayout(self.horizontalLayout_23)


        self.horizontalLayout_16.addWidget(self.forecast_day5)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_20.addWidget(self.scrollArea)

        self.forecast_info_table = QTableWidget(self.forecast_weather)
        self.forecast_info_table.setObjectName(u"forecast_info_table")

        self.verticalLayout_20.addWidget(self.forecast_info_table)

        self.verticalLayout_20.setStretch(0, 1)
        self.verticalLayout_20.setStretch(1, 2)
        self.tabWidget.addTab(self.forecast_weather, "")
        self.settings = QWidget()
        self.settings.setObjectName(u"settings")
        self.label_3 = QLabel(self.settings)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 0, 271, 61))
        font10 = QFont()
        font10.setFamilies([u"Liberation Sans"])
        font10.setPointSize(25)
        font10.setBold(True)
        self.label_3.setFont(font10)
        self.tabWidget.addTab(self.settings, "")

        self.verticalLayout.addWidget(self.tabWidget)

        WeatherApp.setCentralWidget(self.centralwidget)

        self.retranslateUi(WeatherApp)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(WeatherApp)
    # setupUi

    def retranslateUi(self, WeatherApp):
        WeatherApp.setWindowTitle(QCoreApplication.translate("WeatherApp", u"MainWindow", None))
        self.location_input.setPlaceholderText(QCoreApplication.translate("WeatherApp", u"Enter Your Location Here", None))
        self.get_weather_button.setText(QCoreApplication.translate("WeatherApp", u"Get Weather", None))
        self.place_overview.setText(QCoreApplication.translate("WeatherApp", u"Place", None))
        self.current_temp_overview.setText(QCoreApplication.translate("WeatherApp", u"X\u00b0", None))
        self.current_day_icon_overview.setText(QCoreApplication.translate("WeatherApp", u"O", None))
        self.current_condtions_overview.setText(QCoreApplication.translate("WeatherApp", u"Sunny", None))
        self.min_temp_overview.setText(QCoreApplication.translate("WeatherApp", u"Min: x\u00b0", None))
        self.max_temp_overview.setText(QCoreApplication.translate("WeatherApp", u"Max: y\u00b0", None))
        self.feels_like_temp_overview.setText(QCoreApplication.translate("WeatherApp", u"Feels like: x\u00b0", None))
        self.day1_overview.setText(QCoreApplication.translate("WeatherApp", u"Day1", None))
        self.day2_overview.setText(QCoreApplication.translate("WeatherApp", u"Day2", None))
        self.day3_overview.setText(QCoreApplication.translate("WeatherApp", u"Day3", None))
        self.day4_overview.setText(QCoreApplication.translate("WeatherApp", u"Day 4", None))
        self.day5_overview.setText(QCoreApplication.translate("WeatherApp", u"Day5", None))
        self.icon_overview1.setText("")
        self.icon_chance_of_rain1.setText(QCoreApplication.translate("WeatherApp", u"69%", None))
        self.icon_overview2.setText(QCoreApplication.translate("WeatherApp", u"O", None))
        self.icon_chance_of_rain2.setText(QCoreApplication.translate("WeatherApp", u"69%", None))
        self.icon_overview3.setText(QCoreApplication.translate("WeatherApp", u"O", None))
        self.icon_chance_of_rain3.setText(QCoreApplication.translate("WeatherApp", u"69%", None))
        self.icon_overview4.setText(QCoreApplication.translate("WeatherApp", u"O", None))
        self.icon_chance_of_rain4.setText(QCoreApplication.translate("WeatherApp", u"69%", None))
        self.icon_overview5.setText(QCoreApplication.translate("WeatherApp", u"O", None))
        self.icon_chance_of_rain5.setText(QCoreApplication.translate("WeatherApp", u"69%", None))
        self.day1_temp_overview.setText(QCoreApplication.translate("WeatherApp", u"TextLabel", None))
        self.day2_temp_overview.setText(QCoreApplication.translate("WeatherApp", u"TextLabel", None))
        self.day3_temp_overview.setText(QCoreApplication.translate("WeatherApp", u"TextLabel", None))
        self.day4_temp_overview.setText(QCoreApplication.translate("WeatherApp", u"TextLabel", None))
        self.day5_temp_overview.setText(QCoreApplication.translate("WeatherApp", u"TextLabel", None))
        self.label_17.setText(QCoreApplication.translate("WeatherApp", u"UV Index", None))
        self.max_uv_overview.setText(QCoreApplication.translate("WeatherApp", u"Max UV:", None))
        self.sun_protection_recommended_overview.setText(QCoreApplication.translate("WeatherApp", u"Sun Protection recommended:", None))
        self.protection_time_overview.setText(QCoreApplication.translate("WeatherApp", u"xx:xxam to xx:xxpm", None))
        self.sunrise_overview.setText(QCoreApplication.translate("WeatherApp", u"Sunrise: xx:xx", None))
        self.sunset_overview.setText(QCoreApplication.translate("WeatherApp", u"Sunset: xx:xx", None))
        self.label_6.setText(QCoreApplication.translate("WeatherApp", u"Forecasted Amount of Rain Today: ", None))
        self.forecast_amount_of_rain_overview.setText(QCoreApplication.translate("WeatherApp", u"x-xmm", None))
        self.label_4.setText(QCoreApplication.translate("WeatherApp", u"Chance of Rain Today: ", None))
        self.chance_of_rain_overview.setText(QCoreApplication.translate("WeatherApp", u"x%", None))
        self.label.setText(QCoreApplication.translate("WeatherApp", u"N", None))
        self.label_25.setText(QCoreApplication.translate("WeatherApp", u"Current Wind Speed", None))
        self.wind_speed_overview.setText(QCoreApplication.translate("WeatherApp", u"xxkm/h direction", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.overview), QCoreApplication.translate("WeatherApp", u"Overview", None))
        self.highlights_gust_speed.setText(QCoreApplication.translate("WeatherApp", u"XXkm/h", None))
        self.highlights_gust_speed_time.setText(QCoreApplication.translate("WeatherApp", u"at xx:xx", None))
        self.label_35.setText(QCoreApplication.translate("WeatherApp", u"Highest Wind Gust", None))
        self.highlights_max_temp.setText(QCoreApplication.translate("WeatherApp", u"XX\u00b0", None))
        self.highlights_max_temp_time.setText(QCoreApplication.translate("WeatherApp", u"at xx:xx", None))
        self.label_29.setText(QCoreApplication.translate("WeatherApp", u"Highest Temperature", None))
        self.highlights_rain_since_9am.setText(QCoreApplication.translate("WeatherApp", u"Xmm", None))
        self.label_37.setText(QCoreApplication.translate("WeatherApp", u"since 9am", None))
        self.label_38.setText(QCoreApplication.translate("WeatherApp", u"Rain", None))
        self.highlights_min_temp.setText(QCoreApplication.translate("WeatherApp", u"XX\u00b0", None))
        self.highlights_min_temp_time.setText(QCoreApplication.translate("WeatherApp", u"at xx:xx", None))
        self.label_32.setText(QCoreApplication.translate("WeatherApp", u"Lowest Temperature", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.past_weather), QCoreApplication.translate("WeatherApp", u"Past", None))
        self.forecast_day1_icon.setText(QCoreApplication.translate("WeatherApp", u"O", None))
        self.forecast_day1_name.setText(QCoreApplication.translate("WeatherApp", u"TextLabel", None))
        self.forecast_day2_icon.setText(QCoreApplication.translate("WeatherApp", u"O", None))
        self.forecast_day2_name.setText(QCoreApplication.translate("WeatherApp", u"TextLabel", None))
        self.forecast_day3_icon.setText(QCoreApplication.translate("WeatherApp", u"O", None))
        self.forecast_day3_name.setText(QCoreApplication.translate("WeatherApp", u"TextLabel", None))
        self.forecast_day4_icon.setText(QCoreApplication.translate("WeatherApp", u"O", None))
        self.forecast_day4_name.setText(QCoreApplication.translate("WeatherApp", u"TextLabel", None))
        self.forecast_day5_icon.setText(QCoreApplication.translate("WeatherApp", u"O", None))
        self.forecast_day5_name.setText(QCoreApplication.translate("WeatherApp", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.forecast_weather), QCoreApplication.translate("WeatherApp", u"Forecast", None))
        self.label_3.setText(QCoreApplication.translate("WeatherApp", u"Gavin's Weather", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settings), QCoreApplication.translate("WeatherApp", u"Settings", None))
    # retranslateUi

