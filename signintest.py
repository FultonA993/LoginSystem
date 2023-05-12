from PyQt5 import QtWidgets
import subprocess
import sys
from PyQt5.QtCore import Qt
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QMainWindow, QToolBar, QPushButton, QStatusBar, QMessageBox, QVBoxLayout, QLabel, QHBoxLayout, QLineEdit, QWidget,QGridLayout
from myDictionary import users

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app  # declare app member
        self.setWindowTitle("Sign In")
        self.setWindowFlags(Qt.WindowMaximizeButtonHint)

        #set the palette of the central widget to apply the background color
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#344D67"))

        #create the central widget and set its palette
        central_widget = QWidget()
        central_widget.setAutoFillBackground(True)
        central_widget.setPalette(palette)
        self.setCentralWidget(central_widget)
        
        #create the layout for the title and the other widgets
        title_label = QLabel("Forsyth Family Medicine")
        title_label.setStyleSheet('color: white; font-size: 66px; font-family: FreeSerif; border: 24px solid #ADE792;')
        title_label.setAlignment(Qt.AlignCenter)

        label_username = QLabel("Username:")
        label_username.setStyleSheet('color: white;')
        self.line_edit_username = QLineEdit()
        self.line_edit_username.setMaximumWidth(150)
        label_password = QLabel("Password:")
        label_password.setStyleSheet('color: white;')
        self.line_edit_password = QLineEdit()
        self.line_edit_password.setMaximumWidth(150)
        self.line_edit_password.setEchoMode(QLineEdit.Password)
        label_username.setAlignment(Qt.AlignCenter)
        sign_in_btn = QPushButton("Sign In")
        sign_in_btn.clicked.connect(self.sign_in)

        #sign_in_btn.clicked.connect(self.open_program)
        sign_in_btn.setStyleSheet("QPushButton { background-color: #7FB3D5; border-style: outset; border-width: 2px; border-radius: 10px; border-color: grey; font: bold 14px; padding: 6px; } QPushButton:pressed { background-color: #ffffff; border-style: inset; }")

        grid_layout = QGridLayout()
        grid_layout.addWidget(title_label, 0, 0, 1, 2, Qt.AlignCenter)
        grid_layout.addWidget(label_username, 1, 0, Qt.AlignRight)
        grid_layout.addWidget(self.line_edit_username,1, 1, Qt.AlignLeft)
        grid_layout.addWidget(label_password, 2 , 0 , Qt.AlignRight)
        grid_layout.addWidget(self.line_edit_password, 2, 1, Qt.AlignLeft)
        grid_layout.addWidget(sign_in_btn, 3, 0, 1, 2, Qt.AlignCenter)
        
        # set the layout of the central widget
        central_widget.setLayout(grid_layout)

        # menu bar
        menu_bar = self.menuBar()
        menu_bar.setStyleSheet('color: #6ECCAF;')
        file_menu = menu_bar.addMenu("&File")
        clear_action = file_menu.addAction("Clear")
        clear_action.triggered.connect(self.clear_data)
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit_app)

        edit_menu = menu_bar.addMenu("Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Cut")
        edit_menu.addAction("paste")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")
        #edit_action.triggered.connect(self.edit_data)

        menu_bar.addMenu("Setting")
        menu_bar.addMenu("Help")

        # toolbar
        toolbar = QToolBar("Toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)
        toolbar.addSeparator()

        # action to toolbar
        toolbar.addAction(quit_action)
        toolbar.addSeparator()

        self.setFixedSize(QSize(800, 600))

    def quit_app(self):
        self.app.quit()

    def clear_data(self):
        # Clear the list box
        self.line_edit_password.setText('')
        self.line_edit_username.setText('') 

    def sign_in(self):
        username = self.line_edit_username.text()
        password = self.line_edit_password.text()
        if username and password:
            for user in users:
                if user[0] == username and user[1] == password:
                    # found a matching username and password
                    QMessageBox.information(self, "Sign In", f"Welcome {username}!")
                    #will have a program path to open
                    #program_path = ""
                    # Run the program using subprocess
                    #subprocess.Popen([sys.executable, program_path])    
                    #self.quit_app()
                    return
            QMessageBox.warning(self, "Sign in", "Invalid username or password")
        else:
            QMessageBox.warning(self, "Sign in", "Please enter a username and password.")
