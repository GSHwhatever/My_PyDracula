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

class JQWorker(QThread):

    run_ready = Signal(str)

    def __init__(self, dic, ini_path, template_excel) -> None:
        super().__init__()
        self.dic = dic
        self.ini_path = ini_path
        self.template_excel = template_excel
        self.jq = RL(ini_path, template_excel)
    
    async def do(self, ids):
        monitor = asyncio.create_task(self.monitor_tasks())
        await self.jq.init_session()
        await self.jq.run_first(ids)
        # ic(self.result_dic)
        await self.jq.close_session()
        monitor.cancel()
        try:
            await monitor
        except asyncio.CancelledError:
            pass
    
    async def monitor_tasks(self):
        while True:
            # 获取当前事件循环中的所有任务
            tasks = asyncio.all_tasks()
            print(f'Current number of running tasks: {len(tasks)}')
            await asyncio.sleep(1)  # 每秒检查一次
    
    def read_excel(self, path, col_tag="A", part=None, sheet=None):
        B = Base_Class(self.ini_path, self.template_excel)
        lis = B.read_file(path, col_tag, part, sheet)
        if isinstance(lis, str):
            raise lis
        elif isinstance(lis, list):
            return lis
        
    def run(self):
        try:
            ids = self.read_excel(path=self.dic.get('path'), col_tag=self.dic.get('col'), part=f"{self.dic.get('start_row')},{self.dic.get('end_row')}", sheet=self.dic.get('sheet'))
        except Exception as E:
            self.run_ready.emit(E)
        else:
            if os.path.exists(self.jq.out_path):
                asyncio.run(self.do(ids))
                _ = [self.jq.save_result(self.jq.result_dic.get(id)) for id in ids]
                self.jq.Reset.reset(self.jq.ws)
                self.jq.Reset.reset(self.jq.ws_first)
                self.jq.wb.save(os.path.join(self.jq.out_path, f'个人信息查询结果{time.strftime("%Y-%m-%d")}.xlsx'))
            else:
                print(f'检查输出路径:{self.jq.out_path}')


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