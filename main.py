from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from sys import argv
from shutil import copyfile
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

class Sign(QWidget):
    def __init__(self, window):
        QWidget.__init__(self)
        self.window = window
        self.inputPwd = QLineEdit()
        self.inputPwd.setPlaceholderText("인증 키 입력")
        self.inputPwd.setAlignment(Qt.AlignCenter)
        self.inputPwd.setEchoMode(QLineEdit.Password)
        self.btnSign = QPushButton("접속")
        self.btnSign.setShortcut("Return")
        self.btnSign.clicked.connect(self.btnClickEvent)

        layout = QVBoxLayout()
        layout.addWidget(self.inputPwd, stretch=0, alignment=Qt.AlignBottom)
        layout.addWidget(self.btnSign, stretch=0, alignment=Qt.AlignTop)
        self.setLayout(layout)

    def btnClickEvent(self):
        if self.inputPwd.text() == os.environ.get("PASSWORD"):
            self.window.setCentralWidget(Widget(self))
        else:
            self.inputPwd.clear()


class Widget(QWidget):
    def __init__(self, window):
        QWidget.__init__(self)
        self.window = window

        self.files = []
        self.userPath = os.path.expanduser("~").replace("\\", "/") + "/Desktop"

        self.listYetFiles = QListWidget()
        self.listYetFiles.setSelectionMode(QAbstractItemView.MultiSelection)

        self.listCompleteFiles = QListWidget()
        self.listCompleteFiles.setSelectionMode(QAbstractItemView.NoSelection)

        self.btnFiles = QPushButton("파일 불러오기")
        self.btnFiles.clicked.connect(self.btnClickEvent)
        self.btnExport = QPushButton("반출")
        self.btnExport.clicked.connect(self.btnClickEvent)
        self.btnRemove = QPushButton("제거")
        self.btnRemove.clicked.connect(self.btnClickEvent)

        layout_btn = QHBoxLayout()
        layout_btn.addWidget(self.btnFiles, stretch=10, alignment=Qt.AlignLeft)
        layout_btn.addWidget(self.btnExport, stretch=0, alignment=Qt.AlignRight)
        layout_btn.addWidget(self.btnRemove, stretch=0, alignment=Qt.AlignRight)
        layout_btn.setContentsMargins(1, 1, 1, 1)
        self.groupBtn = QGroupBox()
        self.groupBtn.setLayout(layout_btn)

        layout = QVBoxLayout()
        layout.addWidget(self.groupBtn)
        layout.addWidget(self.listYetFiles)
        layout.addWidget(self.listCompleteFiles)

        self.setLayout(layout)

    def btnClickEvent(self):
        btn = self.sender().text()

        if btn == "파일 불러오기":
            files = QFileDialog.getOpenFileNames(self, caption="반출할 파일을 선택하세여.", directory="")[0]
            for file in files:
                if file not in self.files:
                    self.files.append(file)
                    self.listYetFiles.addItem(file)
        
        elif btn == "제거":
            for item in self.listYetFiles.selectedItems():
                self.files.remove(item.text())
            self.listYetFiles.clear()
            self.listYetFiles.addItems(self.files)

        elif btn == "반출":
            if self.files:
                now = datetime.now()
                dirName = f"반출-{now.strftime('%Y-%m-%d-%H%M%S')}"
                savePath = f"{self.userPath}/{dirName}"
                if not os.path.isdir(savePath):
                    os.mkdir(savePath)

                for file in self.files:
                    copyfile(file, f"{savePath}/{file.split('/')[-1]}")
                    self.listCompleteFiles.addItem(f"{now.strftime('%Y-%m-%d %H:%M:%S')}\t{file.split('/')[-1]}")

                self.listYetFiles.clear()
                self.files.clear()
                os.startfile(savePath)


class Main(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("M-Power Master")
        self.setMinimumWidth(350)
        self.setMinimumHeight(150)

        sign = Sign(self)
        self.setCentralWidget(sign)


def run():
    app = QApplication(argv)
    main = Main()
    main.show()
    app.exec_()


if __name__ == "__main__":
    try:
        run()
    except:
        os.system("pip install pyqt5==5.15.0")
        run()
