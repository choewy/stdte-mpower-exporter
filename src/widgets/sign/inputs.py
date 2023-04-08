from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit


class SignPasswordInput(QLineEdit):
  def __init__(self) -> None:
    QLineEdit.__init__(self)
    self.setPlaceholderText('인증 키 입력')
    self.setAlignment(Qt.AlignCenter)
    self.setEchoMode(QLineEdit.Password)
