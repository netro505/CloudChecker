from stormdock import Stormpy_lib
import os

# importing libraries
from PyQt6.QtWidgets import *
from PyQt6 import QtCore, QtGui
from PyQt6.QtGui import *
from PyQt6.QtCore import *
# from PyQt6.QtWidgets import (
# QApplication,
# QMainWindow,
# QLabel,
# QLineEdit,
# QVBoxLayout,
# QWidget,
# QFileDialog,
# QPushButton,
# QScrollArea
# )
import sys
from pathlib import Path

# class for scrollable label
class ScrollLabel(QScrollArea):
 
    # constructor
    def __init__(self, *args, **kwargs):
        QScrollArea.__init__(self, *args, **kwargs)
 
        # making widget resizable
        self.setWidgetResizable(True)
 
        # making qwidget object
        content = QWidget(self)
        self.setWidget(content)
 
        # vertical box layout
        lay = QVBoxLayout(content)
 
        # creating label
        self.label = QLabel(content)
 
        # setting alignment to the text
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
 
        # making label multi-line
        self.label.setWordWrap(True)
 
        # adding label to the layout
        lay.addWidget(self.label)
 
    # the setText method
    def setText(self, text):
        # setting text to the label
        self.label.setText(text)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.path = ""

        self.setWindowTitle("My App")
        
        self.setWindowTitle('PyQt File Dialog')
        self.setGeometry(100, 100, 400, 100)

        # layout = QGridLayout()
        # self.setLayout(layout)

        # file selection
        file_browse = QPushButton('Browse')
        file_browse.clicked.connect(self.open_file_dialog)
        self.filename_edit = QLineEdit()

        # self.label = QLabel("No model has been check")
        self.label = ScrollLabel(self)
        self.label.setText("No model has been check")      

        self.properties_edit = QLineEdit()

        model_check = QPushButton('Model Check')
        model_check.clicked.connect(self.check_model_prob)

        # self.input = QLineEdit()
        # self.input.textChanged.connect(self.label.setText)
        layout = QVBoxLayout()
        layout.addWidget(QLabel('Select Model Specifications:'))
        # layout.addWidget(self.input)
        layout.addWidget(self.filename_edit)
        layout.addWidget(file_browse)
        layout.addWidget(QLabel('Enter properties specifications:'))
        layout.addWidget(self.properties_edit)
        layout.addWidget(self.label)
        layout.addWidget(model_check)
        # layout.addWidget(self.label)        
        container = QWidget()
        container.setLayout(layout)
        # Set the central widget of the Window.
        self.setCentralWidget(container)

    def open_file_dialog(self):
        filename, ok = QFileDialog.getOpenFileName(
            self,
            "Select a File", 
            "D:\\College\\SILIBUS\\Semester 6\\CSP650\\Final Year Project (FYP)\\FYP Project Storm Implementation\\CloudChecker"
            # "Images (*.png *.jpg)"
        )
        if filename:
            self.path = Path(filename)
            self.filename_edit.setText(str(self.path))

    def check_model_prob(self):
        properties_spec = self.properties_edit.text()  

        if self.path and properties_spec != "":
            file_name = os.path.basename(self.path)

            # prop_spec_formatized = properties_spec.replace('"', '\\"')

            with open('prop.txt', 'w') as f:
                f.write(properties_spec)

            # print(file_name)
            with open('model.txt', 'w') as f:
                f.write(file_name)        

            stormpy = Stormpy_lib
            prob = stormpy.check_model(file_name)
            self.label.setText(prob)
            # return prob


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

# Pmax=? [F<=8 "station"]