from PySide6.QtCore import QObject, QThread, Signal
from concurrent.futures import ThreadPoolExecutor as Pool
from myfunction import *
from datetime import datetime
import subprocess, time, re


class LoginWorker(QThread):

    result_ready = Signal(str, str, str)

    def __init__(self, name, idcard, Login) -> None:
        super().__init__()
        self.L = Login
        self.name = name
        self.idcard = idcard

    def run(self):
        # 金保登录，返回机构和用户信息
        try:
            user, origin, error = self.L.main(name=self.name, idcard=self.idcard)
        except Exception as E:
            print(f'login_error:{E}')
            self.result_ready.emit('未知', '未知', str(E))
        finally:
            self.result_ready.emit(user, origin, error)

class SearchWorker(QThread):

    search_result = Signal(dict)
    error_mess = Signal(str)

    def __init__(self, idcard, ini_path, template_excel) -> None:
        super().__init__()
        self.idcard = idcard
        self.ini_path = ini_path
        self.template_excel = template_excel

    def check_id_card(self, id_card):
        # 检查长度
        if len(id_card) not in [15, 18]:
            return False

        # 正则表达式检查格式
        if len(id_card) == 18:
            if not re.match(r'^\d{17}(\d|X)$', id_card):
                return False
        else:  # 15位
            if not re.match(r'^\d{15}$', id_card):
                return False

        # 出生日期检查
        if len(id_card) == 18:
            birth_date = id_card[6:14]
        else:
            # 15位身份证年份需要加上 19 前缀
            birth_date = '19' + id_card[6:12]

        try:
            datetime.strptime(birth_date, '%Y%m%d')
        except ValueError:
            return False

        # 校验位计算（只对18位有效）
        if len(id_card) == 18:
            weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
            check_digits = '10X98765432'
            total = sum(int(id_card[i]) * weight[i] for i in range(17))
            if id_card[17] != check_digits[total % 11]:
                return False

        return True

    def run(self):
        # 金保个人信息查询，返回具体数据
        if self.check_id_card(self.idcard):
            cb = JC_Query(self.ini_path, self.template_excel)
            dic = cb.search(self.idcard)
            data = dic.get(self.idcard)
            self.search_result.emit(data)
        else:
            self.error_mess.emit(f'身份证号:\n{self.idcard}\n不合法,请检查后重试')

class VPNWorker(QThread):
    
    vpn_result = Signal(int)

    def __init__(self, path) -> None:
        super().__init__()
        self.path = path

    def run(self):
        res = subprocess.Popen(self.path, shell=True)
        res.wait()
        self.vpn_result.emit(res.returncode)

class DownloadWorker(QThread):

    get_info = Signal(int)
    run_result = Signal(int)
    run_message = Signal(str)

    def __init__(self, tag, dic, ini_path, template_excel) -> None:
        super().__init__()
        self.tag = tag
        self.loop = asyncio.new_event_loop()
        self.dic = dic
        self.ini_path = ini_path
        self.template_excel = template_excel
        self.file_dic = {
            "sb": "个人信息查询结果",
            "tz": "台账查询结果",
            "gr": "基础信息查询结果"
        }
        func_dic = {
            "sb": RL(ini_path, template_excel),
            "tz": JB(ini_path, template_excel),
            "gr": JC_Query(ini_path, template_excel)
        }
        self.jq = func_dic.get(tag)
    
    def read_excel(self, path, col_tag="A", part=None, sheet=None):
        B = Base_Class(self.ini_path, self.template_excel)
        lis = B.read_file(path, col_tag, part, sheet)
        if isinstance(lis, str):
            raise lis
        elif isinstance(lis, list):
            return lis
    
    async def main_run(self, ids):
        await self.jq.init_session()
        result = await self.jq.run_first(ids)
        if self.tag in ('gr', 'tz'):
            await self.jq.run_end(result)
        await self.jq.close_session()
    
    def main(self, ids):
        self.loop.run_until_complete(self.main_run(ids))
        self.loop.close()
    
    def monitor_tasks(self):
        while True:
            if self.jq.task_num:
                time.sleep(1)
                # 获取当前事件循环中的所有任务
                if self.loop.is_closed():
                    self.run_result.emit(100)
                    break
                else:
                    tasks = len(asyncio.all_tasks(self.loop))
                    print(f'剩余任务数量: {tasks}')
                    num = (self.jq.task_num - tasks) * 100 // self.jq.task_num
                    self.run_result.emit(num)
                    
        
    def run(self):
        if self.tag:
            try:
                ids = self.read_excel(path=self.dic.get('path'), col_tag=self.dic.get('col'), part=f"{self.dic.get('start_row')},{self.dic.get('end_row')}", sheet=self.dic.get('sheet'))
            except Exception as E:
                print(E)
                self.run_message.emit(E)
            else:
                self.get_info.emit(len(ids))
                if os.path.exists(self.jq.out_path):
                    start = time.time()
                    pool = Pool(max_workers=3)
                    pool.submit(self.monitor_tasks)
                    pool.submit(self.main, ids)
                    pool.shutdown(wait=True)
                    if self.tag == 'sb':
                        _ = [self.jq.save_result(self.jq.result_dic.get(id)) for id in ids]
                        self.jq.Reset.reset(self.jq.ws)
                        self.jq.Reset.reset(self.jq.ws_first)
                    elif self.tag == 'tz':
                        _ = [self.jq.save(id) for id in ids]
                        self.jq.reset_format(self.jq.ws, hidden=True)
                        self.jq.reset_format(self.jq.ws_yl)
                    elif self.tag == 'gr':
                        _ = [self.jq.save(id) for id in ids]
                        self.jq.reset_format()
                    self.jq.wb.save(os.path.join(self.jq.out_path, f'{self.file_dic.get(self.tag)}{time.strftime("%Y-%m-%d")}.xlsx'))
                    end = time.time()
                    self.run_message.emit(f'完成\n用时：{int((end - start) // 60)}分{round((end - start) % 60, 2)}秒')
                else:
                    self.run_message.emit(f'检查输出路径:{self.jq.out_path}')

