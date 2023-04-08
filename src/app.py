from sys import argv

from PyQt5.QtWidgets import QApplication

from window import MainWindow

class Application(QApplication):
  def __init__(self) -> None:
    QApplication.__init__(self, argv)

    self.window = MainWindow()
    self.window.show_sign_widget()

  def bootstrap(self) -> None:
    self.window.show()
    self.exec_()
