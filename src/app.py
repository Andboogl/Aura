"""
This module is responsible for the main window of the program.
© Andboogl, Andrii Beznosov, 2024
"""


from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import Qt
from design import MainWindowDesign


class MainWindow(QMainWindow):
    """The main window of the program"""
    def __init__(self) -> None:
        """Initializing the main window"""
        QMainWindow.__init__(self)

        # Design upload
        self.__design = MainWindowDesign(main_window=self)

        # Buttons pressing
        self.__design.back.clicked.connect(self.__design.view_engine.back)
        self.__design.forward.clicked.connect(self.__design.view_engine.forward)
        self.__design.home.clicked.connect(self.home_page)

        self.home_page()

    def home_page(self) -> None:
        with open('pages/home_page.html', 'r', encoding='utf-8') as home_page_file:
            home_page_html = home_page_file.read()

        self.__design.view_engine.setHtml(home_page_html)

    def search(self) -> None:
        """Search user request"""
        link = f'https://www.google.com/search?q={self.__design.search.text()}'
        self.__design.view_engine.setUrl(QUrl(link))

    def keyPressEvent(self, a0) -> None:
        if a0.key() == 16777220:
            self.search()
