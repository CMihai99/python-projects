'''
Developed by: Calinescu Mihai
Date: Feb, 2021

Github: https://github.com/CMihai99
'''

# Import Required Packages
import os, sys, qrcode
from PIL.ImageQt import ImageQt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QStatusBar, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QFont, QPixmap, QImage, QIcon
from PyQt5.QtCore import Qt

# Implement Main Function
class QRCodeGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(600, 525)
        self.setWindowTitle('QR Code Generator')
        self.setWindowIcon(QIcon("icon.png"))
        self.initUI()

    def initUI(self):
        # Window Setup
        font = QFont('Open Sans', 15)
        mainLayout = QVBoxLayout()
        entryLayout = QHBoxLayout()
        buttonLayout = QHBoxLayout()
        imageLayout = QVBoxLayout()
        imageLayout.addStretch()

        # Label Setup
        label = QLabel('Enter Text: ')
        label.setFont(font)
        self.textEntry = QLineEdit()
        self.textEntry.setFont(font)
        entryLayout.addWidget(label)
        entryLayout.addWidget(self.textEntry)
        mainLayout.addLayout(entryLayout)

        # Button Setup
        self.buttonGenerate = QPushButton('Generate QR Code')
        self.buttonGenerate.clicked.connect(self.create_qr_code)
        self.buttonSaveImage = QPushButton('Save As Image')
        self.buttonSaveImage.clicked.connect(self.save_qr_code)
        self.buttonClear = QPushButton('Clear')
        self.buttonClear.clicked.connect(self.clear_fields)

        buttonLayout.addWidget(self.buttonGenerate)
        buttonLayout.addWidget(self.buttonSaveImage)
        buttonLayout.addWidget(self.buttonClear)
        mainLayout.addLayout(buttonLayout)

        self.imageLabel = QLabel()
        self.imageLabel.setAlignment(Qt.AlignCenter)
        imageLayout.addWidget(self.imageLabel)
        mainLayout.addLayout(imageLayout)

        # Run Window
        self.statusBar = QStatusBar()
        mainLayout.addWidget(self.statusBar)
        self.setLayout(mainLayout)

    # Implement Func To Clear Fields
    def clear_fields(self):
        self.textEntry.clear()
        self.imageLabel.clear()

    # Implement Func To Create QR Code
    def create_qr_code(self):
        text = self.textEntry.text()
        img = qrcode.make(text)
        qr = ImageQt(img)
        pic = QPixmap.fromImage(qr)
        self.imageLabel.setPixmap(pic)

    # Implement Func To Save QR Code
    def save_qr_code(self):
        current_dir = os.getcwd()
        file_name = self.textEntry.text()
        if file_name:
            self.imageLabel.pixmap().save(os.path.join(current_dir, file_name + '.png'))
            self.statusBar.showMessage('Image saved at {0}'.format(os.path.join(current_dir, file_name + '.png')))

# Run App
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet('QPushButton{Height: 34px; font-size: 17px;}')
    demo = QRCodeGenerator()
    demo.show()
    sys.exit(app.exec_())
