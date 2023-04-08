from typing import Callable

from PyQt5.QtWidgets import QPushButton


class FileImportButton(QPushButton):
  def __init__(self, click_event: Callable[[], None]) -> None:
    QPushButton.__init__(self, '파일 불러오기')

    self.clicked.connect(click_event)


class FileExportButton(QPushButton):
  def __init__(self, click_event: Callable[[], None]) -> None:
    QPushButton.__init__(self, '반출')

    self.clicked.connect(click_event)


class FileRemoveButton(QPushButton):
  def __init__(self, click_event: Callable[[], None]) -> None:
    QPushButton.__init__(self, '제거')

    self.clicked.connect(click_event)
