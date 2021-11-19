'''
Developed by: Calinescu Mihai
Date: Feb, 2021

Github: https://github.com/CMihai99
'''

# Import Required Packages
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTreeView, QFileSystemModel, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QModelIndex

# Main Window
class FileView(QWidget):
	def __init__(self, dir_path):
		super().__init__()
		# Setup Window
		self.setFixedSize(700, 300)
		self.setWindowTitle('File Viewer')
		self.setGeometry(640, 360, 700, 300)
		self.model = QFileSystemModel()
		self.model.setRootPath(dir_path)
		self.tree =  QTreeView()
		self.tree.setModel(self.model)
		self.tree.setRootIndex(self.model.index(dirPath))
		self.tree.setColumnWidth(0, 250)
		self.tree.setAlternatingRowColors(True)

		# Layout
		layout = QVBoxLayout()
		layout.addWidget(self.tree)
		self.setLayout(layout)

# Run App
if __name__ == '__main__':
	app = QApplication(sys.argv)
	dirPath = r'<Your directory>'
	demo = FileView(dirPath)
	demo.show()
	sys.exit(app.exec_())