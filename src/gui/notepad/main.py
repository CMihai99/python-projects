'''
Developed by: Calinescu Mihai
Date: 20 Mar, 2021

Github: https://github.com/CMihai99
'''


# Import Required Packages
import sys, os
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPlainTextEdit, QStatusBar, QToolBar, QVBoxLayout, QAction, QFileDialog, QMessageBox, QPushButton
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFontDatabase, QIcon, QKeySequence, QColor
from PyQt5.QtPrintSupport import QPrintDialog
import syntax

# Main Window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.screen_width, self.screen_height = self.geometry().width(), self.geometry().height()
        self.resize(self.screen_width * 2, self.screen_height * 2)
        self.filterTypes = 'Text Document (*.txt);; Python File (*.py);; Markdown File (*.md)'
        self.path = None
        fixedFont = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        fixedFont.setPointSize(12)
        mainLayout = QVBoxLayout()

        # Editor
        self.editor = QPlainTextEdit()
        self.editor.setFont(fixedFont)
        self.syntax = syntax.PythonHighlighter(self.editor.document())
        mainLayout.addWidget(self.editor)

        # Status Bar
        self.statusBar = self.statusBar()

        # App Container
        container = QWidget()
        container.setLayout(mainLayout)
        self.setCentralWidget(container)

        # File Menu
        file_menu = self.menuBar().addMenu('&File')

        # Open, Save, Save As
        open_file_action = QAction(QIcon(''), 'Open...', self)
        open_file_action.setStatusTip('Open file')
        open_file_action.setShortcut(QKeySequence.Open)
        open_file_action.triggered.connect(self.file_open)

        save_file_action = self.create_action(self, '', 'Save', 'Save', self.file_save)
        save_file_action.setShortcut(QKeySequence.Save)

        save_fileAs_action = self.create_action(self, '', 'Save As...', 'Save as', self.file_saveAs)
        save_fileAs_action.setShortcut(QKeySequence('Ctrl+Shift+S'))

        file_menu.addActions([open_file_action, save_file_action, save_fileAs_action])

        # Separator
        file_menu.addSeparator()

        # Print
        print_action = self.create_action(self, '', 'Print', 'Print', self.print_file)
        print_action.setShortcut(QKeySequence.Print)
        file_menu.addAction(print_action)

        # Separator
        file_menu.addSeparator()

        # Exit
        exit_action = self.create_action(self, '', 'Exit', 'Exit', self.exit)
        file_menu.addAction(exit_action)

        # Edit Menu
        edit_menu = self.menuBar().addMenu('&Edit')

        # Undo, Redo
        undo_action = self.create_action(self, '', 'Undo', 'Undo', self.editor.undo)
        undo_action.setShortcut(QKeySequence.Undo)
        redo_action = self.create_action(self, '', 'Redo', 'Redo', self.editor.redo)
        redo_action.setShortcut(QKeySequence.Redo)
        edit_menu.addActions([undo_action, redo_action])

        # Separator
        edit_menu.addSeparator()

        # Cut, Copy, Paste, Select All
        cut_action = self.create_action(self, '', 'Cut', 'Cut', self.editor.cut)
        copy_action = self.create_action(self, '', 'Copy', 'Copy', self.editor.copy)
        paste_action = self.create_action(self, '', 'Paste', 'Paste', self.editor.paste)
        select_all_action = self.create_action(self, '', 'Select All', 'Select all', self.editor.selectAll)

        cut_action.setShortcut(QKeySequence.Cut)
        copy_action.setShortcut(QKeySequence.Copy)
        paste_action.setShortcut(QKeySequence.Paste)
        select_all_action.setShortcut(QKeySequence.SelectAll)
        edit_menu.addActions([cut_action, copy_action, paste_action, select_all_action])

        # Separator
        edit_menu.addSeparator()

        # Wrap Text
        wrap_text_action = self.create_action(self, '', 'Wrap Text', 'Wrap text', self.toggle_wrap_text)
        wrap_text_action.setShortcut('Ctrl+Shift+W')
        edit_menu.addAction(wrap_text_action)

        self.update_title()

    # Wrap Text
    def toggle_wrap_text(self):
        self.editor.setLineWrapMode(not self.editor.lineWrapMode())

    # lear Content
    def clear_content(self):
        self.editor.setPlainText('')

    # Open File
    def file_open(self):
        path, _ = QFileDialog.getOpenFileName(
            parent=self,
            caption='Open file',
            directory='',
            filter=self.filterTypes
        )

        if path:
            try:
                with open(path, 'r') as f:
                    text = f.read()
                    f.close()
            except Exception as e:
                self.dialog_message(str(e))
            else:
                self.path = path
                self.editor.setPlainText(text)
                self.update_title()

    # Save File
    def file_save(self):
        if self.path is None:
            self.file_saveAs()
        else:
            try:
                text = self.editor.toPlainText()
                with open(self.path, 'w') as f:
                    f.write(text)
                    f.close()
            except Exception as e:
                self.dialog_message(str(e))

    # Save File As
    def file_saveAs(self):
        path, _ = QFileDialog.getSaveFileName(
            self,
            'Save file as',
            '',
            self.filterTypes
        )
        text = self.editor.toPlainText()

        if not path:
            return
        else:
            try:
                with open(path, 'w') as f:
                    f.write(text)
                    f.close()
            except Exception as e:
                self.dialog_message(str(e))
            else:
                self.path = path
                self.update_title()

    # Print File
    def print_file(self):
        printDialog = QPrintDialog()
        if printDialog.exec_():
            self.editor.print_(printDialog.printer())

    # Rename File
    def rename_file(self):
        pass

    # Exit App
    def exit(self):
        sys.exit(app.exec_())

    # Update File
    def update_title(self):
        self.setWindowTitle('{0} - Notepad'.format(os.path.basename(self.path) if self.path else 'Unitled'))

    # Show action name in status bar
    def dialog_message(self, message):
        dlg = QMessageBox(self)
        dlg.setText(message)
        dlg.setIcon(QMessageBox.Critical)
        dlg.show()

    # Create Actions
    def create_action(self, parent, icon_path, action_name, set_status_tip, triggered_method):
        action = QAction(QIcon(icon_path), action_name, parent)
        action.setStatusTip(set_status_tip)
        action.triggered.connect(triggered_method)
        return action


# Run App
app = QApplication(sys.argv)
notePad = MainWindow()
notePad.show()
sys.exit(app.exec_())