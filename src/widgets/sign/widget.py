from PyQt5.QtWidgets import QWidget, QMainWindow

from widgets.sign.inputs import SignPasswordInput
from widgets.sign.buttons import SignPasswordButton
from widgets.sign.layouts import SignWidgetLayout

from core import env


class SignWidget(QWidget):
  def __init__(self, window: QMainWindow) -> None:
    QWidget.__init__(self)

    self.window = window
    self.input = SignPasswordInput()
    self.button = SignPasswordButton(self.on_click_button)
    self.setLayout(SignWidgetLayout(self.input, self.button))

  def on_click_button(self) -> None:
    is_correct = self.input.text() == env.app_password
    return self.window.show_file_widget() if is_correct else self.input.clear()
