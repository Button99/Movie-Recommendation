''' Creating GUI '''



import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QMessageBox
from PyQt5.QtCore import pyqtSlot
# Import Rec.py
import Rec as r

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Movie Recommendation'
        self.left = 50
        self.top = 50
        self.width = 300
        self.height = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.textbox= QLineEdit(self)
        self.textbox.move(50, 60)
        self.textbox.resize(170, 30)

        self.button1 = QPushButton("Search Button", self)
        self.button1.setToolTip("Click to search similar movies")
        self.button1.move(50, 100)
        self.button1.clicked.connect(self.click_SearchButton)

        self.button2= QPushButton("Cancel Button", self)
        self.button2.setToolTip("Click to close the window")
        self.button2.move(130, 100)
        self.button2.clicked.connect(self.click_CancelButton)

        text= QLineEdit("Click")

        self.show()

    @pyqtSlot()
    # Function if the user clicks the Search button

    def click_SearchButton(self):
        print("Search button click")
        txtValue= self.textbox.text()
        print(txtValue)
        # File Creation and writting the textbox data
        f=open("SimMovie.txt", "w")
        f.write(txtValue)
        f.close()

        # Creating messagebox and showing the recommendations
        alert= QMessageBox()
        # Function from Rec.py file
        r.ReadFile()
        f=open("Rec_Movies.csv", "r")
        movies= f.read()
        # Showing the movies
        alert.setText(str(movies))
        alert.exec_()

    # Function if the user clicks the cancel button
    def click_CancelButton(self):
        print("Cancel button click")
        sys.exit(app.exec_())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())