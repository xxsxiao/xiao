#!/usr/bin/python3
# -------------------------------
# cron "0 0 0 * * *" script-path=xxx.py,tag=匹配cron用
# const $ = new Env('流量杀手')
'''
by：神也眷顾小晓吖
修复保活规则，利用系统wget进行下载

'''
import requests
import os
import time
import glob
import re
import subprocess
import shutil
print("流量杀手-启动")
print("正在检查安装依赖")
def check_dependencies(*dependencies):
    for dependency in dependencies:
        try:
            __import__(dependency)
            print(f"{dependency} 依赖已安装")
        except ModuleNotFoundError:
            print(f"{dependency} 依赖未安装-请去依赖管理-python进行安装")

# 检查多个依赖
check_dependencies("os", "requests", "re", "time", "glob", "subprocess", "shutil")
print("开始删除旧文件日志 ┄ ┄ ┄ 如果没有日志或者任务未运行请手动重新再运行")
time.sleep(3)
from datetime import datetime

# 定义要遍历的目录路径
directory = '/ql/data/log/'

# 指定要匹配的文件夹名称模式
folder_pattern = r'.*刷流量.*'

# 获取当前时间
current_time = datetime.now()

for root, dirs, files in os.walk(directory):
    for dir_name in dirs:
        if re.match(folder_pattern, dir_name):
            dir_path = os.path.join(root, dir_name)
            file_list = os.listdir(dir_path)
            if file_list:  # 检查文件列表是否为空
                first_file = file_list[0]  # 获取文件夹中的第一个文件
                first_file_path = os.path.join(dir_path, first_file)
                if os.path.isfile(first_file_path):
                    print("要删除旧日志文件路径:", first_file_path)
                    print("要删除旧日志文件名称:", first_file)
                    os.remove(first_file_path)  # 删除文件
print("┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄")
url = 'http://myip.ipip.net/'
response = requests.get(url)
print(f"国内IP地址：{response.text}")
url = 'https://ipinfo.io/json'
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    ip = data['ip']
    country = data['country']
    city = data['city']
    
    print(f"国外IP地址：IP 地址: {ip},国家: {country},城市: {city}")
else:
    print(f"获取数据失败: {response.status_code}")
print("┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄")
url = 'https://issuecdn.baidupcs.com/issue/netdisk/apk/BaiduNetdiskSetup_wap_share.apk'  # 你的文件URL
download_count = 0

def download_file(url):
    global download_count
    while True:
        download_count += 1
        print(f"开始下载: {url}")
        process = subprocess.Popen(['wget', url, '--progress=bar:force', '-O', '/dev/null'], stderr=subprocess.PIPE, universal_newlines=True)
        
        print(f"进程PID: {process.pid}")
        t = time.localtime(time.time())
        localtime = time.asctime(t)
        print(f"当前时间: {localtime}")
        print(f"下载次数: {download_count}")
        print("┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄")

        while True:
            output = process.stderr.readline()
            if process.poll() is not None and not output:
                break
            if output:
                print(output, end='', flush=True)
            time.sleep(0.1)

        print(f"下载完成。等待5秒后重新开始下载...\n┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄")
        time.sleep(5)
download_file(url)
