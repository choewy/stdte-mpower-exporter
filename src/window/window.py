from PyQt5.QtWidgets import QMainWindow

from widgets import SignWidget, FileWidget
from core import env


class MainWindow(QMainWindow):
  def __init__(self) -> None:
    QMainWindow.__init__(self)

    self.sign_widget = SignWidget(self)
    self.file_widget = FileWidget(self)

    self.setWindowTitle(env.app_name)
    self.setMinimumWidth(350)
    self.setMinimumHeight(150)

  def show_sign_widget(self) -> None:
    self.setCentralWidget(self.sign_widget)

  def show_file_widget(self) -> None:
    self.setCentralWidget(self.file_widget)
