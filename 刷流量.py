#!/usr/bin/python3
# -------------------------------
# cron "0 0 6-23/1 * * *" script-path=xxx.py,tag=匹配cron用
#6点到23点每1小时循环200次
# const $ = new Env('流量杀手')
'''
by：神也眷顾小晓吖
修复保活规则，利用系统wget进行下载
12/28
修复卡死线程问题
'''
import requests
import os
import time
import glob
import re
import subprocess
import shutil
import select

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
print("请手动删除旧文件日志\n没有日志就多重新开启几次")
time.sleep(5)
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
                    print("要删除旧日志文件名称(可能有很多个日志):", first_file)
                   # os.remove(first_file_path)  # 删除文件
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
url = 'https://issuecdn.baidupcs.com/issue/netdisk/apk/BaiduNetdiskSetup_wap_share.apk'

def download_file(url):
    for i in range(1, 201):
        print(f"开始下载: {url}")
        process = subprocess.Popen(['wget', url, '-O', '/dev/null', '-q', '--show-progress'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        print(f"进程PID: {process.pid}")
        localtime = time.asctime(time.localtime(time.time()))
        print(f"当前时间: {localtime}")
        print("┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄")

        while True:
            output = process.stderr.readline()
            if output == b'' and process.poll() is not None:
                break
            if output:
                print(output.strip().decode('utf-8'))

        process.communicate()
        
        print(f"第 {i} 次下载完成")
        if i < 200:
            print("等待5秒后重新开始下载...\n┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄")
            time.sleep(5)

download_file(url)
