import minecraft_launcher_lib as mc_lib
import os, pathlib, requests, shutil, json, glob, sys
from typing import List, Dict, TypedDict, Tuple, Union, Optional

ely_by_authlib_file : str = 'authlib-injector-1.2.3.jar'
file_dir : str = os.path.dirname(os.path.realpath(__file__))
frozen_dir = os.path.dirname(sys.executable)
executable_dir : str = os.path.dirname(os.path.realpath(__file__))
if getattr(sys, 'frozen', False):
    executable_dir = os.path.dirname(sys.executable)
launcher_name : str = 'Impaler'
launcher_version : str = '0.01'
home_path : str = pathlib.Path.home()
authlib_folder : str = 'authlib'
launcher_folder : str = '.impaler'
launcher_mc_folder : str = 'minecraft'
launcher_instance_folder : str = 'instances'
launcher_json_file : str = 'data.json'
launcher_json_instances_file : str = 'instance_info.json'
launcher_path : str = os.path.join(home_path, launcher_folder)
launcher_mc_path : str = os.path.join(launcher_path, launcher_mc_folder)
launcher_instance_path : str = os.path.join(launcher_path, launcher_instance_folder)
authlib_path : str = os.path.join(executable_dir, authlib_folder)
authlib_jvm_argument : str = '-javaagent:' + os.path.join(authlib_path, ely_by_authlib_file) + '=ely.by'
launcher_json_path : str = os.path.join(launcher_path, launcher_json_file)

class LauncherData(TypedDict):
    username:str
    password:str
    client_token:str
    offline:bool

class InstanceInfo(TypedDict):
    name : str
    version : str
    java_path : str
    jvm_args : list

def create_instance(name:str, version:str, java_path:str, jvm_args:list, callback:mc_lib.types.CallbackDict, is_fabric:bool) -> Tuple[bool, str, str]:
    instance_path : str = os.path.join(launcher_instance_path, name)
    try:
        os.mkdir(instance_path)
    except FileExistsError:
        return (False, 'Already Exists', 'Please check instance directory.')
    install_result : Tuple[bool, str, str] = install_mc(version, launcher_mc_path, java_path, callback, is_fabric)
    if install_result[0]:
        instance_json_path : str = os.path.join(instance_path, launcher_json_instances_file)
        with open(instance_json_path, 'w') as json_file:
            data : InstanceInfo = {
                'name' : name,
                'version' : install_result[2],
                'java_path' : java_path,
                'jvm_args' : jvm_args
            }
            json.dump(data, json_file)
    return install_result
    

def make_dirs() -> None:
    for folder in [launcher_path, launcher_mc_path, launcher_instance_path]:
        try:
            os.mkdir(folder)
        except FileExistsError:
            pass
    os.chdir(launcher_path)

def get_default_java_exec() -> Optional[str]:
    return shutil.which('java')

def get_mc_launch_command(version:str, mc_dir:str, i_dir:str, username:str, uuid:str, token:str, java_path:str, jvm_args:list) -> List[str]:
    options : mc_lib.types.MinecraftOptions = {
        'username' : username,
        'uuid' : uuid,
        'gameDirectory' : i_dir,
        'executablePath' : java_path,
        'jvmArguments' : jvm_args,
        'launcherName' : launcher_name,
        'launcherVersion' : launcher_version
    }
    if token:
        options['token'] = token
    command : List[str] = mc_lib.command.get_minecraft_command(version, mc_dir, options)
    command.insert(1, authlib_jvm_argument)
    return command

def install_mc(version:str, mc_dir:str, java_path:str, callback:mc_lib.types.CallbackDict, is_fabric:bool) -> Tuple[bool, str, str]:
    installed_version : str = version
    if not mc_lib.utils.is_version_valid(version, mc_dir):
        return (False, 'Version Not Found', 'The requested version does not exist.')
    try:
        if is_fabric:
            mc_lib.fabric.install_fabric(version, mc_dir, None, callback, java_path)
            installed_version = 'fabric-loader-' + mc_lib.fabric.get_latest_loader_version() + '-' + version
        else:
            mc_lib.install.install_minecraft_version(version, mc_dir, callback)
    except mc_lib.exceptions.VersionNotFound:
        return (False, 'Version Not Found', 'The requested version does not exist.')
    except mc_lib.exceptions.UnsupportedVersion:
        return (False, 'Version Unsupported By Fabric', 'The requested version does not support Fabric loader.')
    except requests.exceptions.ConnectionError:
            return (False, 'Connection Error', 'There was an error with the connection.')
    return (True, 'Successfully Installed', installed_version)

def ely_by_auth(username:str, password:str, client_token:str) -> tuple:
    request_data : dict = {
        'username' : username,
        'password' : password,
        'clientToken' : client_token,
        'requestUser' : True
    }
    exists_request : requests.Response = requests.get('https://authserver.ely.by/api/users/profiles/minecraft/' + username)
    if exists_request.status_code == 200:
        login_request : requests.Response = requests.post('https://authserver.ely.by/auth/authenticate', request_data)
        if login_request.status_code == 200:
            login_request_response : dict = login_request.json()
            access_token : str = login_request_response['accessToken']
            uid : str = login_request_response['user']['id']
            return (uid, access_token)
    return ()
