from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import urllib.request


class Downloader(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        layout = QVBoxLayout()

        self.url = QLineEdit()
        self.save_location = QLineEdit()
        self.progress = QProgressBar()
        download = QPushButton("Download")

        self.url.setPlaceholderText("URL")
        self.save_location.setPlaceholderText("File save location")
        self.progress.setValue(0)
        self.progress.setAlignment(Qt.AlignHCenter)

        layout.addWidget(self.url)
        layout.addWidget(self.save_location)
        layout.addWidget(self.progress)
        layout.addWidget(download)

        self.setLayout(layout)
        self.setWindowTitle("File Downloader Application")
        self.setFocus()

        download.clicked.connect(self.download)

    # eventhandler
    def download(self):
        url = self.url.text()
        save_location = self.save_location.text()
        urllib.request.urlretrieve(url, save_location, self.report)


    def report(self, blocknum, blocksize, totalsize):
        readsofar = blocknum * blocksize
        if totalsize > 0:
            percent = readsofar * 100 / totalsize
            self.progress.setValue(int(percent))


app = QApplication(sys.argv)
dl = Downloader()
dl.show()
app.exec_()
