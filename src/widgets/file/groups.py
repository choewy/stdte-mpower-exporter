from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout, QGroupBox, QPushButton


class FileWidgetButtonGroup(QGroupBox):
  def __init__(
      self,
      import_button: QPushButton,
      export_button: QPushButton,
      remove_button: QPushButton
  ) -> None:
    QGroupBox.__init__(self)

    layout = QHBoxLayout()
    layout.addWidget(import_button, stretch = 10, alignment = Qt.AlignLeft)
    layout.addWidget(export_button, stretch = 0, alignment = Qt.AlignRight)
    layout.addWidget(remove_button, stretch = 0, alignment = Qt.AlignRight)
    layout.setContentsMargins(1, 1, 1, 1)

    self.setLayout(layout)
