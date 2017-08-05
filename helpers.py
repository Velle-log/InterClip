import pyperclip
from PyQt5 import Qt
import sys
import time

class ClipBoard:
    """
    Clipboard class holds the data copied or data
    to be pasted on dropbox
    """

    def __init__(self):
        self.state = None
        self.notifier = Notifier()

    def push_text(self, text):
        pyperclip.copy(text)
        self.state = text
        self.notifier.notify('Data Copied')

    def pull_text(self):
        self.notifier.notify('Data Pasted')
        if self.state is not None:
            return self.state
        return pyperclip.paste()

class Notifier:

    def __init__(self):
        self.application = Qt.QApplication(sys.argv)

    def notify(self, text):
        tray = Qt.QSystemTrayIcon(self.application)
        tray.show()
        tray.showMessage('InterClip Notification', text)
        time.sleep(3)
        tray.hide()
