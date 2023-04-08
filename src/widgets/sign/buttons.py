from typing import Callable

from PyQt5.QtWidgets import QPushButton


class SignPasswordButton(QPushButton):
  def __init__(self, click_event: Callable[[], None]) -> None:
    QPushButton.__init__(self, '접속')

    self.setShortcut('Return')
    self.clicked.connect(click_event)
