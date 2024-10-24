# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

import sys
import os
import platform

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
from myfunction import *
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.my_thread = None
        abs_path = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__))))
        self.ini_path = os.path.abspath(os.path.join(abs_path, 'config.ini'))
        self.template_excel = os.path.abspath(os.path.join(abs_path, 'template_excel'))
        self.Login = Login(self.ini_path)
        self.set_page()
        self.set_column_widths()
        # self.useCustomTheme = None
        # self.abspath = None

        global widgets
        widgets = self.ui

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "Jinbao Downloader Speed Edition"
        description = "金保下载器极速版"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS 表格的列宽自动调整以填满可用空间
        # ///////////////////////////////////////////////////////////////
        # widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_login.clicked.connect(self.buttonClick)
        widgets.btn_search.clicked.connect(self.buttonClick)
        widgets.btn_batch.clicked.connect(self.buttonClick)
        widgets.btn_set.clicked.connect(self.buttonClick)
        widgets.btn_background.clicked.connect(self.buttonClick)
        # login_page
        widgets.pb_login_login.clicked.connect(self.buttonClick)
        widgets.pb_rc_login.clicked.connect(self.buttonClick)
        widgets.pb_vpn_login.clicked.connect(self.buttonClick)
        # search_page
        widgets.pushButton.clicked.connect(self.buttonClick)
        # batch_page
        widgets.pb_select_batch.clicked.connect(self.buttonClick)
        widgets.pb_run_batch.clicked.connect(self.buttonClick)
        # set_page
        widgets.pb_submit_set.clicked.connect(self.buttonClick)
        widgets.pb_choose_set.clicked.connect(self.buttonClick)
        widgets.pb_choose_set_2.clicked.connect(self.buttonClick)
        widgets.pb_edit_set.clicked.connect(self.buttonClick)
        widgets.pb_edit_set2.clicked.connect(self.buttonClick)

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        if getattr(sys, 'frozen', False):
            absPath = os.path.dirname(os.path.abspath(sys.executable))
        elif __file__:
            absPath = os.path.dirname(os.path.abspath(__file__))
        useCustomTheme = False
        self.useCustomTheme = useCustomTheme
        self.abspath = absPath
        themeFile = os.path.abspath(os.path.join(absPath, "themes\py_dracula_light.qss"))

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))


    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btnName == "btn_login":
            widgets.stackedWidget.setCurrentWidget(widgets.login)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW NEW PAGE
        if btnName == "btn_search":
            widgets.stackedWidget.setCurrentWidget(widgets.search) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        if btnName == "btn_batch":
            widgets.stackedWidget.setCurrentWidget(widgets.batch) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU
        
        if btnName == "btn_set":
            widgets.stackedWidget.setCurrentWidget(widgets.set) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU
        
        # 自定义按钮功能
        # /////////////
        if btnName == "btn_background":         
            # SET THEME AND HACKS
            if self.useCustomTheme:
                themeFile = os.path.abspath(os.path.join(self.abspath, "themes\py_dracula_dark.qss"))
                # LOAD AND APPLY STYLE
                UIFunctions.theme(self, themeFile, True)

                # SET HACKS
                AppFunctions.setThemeHack(self)
                self.useCustomTheme = False
            else:
                themeFile = os.path.abspath(os.path.join(self.abspath, "themes\py_dracula_light.qss"))
                # LOAD AND APPLY STYLE
                UIFunctions.theme(self, themeFile, True)

                # SET HACKS
                AppFunctions.setThemeHack(self)
                self.useCustomTheme = True

        if btnName == "pb_rc_login":
            user, idcard = self.Login.read_ini()
            self.ui.le_idcard_login.setText(idcard)
            self.ui.le_name_login.setText(user)

        if btnName == "pb_login_login":
            self.ui.pb_login_login.setEnabled(False)
            self.my_thread = LoginWorker(name=self.ui.le_name_login.text(), idcard=self.ui.le_idcard_login.text(), Login=self.Login)
            self.my_thread.result_ready.connect(self.update_le)
            self.my_thread.start()
        
        if btnName == "pb_vpn_login":
            self.ui.pb_vpn_login.setEnabled(False)
            path = self.ui.le_path_set_2.text()
            self.vpn_thread = VPNWorker(path)
            self.vpn_thread.vpn_result.connect(self.vpn_res)
            self.vpn_thread.start()
        
        if btnName == "pushButton":
            idcard = self.ui.lineEdit.text()
            self.search_thread = SearchWorker(idcard, self.ini_path, self.template_excel)
            self.search_thread.search_result.connect(self.table_update)
            self.search_thread.start()

        if btnName == "pb_select_batch":
            options = QFileDialog.Options()
            file_path, _ = QFileDialog.getOpenFileName(self, "选择 XLSX 文件", "", "Excel Files (*.xlsx);;All Files (*)", options=options)

            # 如果用户选择了文件，则更新标签显示文件路径
            if file_path:
                print(file_path)
                self.ui.le_input_batch.setText(file_path)

        if btnName == "pb_run_batch":
            dic = {
                "path": self.ui.le_input_batch.text(),
                "sheet": self.ui.le_sheet_batch.text(),
                "col": self.ui.le_colum_batch.text(),
                "start_row": self.ui.le_startrow_batch.text(),
                "end_row": self.ui.le_endrow_batch.text(),
                "jb_status": self.ui.cb_jbbx.isChecked(),
                "tz_status": self.ui.cb_jbtz.isChecked(),
                "cb_status": self.ui.cb_jbinfo.isChecked()
            }
            text = f"""
            文件位置: {dic.get('path')}
            表名: {dic.get('sheet')}
            身份证号所在列: {dic.get('col')}
            起始行: {dic.get('start_row')}
            结束行: {dic.get('end_row')}
            """
            self.ui.tb_batch.setPlainText(text)
            self.work = JQWorker(dic, self.ini_path, self.template_excel)
            self.work.run_ready.connect(self.run_result)
            self.work.start()
        
        if btnName == "pb_submit_set":
            self.Login.set_ini("Info", {"username": self.ui.le_name_set.text(), "password": self.ui.le_idcard_set.text()})
            self.ui.le_idcard_set.setReadOnly(True)
            self.ui.le_name_set.setReadOnly(True)
        
        if btnName == "pb_choose_set":
            folder_path = QFileDialog.getExistingDirectory(self, "选择文件夹", "")
            if folder_path:
                self.Login.set_ini("Path", {"download": folder_path})
                self.ui.le_path_set.setText(folder_path)
        
        if btnName == "pb_choose_set_2":
            options = QFileDialog.Options()
            # 打开文件选择对话框，过滤器只显示 .exe 文件
            file_path, _ = QFileDialog.getOpenFileName(self, "选择 EXE 文件", "", "Executable Files (*.exe);;All Files (*)", options=options)
            
            if file_path:
                self.Login.set_ini("Path", {"exe": file_path})
                self.ui.le_path_set_2.setText(file_path)
        
        if btnName == "pb_submit_set2":
            self.Login.set_ini("Host", {"host": self.ui.le_jb_set.text(), "jb_host": self.ui.le_JB_set.text()})
            self.ui.le_idcard_set.setReadOnly(True)
            self.ui.le_name_set.setReadOnly(True)

        if btnName == "pb_edit_set":
            self.ui.le_idcard_set.setReadOnly(False)
            self.ui.le_name_set.setReadOnly(False)
        
        if btnName == "pb_edit_set2":
            self.ui.le_jb_set.setReadOnly(False)
            self.ui.le_JB_set.setReadOnly(False)


        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')

    def update_le(self, user, origin, error):
        self.ui.pb_login_login.setEnabled(True)
        if error=='None':
            self.ui.le_user_login.setText(user)
            self.ui.le_origin_login.setText(origin)  
        else:
            messbox = QMessageBox()
            messbox.setWindowTitle("登录错误")
            messbox.setText(error)
            messbox.exec()
    
    def vpn_res(self, result):
        print(result)
        self.ui.pb_vpn_login.setEnabled(True)
    
    def table_update(self, dic):
        table_dic = {
            "ryjb_info": self.ui.tableWidget,
            "jydj_info": self.ui.tableWidget_3,
            "sydj_info": self.ui.tableWidget_4,
            "jycyz_info": self.ui.tableWidget_5,
            "knrd_info": self.ui.tableWidget_6,
            "zgzs_info": self.ui.tableWidget_7,
        }
        for key, table in table_dic.items():
            lis = dic.get(key)
            # print(lis)
            for r, d in enumerate(lis):
                header = table.horizontalHeader()
                headers = [header.model().headerData(i, Qt.Horizontal) for i in range(table.columnCount())]
                # print(f'{key}--{headers}')
                for i, h in enumerate(headers):
                    text = d.get(h) if d.get(h) else ""
                    # print(f'{text}--{type(text)}')
                    text_item = QTableWidgetItem(str(text))
                    text_item.setTextAlignment(Qt.AlignCenter)
                    table.setItem(r, i, text_item)
            table.resizeColumnsToContents()
            # column_count = self.ui.tableWidget.columnCount()
            # widths = []
            # for i in range(column_count):
            #     width = self.ui.tableWidget.columnWidth(i)
            #     widths.append(width)
            # print("当前每列的宽度:", widths)

    
    def run_result(self, result):
        messbox = QMessageBox()
        messbox.setWindowTitle("导出结果")
        messbox.setText(result)
        messbox.exec()

    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            # print('Mouse click: LEFT CLICK')
            pass
        if event.buttons() == Qt.RightButton:
            # print('Mouse click: RIGHT CLICK')
            pass
    
    def set_page(self):
        res_dic = self.Login.read_all()
        self.ui.le_idcard_set.setText(res_dic.get('idcard'))
        self.ui.le_name_set.setText(res_dic.get('name'))
        self.ui.le_path_set.setText(res_dic.get('path'))
        self.ui.le_jb_set.setText(res_dic.get('host'))
        self.ui.le_JB_set.setText(res_dic.get('jb_host'))
        self.ui.le_path_set_2.setText(res_dic.get('exe'))
    
    def set_column_widths(self):
        for i, v in enumerate([145, 50, 50, 50, 85, 130, 75, 75, 95, 75, 60, 75, 85]):
            self.ui.tableWidget.setColumnWidth(i, v)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec_())
