import sys
from PyQt6.QtWidgets import QApplication
from src.InicialGlobal import InicialGlobal

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = InicialGlobal()
    window.show()
    sys.exit(app.exec())