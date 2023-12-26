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
check_dependencies("os", "requests", "re", "time", "glob", "subprocess")
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