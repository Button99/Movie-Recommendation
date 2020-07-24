from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QVBoxLayout, QLineEdit

app=QApplication([])

window= QWidget()
layout=QVBoxLayout()

layout.addWidget(QPushButton("Search"))
layout.addWidget(QPushButton("Cancel"))
layout.addWidget(QLineEdit())

window.setLayout(layout)
window.show()

app.exec_()