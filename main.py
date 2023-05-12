from PySide6.QtWidgets import QApplication
from signintest import MainWindow
import sys 

app = QApplication(sys.argv)

window = MainWindow(app)
window.show()

app.exec()