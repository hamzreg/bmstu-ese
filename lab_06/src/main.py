import sys
from PyQt6.QtWidgets import QApplication

from app.window import MainWindow


def run_app():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()


if __name__ == '__main__':
    run_app()
