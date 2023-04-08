from os import path, environ
from platform import system


class Env:
  __APP_NAME = 'M-Power File Exporter'
  __COMMAND = 'OS_COMMAND'
  __EXPORT_PATH = 'APP_DEFAULT_EXPORT_PATH'
  __PASSWORD = 'APP_PASSWORD'

  def __init__(self) -> None:
    self.__set_os_command()
    self.__set_default_path()
    self.__set_password()

  def __set_os_command(self) -> None:
    os_name = system()

    if ('Window' in os_name):
      environ[self.__COMMAND] = 'start'
      return

    if ('Mac' in os_name or 'Darwin' in os_name):
      environ[self.__COMMAND] = 'open'
      return

    if ('Linux' in os_name):
      environ[self.__COMMAND] = 'open'
      return

  def __set_default_path(self) -> None:
    window_path = path.expanduser('~').replace('\\', '/')
    window_desktop_path = 'Desktop'

    environ[self.__EXPORT_PATH] = '/'.join([window_path, window_desktop_path])

  def __set_password(self) -> None:
    with open('.password', 'r', encoding='UTF-8') as conf:
      environ[self.__PASSWORD] = conf.read()

  @property
  def app_name(self) -> str:
    return self.__APP_NAME

  @property
  def app_os_command(self) -> str:
    return environ.get(self.__COMMAND)

  @property
  def app_export_path(self) -> str:
    return environ.get(self.__EXPORT_PATH)

  @property
  def app_password(self) -> str:
    return environ.get(self.__PASSWORD)
