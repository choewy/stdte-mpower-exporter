from PyQt5.QtWidgets import QVBoxLayout, QGroupBox, QListWidget


class FileWidgetLayout(QVBoxLayout):
  def __init__(
      self,
      button_group: QGroupBox,
      import_file_list: QListWidget,
      export_file_list: QListWidget
  ) -> None:
    QVBoxLayout.__init__(self)

    self.addWidget(button_group)
    self.addWidget(import_file_list)
    self.addWidget(export_file_list)
