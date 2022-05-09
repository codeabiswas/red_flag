import sys
from PyQt5 import QtCore, QtWidgets, QtMultimedia
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize    

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # Title of the Window
        self.setWindowTitle("Red Flag Button") 

        pybutton = QPushButton('Red Flag', self)
        pybutton.clicked.connect(self.clickMethod)
        # Make it the main widget of this window
        self.setCentralWidget(pybutton)

    def clickMethod(self):
        print('RED FLAG')
        # Play the sound
        QtMultimedia.QSound.play("/Users/dragonfruit/Developer/red_flag/src/assets/red_flag_bitch.wav")

if __name__ == "__main__":
    # Initialize the application
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )
