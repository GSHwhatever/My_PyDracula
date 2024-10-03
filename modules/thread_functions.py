from PySide6.QtCore import QThread, Signal
from myfunction import *


class Worker(QThread):

    result_ready = Signal(str, str, str)

    def __init__(self, name, idcard, Login) -> None:
        super().__init__()
        self.L = Login
        self.name = name
        self.idcard = idcard

    def run(self):
        try:
            user, origin, error = self.L.main(name=self.name, idcard=self.idcard)
        finally:
            self.result_ready.emit(user, origin, error)

