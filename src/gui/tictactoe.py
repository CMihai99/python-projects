'''
Developed by: Calinescu Mihai
Date: Feb, 2021

Github: https://github.com/CMihai99
'''


# Import Required Packages
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

# Create Window class
class Window(QMainWindow):
	def __init__(self):
		super().__init__()
		# Window Setup
		self.setWindowTitle("Tic-Tac-Toe")
		self.setFixedSize(300, 450)
		self.UiComponents()
		self.show()
		self.setFixedWidth(300)
		self.setFixedHeight(450)

	# Method For Components
	def UiComponents(self):
		self.turn = 0
		self.times = 0

		# Creating Push Button List
		self.push_list = []

		# Creating 2D List
		for _ in range(3):
			temp = []
			for _ in range(3):
				temp.append((QPushButton(self)))

			# Adding 3 Push buttons In Single Row
			self.push_list.append(temp)
		x = 90
		y = 90

		# Traversing Through Push Button List
		for i in range(3):
			for j in range(3):
				self.push_list[i][j].setGeometry(x*i + 20,
												y*j + 20,
												80, 80)

				# Button Font
				self.push_list[i][j].setFont(QFont(QFont('Times', 17)))

				# Adding Action
				self.push_list[i][j].clicked.connect(self.action_called)

		# Score Label Setup
		self.label = QLabel(self)
		self.label.setGeometry(20, 300, 260, 60)
		self.label.setStyleSheet("QLabel"
								"{"
								"border : 1px solid black;"
								"}")
		self.label.setAlignment(Qt.AlignCenter)
		self.label.setFont(QFont('Times', 15))

		# Reset Button Setup
		reset_game = QPushButton("Play Again", self)
		reset_game.setGeometry(20, 380, 260, 50)
		reset_game.clicked.connect(self.reset_game_action)

	# Method Called By Reset Button
	def reset_game_action(self):

		# Resetting Values
		self.turn = 0
		self.times = 0

		# Making Label Text Empty
		self.label.setText("")
		for buttons in self.push_list:
			for button in buttons:

				# Enabling All The Buttons
				button.setEnabled(True)

				# Removing Text Of All The Buttons
				button.setText("")

	# Action Called By The Push Buttons
	def action_called(self):
		self.times += 1

		# Getting Button Which Called The Action
		button = self.sender()

		# Disabling Button
		button.setEnabled(False)

		# Checking Turn
		if self.turn == 0:
			button.setText("X")
			self.turn = 1
		else:
			button.setText("O")
			self.turn = 0

		# Call The Winner Checker Method
		win = self.who_wins()
		text = ""

		# If Winner Is Decided
		if win == True:
			# If current chance is 0
			if self.turn == 0:
				# O won
				text = "O Won."
			else:
				# X won
				text = "X Won."

			# Disabling All The Buttons
			for buttons in self.push_list:
				for push in buttons:
					push.setEnabled(False)

		# If Winner Is Not Decided And Total Times Is 9
		elif self.times == 9:
			text = "Draw."

		# Setting Text To Label
		self.label.setText(text)

	# Method To Check Who Wins
	def who_wins(self):
		# Checking If Any Row Crossed
		for i in range(3):
			if self.push_list[0][i].text() == self.push_list[1][i].text() \
					and self.push_list[0][i].text() == self.push_list[2][i].text() \
					and self.push_list[0][i].text() != "":
				return True

		# Checking If Any Column Crossed
		for i in range(3):
			if self.push_list[i][0].text() == self.push_list[i][1].text() \
					and self.push_list[i][0].text() == self.push_list[i][2].text() \
					and self.push_list[i][0].text() != "":
				return True

		# Checking If Diagonal Crossed
		if self.push_list[0][0].text() == self.push_list[1][1].text() \
				and self.push_list[0][0].text() == self.push_list[2][2].text() \
				and self.push_list[0][0].text() != "":
			return True

		# If Other Diagonal Is Crossed
		if self.push_list[0][2].text() == self.push_list[1][1].text() \
				and self.push_list[1][1].text() == self.push_list[2][0].text() \
				and self.push_list[0][2].text() != "":
			return True

		# If Nothing Is Crossed
		return False

# Run
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())