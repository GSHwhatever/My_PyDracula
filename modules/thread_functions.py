from PySide6.QtCore import QObject, QThread, Signal
from myfunction import *
import subprocess


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
        except Exception as E:
            print(f'login_error:{E}')
            self.result_ready.emit('未知', '未知', str(E))
        finally:
            self.result_ready.emit(user, origin, error)

class MainWorker(QThread):

    run_ready = Signal(str)

    def __init__(self, dic, ini_path, template_excel) -> None:
        super().__init__()
        self.dic = dic
        self.ini_path = ini_path
        self.template_excel = template_excel
    
    def read_excel(self, path, col_tag="A", part=None, sheet=None):
        B = Base_Class(self.ini_path, self.template_excel)
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
                    jb = RL(self.ini_path, self.template_excel)
                    jb.main(lis)
                if self.dic.get('tz_status'):
                    tz = JB(self.ini_path, self.template_excel)
                    tz.main(lis)
                if self.dic.get('cb_status'):
                    cb = JC_Query(self.ini_path, self.template_excel)
                    cb.main(lis)
            except Exception as E:
                self.run_ready.emit(E)
            else:
                self.run_ready.emit('导出完成')


class SearchWorker(QThread):

    search_result = Signal(dict)

    def __init__(self, idcard, ini_path, template_excel) -> None:
        super().__init__()
        self.idcard = idcard
        self.ini_path = ini_path
        self.template_excel = template_excel

    def run(self):
        cb = JC_Query(self.ini_path, self.template_excel)
        dic = cb.search(self.idcard)
        data = dic.get(self.idcard)
        self.search_result.emit(data)

class VPNWorker(QThread):
    
    vpn_result = Signal(int)

    def __init__(self, path) -> None:
        super().__init__()
        self.path = path

    def run(self):
        res = subprocess.Popen(self.path, shell=True)
        res.wait()
        self.vpn_result.emit(res.returncode)