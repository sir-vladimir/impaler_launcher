import os, sys, time, subprocess, requests, string, json, shutil, threading, platform
import launcher_lib
from uuid import uuid4
from typing import List, Dict, Tuple, Union
from ui.ui_main import Ui_MainWindow as ui_main_window
from ui.ui_dialog_new import Ui_dialog_new as ui_dialog_new
from ui.ui_dialog_account import Ui_dialog_account as ui_dialog_account
from ui.ui_dialog_configure import Ui_dialog_configure as ui_dialog_configure
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog, QScrollBar, QTextBrowser, QProgressDialog, QLineEdit
from PySide2.QtGui import QIcon, QCloseEvent
from PySide2.QtCore import QThread, QMutex, Signal, QStringListModel

allow_characters : str = string.ascii_letters + string.digits + ' .()'

class ConsoleThread(QThread): # CONSOLE THREAD
    append = Signal(str)
    move_scrollbar = Signal()
    def __init__(self, other:ui_main_window, process:subprocess.Popen) -> None:
        super(ConsoleThread, self).__init__()
        self.thread_lock : QMutex = QMutex()
        self.arg_other : MainWindow = other
        self.arg_process : Union[subprocess.Popen, None] = process

    def run(self) -> None:
        output : str = ''
        while not isinstance(self.arg_process.poll(), int):
            output = self.arg_process.stdout.readline()
            if output:
                self.append.emit(output)
        time.sleep(0.10)
        error : list = self.arg_process.stderr.readlines()
        if error:
            self.append.emit('\n'.join(error))
        self.arg_other.set_running(False)
        time.sleep(0.10)
        self.append.disconnect()
        self.move_scrollbar.disconnect()
        self.arg_other = None

    def lock(self) -> None:
        self.thread_lock.lock()

    def unlock(self) -> None:
        self.thread_lock.unlock()

class MainWindow(QMainWindow, ui_main_window): # MAIN WINDOW
    def __init__(self, parent=None) -> None:
        super(MainWindow, self).__init__(parent=parent)
        
        self.setupUi(self)
        self.action_new.triggered.connect(self.show_dialog_new)
        self.action_info.triggered.connect(lambda: self.create_message('Info', f'{launcher_lib.launcher_name} Launcher\nVersion {launcher_lib.launcher_version}\nSir Vladimir Productions'))
        self.action_login.triggered.connect(self.show_dialog_account)
        self.action_logout.triggered.connect(self.remove_account)
        self.set_buttons_enabled(False)
        self.list_instances.clicked.connect(self.instance_selected)
        self.button_launch.clicked.connect(self.run_instance)
        self.button_remove.clicked.connect(self.remove_instance)
        self.button_configure.clicked.connect(self.show_dialog_configure)
        self.refresh_instances()
        self.selected_instance : str = ''
        self.is_installing : bool = False
        self.scrollbar : QScrollBar = self.text_browser_log.verticalScrollBar()
        self.console_thread : Union[ConsoleThread, None] = None
        self.install_thread : Union[threading.Thread, None] = None
        self.process : Union[subprocess.Popen, None] = None
        self.launcher_data : launcher_lib.LauncherData = {
            'username' : '',
            'password' : '',
            'client_token' : '',
            'offline' : False
        }
        launcher_lib.make_dirs()
        if os.path.isfile(launcher_lib.launcher_json_path):
            try:
                with open(launcher_lib.launcher_json_path, 'r') as json_file:
                    self.launcher_data = json.load(json_file)
            except json.decoder.JSONDecodeError:
                self.create_data_json()
        else:
            self.create_data_json()
    
    def set_running(self, is_running:bool) -> None:
        self.button_configure.setDisabled(is_running)
        self.button_remove.setDisabled(is_running)
        if is_running:
            self.button_launch.setText('Stop')
            return
        self.button_launch.setText('Launch')

    def remove_account(self) -> None:
        with open(launcher_lib.launcher_json_path, 'w') as json_file:
            self.launcher_data['username'] = ''
            self.launcher_data['password'] = ''
            self.launcher_data = json.dump(json_file)

    def remove_instance(self) -> None:
        if not self.selected_instance:
            return
        confirmation : QMessageBox.StandardButton = QMessageBox.question(None, 'Remove Instance', 'Delete instance ' + self.selected_instance + ' ?', QMessageBox.Apply | QMessageBox.Cancel, QMessageBox.Cancel)
        if confirmation == QMessageBox.Apply:
            instance_root_path : str = os.path.join(launcher_lib.launcher_instance_path, self.selected_instance)
            shutil.rmtree(instance_root_path, True)
            self.refresh_instances()
            self.set_buttons_enabled(False)

    def create_data_json(self) -> None:
        with open(launcher_lib.launcher_json_path, 'w') as json_file:
            self.launcher_data['client_token'] = str(uuid4())
            json.dump(self.launcher_data, json_file)

    def run_instance(self) -> None:
        if self.process and self.button_launch.text() == 'Stop':
            self.process.kill()
            return
        if not self.selected_instance:
            self.create_message('No Instance Selected', 'Select an instance to launch.')
            return
        info : Tuple[str, str] = (uuid4().hex, '')
        if not self.launcher_data['offline']:
            if not ( self.launcher_data['username'] and self.launcher_data['password'] ):
                self.create_message('No User', 'Login in an account or use offline mode to launch.')
                return
            info = launcher_lib.ely_by_auth(self.launcher_data['username'], self.launcher_data['password'], self.launcher_data['client_token'])
            if not info:
                self.create_message('Login Failed', 'Credencials are incorrect.')
                return
        uuid, access_token = info
        instance_root_path : str = os.path.join(launcher_lib.launcher_instance_path, self.selected_instance)
        instance_json_path : str = os.path.join(instance_root_path, launcher_lib.launcher_json_instances_file)
        if not os.path.isfile(instance_json_path):
            self.create_message('Invalid Instance', 'Instance JSON is missing.')
            return
        with open(instance_json_path, 'r') as json_file:
            data : launcher_lib.InstanceInfo = json.load(json_file)
            version : str = data['version']
            java_path : str = data['java_path']
            jvm_args : list = data['jvm_args']
        self.text_browser_log.setText('')
        command : List[str] = launcher_lib.get_mc_launch_command(
            version,
            launcher_lib.launcher_mc_path,
            instance_root_path,
            self.launcher_data['username'],
            uuid,
            access_token,
            java_path,
            jvm_args
        )
        self.set_running(True)
        self.process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        self.console_thread = ConsoleThread(self, self.process)
        self.console_thread.append.connect(self.append_console)
        self.console_thread.move_scrollbar.connect(self.scroll_signal)
        self.console_thread.start()
        
    def scroll_signal(self) -> None:
        lines : int = (self.text_browser_log.height() // self.text_browser_log.fontMetrics().height()) * 15
        if self.scrollbar.value() >= self.scrollbar.maximum() - lines:
            self.scrollbar.setValue(self.scrollbar.maximum())
    
    def append_console(self, text:str) -> None:
        self.text_browser_log.append(text)

    def instance_selected(self, index) -> None:
        self.selected_instance = index.data()
        self.set_buttons_enabled(True)

    def set_buttons_enabled(self, enable:bool) -> None:
        self.button_launch.setEnabled(enable)
        self.button_configure.setEnabled(enable)
        self.button_remove.setEnabled(enable)

    def refresh_instances(self) -> None:
        instances_folders : List[str] = os.listdir(launcher_lib.launcher_instance_path)
        item_list : List[str] = []
        for folder in instances_folders:
            path : str = os.path.join(launcher_lib.launcher_instance_path, folder, launcher_lib.launcher_json_instances_file)
            if os.path.isfile(path):
                item_list.append(folder)
        model : QStringListModel = QStringListModel()
        model.setStringList(item_list)
        self.list_instances.setModel(model)

    def show_dialog_configure(self) -> None:
        if not self.selected_instance:
            self.create_message('No Instance Selected', 'Select an instance to configure.')
            return
        window : QDialog = QDialog()
        dialog : ui_dialog_configure = ui_dialog_configure()
        dialog.setupUi(window)
        instance_data : launcher_lib.InstanceInfo = {}
        instance_root_path : str = os.path.join(launcher_lib.launcher_instance_path, self.selected_instance)
        instance_json_path : str = os.path.join(instance_root_path, launcher_lib.launcher_json_instances_file)
        with open(instance_json_path, 'r') as json_file:
            instance_data = json.load(json_file)
        dialog.text_name.setText(self.selected_instance)
        dialog.text_jvm.setText(' '.join(instance_data['jvm_args']))
        dialog.text_java.setText(instance_data['java_path'])
        dialog.label_version.setText(instance_data['version'])
        dialog.button_cancel.clicked.connect(window.close)
        dialog.button_accept.clicked.connect(lambda: self.dialog_configure_confirm(self.selected_instance, instance_root_path, dialog, window))
        dialog.button_open_folder.clicked.connect(lambda: self.open_folder(instance_root_path))
        window.exec_()

    def dialog_configure_confirm(self, instance_name_old:str, instance_root_path:str, dialog:ui_dialog_configure, window:QDialog) -> None:
        instance_name : str = dialog.text_name.text().strip()
        java_path : str = dialog.text_java.text().strip()
        jvm_arguments : list = dialog.text_jvm.text().strip().split()
        instance_json_path : str = os.path.join(instance_root_path, launcher_lib.launcher_json_instances_file)
        old_data : launcher_lib.InstanceInfo = {}
        with open(instance_json_path, 'r') as json_file:
            old_data = json.load(json_file)
        if not instance_name:
            self.create_message('Invalid Entry', 'Fill instance name entry.')
            return
        for char in instance_name:
            if not char in allow_characters:
                self.create_message('Invalid Name', 'Invalid characters in instance name entry.\nUse only ascii letters, digits, dots, spaces, and parenthesis.')
                return
        if instance_name != instance_name_old:
            if instance_name in os.listdir(launcher_lib.launcher_instance_path):
                self.create_message('Already Exists', 'Please select an unused instance name.')
                return
        if not java_path:
            java_path = launcher_lib.get_default_java_exec()
        if not os.path.isfile(java_path):
            self.create_message('Invalid Java Path', 'Either invalid Java path or not installed.')
            return
        with open(instance_json_path, 'w') as json_file:
            old_data['name'] = instance_name
            old_data['java_path'] = java_path
            old_data['jvm_args'] = jvm_arguments
            json.dump(old_data, json_file)
        if instance_name != instance_name_old:
            new_path : str = os.path.join(launcher_lib.launcher_instance_path, instance_name)
            try:
                os.rename(instance_root_path, new_path)
            except PermissionError:
                self.create_message('Permission Error', 'Could not rename instance directory.')
        window.close()
        self.refresh_instances()

    def open_folder(self, path:str) -> None:
        system : str = platform.system()
        match system:
            case 'Windows':
                os.startfile(path)
            case 'Darwin':
                subprocess.Popen(['open', path])
            case 'Linux':
                subprocess.Popen(['xdg-open', path])
            case _:
                self.create_message('Could Not Open Folder', 'There was an issue selecting platform open folder method.')

    def show_dialog_account(self) -> None:
        window : QDialog = QDialog()
        dialog : ui_dialog_account = ui_dialog_account()
        dialog.setupUi(window)
        dialog.text_password.setEchoMode(QLineEdit.Password)
        dialog.check_offline.setChecked(self.launcher_data['offline'])
        if self.launcher_data['username'] and self.launcher_data['password']:
            dialog.label_info.setText('Logged in as ' + self.launcher_data['username'])
        dialog.button_cancel.clicked.connect(window.close)
        dialog.button_accept.clicked.connect(lambda: self.dialog_account_confirm(dialog, window))
        window.exec_()

    def dialog_account_confirm(self, dialog:ui_dialog_account, window:QDialog) -> None:
        username : str = dialog.text_user.text().strip()
        offline_mode : bool = dialog.check_offline.isChecked()
        if offline_mode:
            if not username:
                self.create_message('No Username', 'Enter a valid username.')
                return
            with open(launcher_lib.launcher_json_path, 'w') as json_file:
                self.launcher_data['username'] = username
                self.launcher_data['offline'] = True
                json.dump(self.launcher_data, json_file)
        else:
            if not username:
                self.create_message('No Username', 'Enter a valid username.')
                return
            password : str = dialog.text_password.text()
            info : tuple = launcher_lib.ely_by_auth(username, password, self.launcher_data['client_token'])
            if not info:
                self.create_message('Login Failed', 'Credencials are incorrect.')
                return
            with open(launcher_lib.launcher_json_path, 'w') as json_file:
                self.launcher_data['username'] = username
                self.launcher_data['password'] = password
                self.launcher_data['offline'] = False
                json.dump(self.launcher_data, json_file)
        window.close()

    def show_dialog_new(self) -> None:
        if self.is_installing:
            self.create_message('Ongoing Install', 'An installation is active.')
            return
        window : QDialog = QDialog()
        dialog : ui_dialog_new = ui_dialog_new()
        dialog.setupUi(window)
        dialog.check_fabric.setEnabled(False)
        try:
            dialog.box_version.addItems([version['id'] for version in launcher_lib.mc_lib.utils.get_version_list() if version['type'] == 'release'])
        except requests.exceptions.ConnectionError:
            self.create_message('No Connection', 'Fetching version list failed.')
            return
        dialog.box_version.currentTextChanged.connect(lambda x: self.box_version_changed(dialog, x))
        dialog.button_cancel.clicked.connect(window.close)
        dialog.button_accept.clicked.connect(lambda: self.dialog_new_confirm(dialog, window))
        window.exec_()

    def box_version_changed(self, dialog:ui_dialog_new, text:str) -> None:
        if launcher_lib.mc_lib.fabric.is_minecraft_version_supported(text):
            dialog.check_fabric.setEnabled(True)
            return
        dialog.check_fabric.setChecked(False)
        dialog.check_fabric.setEnabled(False)

    def dialog_new_confirm(self, dialog:ui_dialog_new, window:QDialog) -> None:
        if self.is_installing:
            self.create_message('Ongoing Install', 'An installation is active.')
            return
        instance_name : str = dialog.text_name.text().strip()
        instance_version : str = dialog.box_version.currentText()
        is_fabric_version : bool = dialog.check_fabric.isChecked()
        java_path : str = dialog.text_java.text().strip()
        jvm_arguments : list = dialog.text_jvm.text().strip().split()
        if not instance_name:
            self.create_message('Invalid Entry', 'Fill instance name entry.')
            return
        for char in instance_name:
            if not char in allow_characters:
                self.create_message('Invalid Name', 'Invalid characters in instance name entry.\nUse only ascii letters, digits, dots, spaces, and parenthesis.')
                return
        if instance_name in os.listdir(launcher_lib.launcher_instance_path):
            self.create_message('Already Exists', 'Please select an unused instance name.')
            return
        if not instance_version:
            self.create_message('Invalid Version', 'Please select a version.')
            return
        if is_fabric_version:
            if not launcher_lib.mc_lib.fabric.is_minecraft_version_supported(instance_version):
                self.create_message('Incompatible Version', 'Please select a version compatible with Fabric loader.\nOtherwise uncheck use Fabric.')
                return
        if not java_path:
            java_path = launcher_lib.get_default_java_exec()
        if not os.path.isfile(java_path):
            self.create_message('Invalid Java Path', 'Either invalid Java path or not installed.')
            return
        window.close()
        self.is_installing = True
        self.install_thread = threading.Thread(None, lambda: self.install_on_thread(instance_name, instance_version, java_path, jvm_arguments, is_fabric_version))
        self.install_thread.daemon = True
        self.install_thread.start()

    def install_on_thread(self, instance_name:str, instance_version:str, java_path:str, jvm_arguments:List[str], is_fabric_version:bool) -> None:
        progress_dialog : QProgressDialog = QProgressDialog('Wait...', None, 0, 0, self)
        progress_dialog.setWindowTitle('Installing Minecraft')
        progress_dialog.setAutoClose(False)
        callback : launcher_lib.mc_lib.types.CallbackDict = {
            'setProgress' : progress_dialog.setValue,
            'setMax' : progress_dialog.setMaximum,
            'setStatus' : progress_dialog.setLabelText
        }
        install_result : Tuple[bool, str, str] = launcher_lib.create_instance(instance_name, instance_version, java_path, jvm_arguments, callback, is_fabric_version)
        progress_dialog.close()
        self.is_installing = False
        if install_result[0]:
            text : str = 'Minecraft Version ' + install_result[2] + ' Has been successfully installed.'
            self.create_message(install_result[1], text)
            self.refresh_instances()
            return
        self.create_message(install_result[1], install_result[2])

    def create_message(self, title:str, information:str) -> None:
        message_box = QMessageBox()
        message_box.setWindowTitle(title)
        message_box.setText(information)
        message_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        message_box.exec_()

if __name__ == '__main__':
    print(launcher_lib.launcher_name, 'Launcher', launcher_lib.launcher_version)
    if '--print-dir' in sys.argv:
        print('CWD:', launcher_lib.executable_dir)
        print('PYTHON FILE:', launcher_lib.file_dir)
        print('EXECUTABLE:', launcher_lib.frozen_dir)
    app : QApplication = QApplication([])
    icon_path : str = os.path.join(launcher_lib.executable_dir, 'icon.svg')
    icon : QIcon = QIcon(icon_path)
    app.setWindowIcon(icon)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())