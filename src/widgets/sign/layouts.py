from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QLineEdit, QPushButton


class SignWidgetLayout(QVBoxLayout):
  def __init__(self, input_widget: QLineEdit, button_widget: QPushButton) -> None:
    QVBoxLayout.__init__(self)
      
    self.addWidget(input_widget, stretch = 0, alignment = Qt.AlignBottom)
    self.addWidget(button_widget, stretch = 0, alignment = Qt.AlignTop)
