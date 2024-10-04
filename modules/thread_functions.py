from PySide6.QtCore import QObject, QThread, Signal
from myfunction import *
from openpyxl import load_workbook


class LoginWorker(QThread):

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

class MainWorker(QThread):

    run_ready = Signal(str)

    def __init__(self, dic) -> None:
        super().__init__()
        self.dic = dic
    
    def read_excel(self, path, col_tag="A", part=None, sheet=None):
        B = Base_Class()
        lis = B.read_file(path, col_tag, part, sheet)
        if isinstance(lis, str):
            raise lis
        elif isinstance(lis, list):
            return lis
        
    def run(self):
        try:
            lis = self.read_excel(path=self.dic.get('path'), col_tag=self.dic.get('col'), part=f"{self.dic.get('start_row')},{self.dic.get('end_row')}", sheet=self.dic.get('sheet'))
        except Exception as E:
            self.run_ready.emit(E)
        else:
            try:
                if self.dic.get('jb_status'):
                    jb = RL()
                    jb.main(lis)
                if self.dic.get('tz_status'):
                    tz = JB()
                    tz.main(lis)
                if self.dic.get('cb_status'):
                    cb = JC_Query()
                    cb.main(lis)
            except Exception as E:
                self.run_ready.emit(E)
            else:
                self.run_ready.emit('导出完成')


class SearchWorker(QThread):

    search_result = Signal(dict)

    def __init__(self, idcard) -> None:
        super().__init__()
        self.idcard = idcard

    def run(self):
        cb = JC_Query()
        dic = cb.search(self.idcard)
        data = dic.get(self.idcard)
        self.search_result.emit(data)
