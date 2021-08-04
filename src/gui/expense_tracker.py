'''
Developed by: Calinescu Mihai
Date: 8 Apr, 2021

Github: https://github.com/CMihai99
'''


import sys
import csv
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QPushButton, QAction, QHeaderView, QLineEdit, QLabel, QTableWidget, QTableWidgetItem, QVBoxLayout, QHBoxLayout)
from PyQt5.QtGui import QPainter, QStandardItemModel, QIcon
from PyQt5.Qt import Qt
from PyQt5.QtChart import QChart, QChartView, QPieSeries

# Data Entry
class DataEntryForm(QWidget):
	def __init__(self):
		super().__init__()
		self.items = 0
		
		# Data
		self._data = {}

		# Left Side
		self.table = QTableWidget()
		self.table.setColumnCount(2)
		self.table.setHorizontalHeaderLabels(('Description', 'Price'))
		self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

		self.layoutRight = QVBoxLayout()

		# Chart Widget
		self.chartView = QChartView()
		self.chartView.setRenderHint(QPainter.Antialiasing)

		self.lineEditDescription = QLineEdit()
		self.lineEditPrice = QLineEdit()
		self.buttonAdd = QPushButton('Add Expense')
		self.buttonClear = QPushButton('Clear All')
		self.buttonPlot = QPushButton('Pie Chart')

		self.buttonAdd.setEnabled(False)

		self.layoutRight.setSpacing(10)
		self.layoutRight.addWidget(QLabel('Description'))
		self.layoutRight.addWidget(self.lineEditDescription)
		self.layoutRight.addWidget(QLabel('Price'))
		self.layoutRight.addWidget(self.lineEditPrice)
		self.layoutRight.addWidget(self.buttonAdd)
		self.layoutRight.addWidget(self.buttonPlot)
		self.layoutRight.addWidget(self.chartView)
		self.layoutRight.addWidget(self.buttonClear)

		self.layout = QHBoxLayout()
		self.layout.addWidget(self.table, 50)
		self.layout.addLayout(self.layoutRight, 50)

		self.setLayout(self.layout)

		self.buttonClear.clicked.connect(self.reset_table)
		self.buttonPlot.clicked.connect(self.graph_chart)
		self.buttonAdd.clicked.connect(self.add_entry)

		self.lineEditDescription.textChanged[str].connect(self.check_disable)
		self.lineEditPrice.textChanged[str].connect(self.check_disable)

		self.fill_table()

	# Fill Table
	def fill_table(self, data=None):
		data = self._data if not data else data
		for desc, price in data.items():
			descItem = QTableWidgetItem(desc)
			priceItem = QTableWidgetItem('${0:.2f}'.format(price))
			priceItem.setTextAlignment(Qt.AlignRight | Qt.AlignCenter)
			self.table.insertRow(self.items)
			self.table.setItem(self.items, 0, descItem)
			self.table.setItem(self.items, 1, priceItem)
			self.items += 1

	# Add Entry
	def add_entry(self):
		desc = self.lineEditDescription.text()
		price = self.lineEditPrice.text()
		try:
			descItem = QTableWidgetItem(desc)
			priceItem = QTableWidgetItem('${0:.2f}'.format(float(price)))
			priceItem.setTextAlignment(Qt.AlignRight | Qt.AlignCenter)
			self.table.insertRow(self.items)
			self.table.setItem(self.items, 0, descItem)
			self.table.setItem(self.items, 1, priceItem)
			self.items += 1
			self.lineEditDescription.setText('')
			self.lineEditPrice.setText('')
		except ValueError:
			pass

	# Check If Buttons Are Disabled
	def check_disable(self):
		if self.lineEditDescription.text() and self.lineEditPrice.text():
			self.buttonAdd.setEnabled(True)
		else:
			self.buttonAdd.setEnabled(False)

	# Reset Table
	def reset_table(self):
		self.table.setRowCount(0)
		self.items = 0
		chart = QChart()
		self.chartView.setChart(chart)

	# Graph Data Chart
	def graph_chart(self):
		series = QPieSeries()
		for i in range(self.table.rowCount()):
			text = self.table.item(i, 0).text()
			val = float(self.table.item(i, 1).text().replace('$', ''))
			series.append(text, val)

		chart = QChart()
		chart.addSeries(series)
		chart.legend().setAlignment(Qt.AlignTop)
		self.chartView.setChart(chart)

# Main Window
class MainWindow(QMainWindow):
	def __init__(self, w):
		# Setup Window
		super().__init__()
		self.setWindowTitle('Expense Tracker')
		self.resize(1200, 600)
		self.menuBar = self.menuBar()
		self.fileMenu = self.menuBar.addMenu('File')

		# Export to csv button
		exportAction = QAction('Export to CSV', self)
		exportAction.setShortcut('Ctrl+S')
		exportAction.triggered.connect(self.export_to_csv)

		self.fileMenu.addAction(exportAction)
		self.setCentralWidget(w)

	# Export Data to CSV
	def export_to_csv(self):
		try:
			with open('Expense Report.csv', 'w', newline='') as file:
				writer = csv.writer(file)
				writer.writerow((w.table.horizontalHeaderItem(0).text(), w.table.horizontalHeaderItem(1).text()))
				for rowNumber in range(w.table.rowCount()):
					writer.writerow([w.table.item(rowNumber, 0).text(), w.table.item(rowNumber, 1).text()])
				print('CSV file exported.')
			file.close()
		except Exception as e:
			print(e)

# Run Program
if __name__ == '__main__':
	app = QApplication(sys.argv)
	w = DataEntryForm()
	demo = MainWindow(w)
	demo.show()
	sys.exit(app.exec_())
