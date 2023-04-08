import os

from typing import List
from shutil import copyfile
from datetime import datetime

from PyQt5.QtWidgets import QListWidget, QAbstractItemView, QFileDialog

from core import env

class FileWidgetImportList(QListWidget):
  def __init__(self, files: List[str]) -> None:
    QListWidget.__init__(self)

    self.files = files
    self.setSelectionMode(QAbstractItemView.MultiSelection)

  def import_files(self) -> None:
    targets = QFileDialog.getOpenFileNames(self, caption='반출할 파일을 선택하세요.', directory="")[0]

    for target in targets:
      if target in self.files:
        continue

      self.files.append(target)
      self.addItem(target)

  def remove_files(self) -> None:
    targets = self.selectedItems()

    for target in targets:
      self.files.remove(target.text())

    self.clear()
    self.addItems(self.files)

class FileWidgetExportList(QListWidget):
  def __init__(self, files: List[str]) -> None:
    QListWidget.__init__(self)

    self.files = files
    self.setSelectionMode(QAbstractItemView.MultiSelection)

  def __generate_export_dir_path(self) -> str:
    now = datetime.now().strftime('%Y-%m-%d-%H%M%S')
    dir_path = '-'.join(['반출', now])
    export_path = '/'.join([env.app_export_path, dir_path])

    if not os.path.isdir(export_path):
      os.mkdir(export_path)

    return export_path

  def export_files(self) -> None:
    if not self.files:
      return

    export_dir_path = self.__generate_export_dir_path()

    for target in self.files:
      origin_file_name = target.split('/')[-1]

      copyfile(target, '/'.join([export_dir_path, origin_file_name]))
      self.addItem('\t'.join([export_dir_path, origin_file_name]))

    self.files.clear()

    os.system(' '.join([env.app_os_command, export_dir_path]))
