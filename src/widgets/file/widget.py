from typing import List

from PyQt5.QtWidgets import QWidget, QMainWindow

from widgets.file.lists import FileWidgetImportList, FileWidgetExportList
from widgets.file.buttons import FileImportButton, FileExportButton, FileRemoveButton
from widgets.file.groups import FileWidgetButtonGroup
from widgets.file.layouts import FileWidgetLayout

class FileWidget(QWidget):
  FILES: List[str] = []

  def __init__(self, window: QMainWindow) -> None:
    QWidget.__init__(self)

    self.window = window
    self.import_file_list = FileWidgetImportList(self.FILES)
    self.export_file_list = FileWidgetExportList(self.FILES)

    self.setLayout(FileWidgetLayout(
      FileWidgetButtonGroup(
        FileImportButton(self.on_click_import_button),
        FileExportButton(self.on_click_export_button),
        FileRemoveButton(self.on_click_remove_button)
      ),
      self.import_file_list,
      self.export_file_list
    ))

  def on_click_import_button(self) -> None:
    self.import_file_list.import_files()

  def on_click_export_button(self) -> None:
    self.export_file_list.export_files()
    self.import_file_list.clear()

  def on_click_remove_button(self) -> None:
    self.import_file_list.remove_files()
