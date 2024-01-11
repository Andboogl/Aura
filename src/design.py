"""
This module is responsible for the design of the program
© Andboogl, 2024
"""


from PyQt6 import QtWidgets
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize, Qt, QUrl


class MainWindowDesign:
    """Design of the main window"""
    def __init__(self, main_window: QtWidgets.QMainWindow) -> None:
        main_window.setWindowTitle('Aura')
        main_window.setStyleSheet('background: rgb(200, 200, 200);')
        main_window.setFixedSize(1000, 600)

        # Top panel
        # ——————————————————————————————————
        self.top_panel = QtWidgets.QFrame(main_window)
        self.top_panel.resize(946, 54)
        self.top_panel.move(26, 11)
        self.top_panel.setStyleSheet("""
background: #D9D9D9;
border-radius: 13px;
""")

        # Back button
        self.back = QtWidgets.QPushButton(self.top_panel)
        self.back.setIcon(QIcon('icons/back.png'))
        self.back.setIconSize(QSize(40, 40))
        self.back.move(15, 8)
        self.back.resize(40, 40)
        self.back.setCursor(Qt.CursorShape.PointingHandCursor)

        # Forward button
        self.forward = QtWidgets.QPushButton(self.top_panel)
        self.forward.setIcon(QIcon('icons/forward.png'))
        self.forward.setIconSize(QSize(45, 45))
        self.forward.move(65, 6)
        self.forward.resize(45, 45)
        self.forward.setCursor(Qt.CursorShape.PointingHandCursor)

        # Home button
        self.home = QtWidgets.QPushButton(self.top_panel)
        self.home.setIcon(QIcon('icons/home.png'))
        self.home.setIconSize(QSize(40, 40))
        self.home.move(120, 6)
        self.home.resize(40, 40)
        self.home.setCursor(Qt.CursorShape.PointingHandCursor)

        # Entering a page search
        self.search = QtWidgets.QLineEdit(self.top_panel)
        self.search.setPlaceholderText('Введіть запрос для пошука')
        self.search.setStyleSheet("""
border-radius: 16px;
background: #C2C0C0;
color: black;
padding-left: 5px;
""")
        self.search.resize(720, 40)
        self.search.move(205, 7)
        # ——————————————————————————————————

        # A widget that displays websites
        self.view_engine = QWebEngineView(main_window)
        self.view_engine.resize(949, 500)
        self.view_engine.move(23, 80)
        self.view_engine.setStyleSheet("""
background: #7E7E7E;
border-radius: 28px;
""")
        self.view_engine.back()
