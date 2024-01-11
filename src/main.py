"""
Aura is a free browser based on the Python programming language.
You can modify the source code and add or remove what you want.
Based on this code, you can create your own browser.

© Andboogl, 2024
"""


from sys import argv
from PyQt6.QtWidgets import QApplication
from app import MainWindow


def main() -> None:
    """The function starts the program"""
    app = QApplication(argv)
    main_window = MainWindow()
    main_window.show()
    app.exec()


if __name__ == '__main__':
    main()
