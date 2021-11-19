'''
Developed by: Calinescu Mihai
Date: 16 Feb, 2021

Github: https://github.com/CMihai99
'''


# Import Required Packages
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QSlider, QStyle, QSizePolicy, QFileDialog
import sys
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtCore import Qt, QUrl

class Window(QWidget):
    def __init__(self):
        super().__init__()
        # Setup Window
        self.setWindowTitle("MP4 Player")
        self.resize(1080, 720)
        self.setMinimumSize(720, 480)
        self.setMaximumSize(1440, 866)
        self.setAcceptDrops(True)
        p = self.palette()
        p.setColor(QPalette.Window, Qt.gray)
        self.setPalette(p)
        self.init_ui()
        self.show()

    def init_ui(self):
        # Media Player Object
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        # Videowidget Object
        videowidget = QVideoWidget()

        # Open Button
        openBtn = QPushButton('Open Video')
        openBtn.clicked.connect(self.open_file)

        # Play Button
        self.playBtn = QPushButton()
        self.playBtn.setEnabled(False)
        self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playBtn.clicked.connect(self.play_video)

        # Slider
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0,0)
        self.slider.sliderMoved.connect(self.set_position)

        # Label
        self.label = QLabel()
        self.label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)

        # HBox Layout
        hboxLayout = QHBoxLayout()
        hboxLayout.setContentsMargins(0,0,0,0)
        hboxLayout.addWidget(openBtn)
        hboxLayout.addWidget(self.playBtn)
        hboxLayout.addWidget(self.slider)

        # VBox Layout
        vboxLayout = QVBoxLayout()
        vboxLayout.addWidget(videowidget)
        vboxLayout.addLayout(hboxLayout)
        vboxLayout.addWidget(self.label)

        # Output Media
        self.setLayout(vboxLayout)
        self.mediaPlayer.setVideoOutput(videowidget)

        # Signals
        self.mediaPlayer.stateChanged.connect(self.mediastate_changed)
        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)

    # Open File From Internal Storage
    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open Video")
        if filename != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
            self.playBtn.setEnabled(True)

    # Play Video From Internal Storage
    def play_video(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    # Change Play Button To Pause Button Once Video Paused
    def mediastate_changed(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playBtn.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPause)
            )
        else:
            self.playBtn.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPlay)
            )

    # Change Slider Position
    def position_changed(self, position):
        self.slider.setValue(position)

    # Change Slider Duration
    def duration_changed(self, duration):
        self.slider.setRange(0, duration)

    # Set Media Player Position
    def set_position(self, position):
        self.mediaPlayer.setPosition(position)

    # Handle Media Player Errors
    def handle_errors(self):
        self.playBtn.setEnabled(False)
        self.label.setText("Error: " + self.mediaPlayer.errorString())

# Run Program
app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())