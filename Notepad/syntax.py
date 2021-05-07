'''
Developed by: Calinescu Mihai
Date: 20 Mar, 2021

Github: https://github.com/CMihai99
'''


# Import Required Packages
import sys
from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtGui import QColor, QTextCharFormat, QFont, QPalette, QSyntaxHighlighter
from PyQt5.QtWidgets import QMainWindow, QApplication, QPlainTextEdit

# Format styles and colors
def format(color, style=''):
    word_color = QColor()
    word_color.setNamedColor(color)
    word_format = QTextCharFormat()
    word_format.setForeground(word_color)

    if 'italic' in style:
        word_format.setFontItalic(True)
    elif 'bold' in style:
        word_format.setFontWeight(QFont.Bold)
    return word_format

# Styles
style = {
    'keywords': format('#A9AA1E'),
    'booleans': format('#FF9933'),
    'operators': format('#52A54B'),
    'braces': format('#FEDE00'),
    'comments': format('#9EAF9F', 'italic'),
    'string': format('#42BDAD'),
    'doc_string': format('#42BDAD'),
    'self': format('#5D48B4'),
    'numbers': format('#EA6868'),
    'lightmode_letters': format('#000000'),
    'nightmode_letters': format('#f4f4f4'),
}

# Syntax Highlighting
class PythonHighlighter(QSyntaxHighlighter):

    keywords = [
        'and', 'as', 'assert', 'break', 'continue', 'class',
        'del', 'def', 'elif', 'else', 'except', 'exec', 'finally',
        'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
        'not', 'or', 'pass', 'print', 'raise', 'return', 'try', 'while',
        'with', 'yield', '\:',
    ]

    booleans = [
        'True', 'False', 'None',
    ]

    operators = [
        '=',
        '==', '!=', '<', '<=', '>', '>=',
        '\+', '-', '\*', '/', '//', '\%', '\*\*',
        '\+=', '-=', '\*=', '/=', '\%=',
        '\^', '\|', '\&', '\~', '>>', '<<',
    ]

    braces = [
        '\{', '\}', '\[', '\]', '\(', '\)'
    ]

    def __init__(self, document):

        QSyntaxHighlighter.__init__(self, document)

        self.triple_single = (QRegExp("\'\'\'"), 1, style['doc_string'])
        self.triple_double = (QRegExp('\"\"\"'), 2, style['doc_string'])

        # RULES
        rules = []
        # r'' regular expression
        # [] used to indicate set of characters
        # \b matches the empty string, but only at the beginning or end of the word
        # \w matches any alphanumeric chars and the underscore
        # \s matches any whitespace char
        # * causes the resulting regexp to match 0 or more repetitions of the preceding regexp. ab* = a, ab, abb, abbb..
        # + causes the resulting regexp to match 1 or more repetitions of the preceding regexp. ab+ = ab, abb, abbbb..
        # ? causes the resulting regexp to match 0 or 1 repetitions of the preceding regexp. ab? = a, ab
        # ^ matches the start of the string, and in multi line mode also matches immediately after each new line
        # ?: A non-capturing version of regular parentheses
        # QRegExp, int, style

        rules += [(r'\b%s\b' % keyword, 0, style['keywords']) for keyword in PythonHighlighter.keywords]
        rules += [(r'\b%s\b' % boolean, 0, style['booleans']) for boolean in PythonHighlighter.booleans]
        rules += [(r'%s' % operator, 0, style['operators']) for operator in PythonHighlighter.operators]
        rules += [(r'%s' % brace, 0, style['braces']) for brace in PythonHighlighter.braces]

        # Other rules:
        rules += [
            # self
            (r'\bself\b', 0, style['self']),
            # string containing double-quote with escape sequence
            (r'"[^"\\]*(\\.[^"\\]*)*"', 0, style['string']),
            # string containing single-quote with escape sequence
            (r"'[^'\\]*(\\.[^'\\]*)*'", 0, style['string']),
            # from # until new-line
            (r'#[^\n]*', 0, style['comments']),
            # numbers
            (r'\b[+-]?[0-9]+[lL]?\b', 0, style['numbers']),
            (r'\b[+-]?[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?\b', 0, style['numbers']),
        ]

        # Build QRegExp for each pattern
        self.rules = [(QRegExp(pattern), index, fmt) for (pattern, index, fmt) in rules]
    
    # Block highlighting
    def highlightBlock(self, text):
        for expression, nth, format in self.rules:
            index = expression.indexIn(text, 0)

            while index >= 0:
                index = expression.pos(nth)

                length = len(expression.cap(nth))

                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)

        self.setCurrentBlockState(0)

        in_multiline = self.match_multiline(text, *self.triple_single)
        if not in_multiline:
            in_multiline = self.match_multiline(text, *self.triple_double)

    # Match multiline highlighting
    def match_multiline(self, text, delimiter, in_state, style):
        if self.previousBlockState() == in_state:
            start = 0
            add = 0
        else:
            start = delimiter.indexIn(text)
            add = delimiter.matchedLength()

        while start >= 0:
            end = delimiter.indexIn(text, start + add)
            if end >= add:
                length = end - start + add + delimiter.matchedLength()
                self.setCurrentBlockState(0)
            else:
                self.setCurrentBlockState(in_state)
                length = len(text) - start + add

            self.setFormat(start, length, style)
            start = delimiter.indexIn(text, start + length)

        if self.currentBlockState() == in_state:
            return True
        else:
            return False

# Example window
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.text_editor = QPlainTextEdit()
        self.syntax = PythonHighlighter(self.text_editor.document())

        self.init_ui()


# Run program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
