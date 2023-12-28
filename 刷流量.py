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
增加推送通知！
'''
import requests
import os
import time
import re
import subprocess
import sys

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
check_dependencies("os", "requests", "re", "subprocess", "sys")
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
#推送
def load_send_notification():
    cur_path = os.path.abspath(os.path.dirname(__file__))
    sendNotifyPath = os.path.join(cur_path, "notify.py")
    try:
        from notify import send
        return send
    except ImportError:
        print("加载通知服务失败！")
        return None

# 修改get_local_ip()函数
def get_local_ip():
    try:
        url = 'http://myip.ipip.net/'
        response = requests.get(url)
        if response.ok:
            return response.text
        else:
            return "无法获取本地IP"
    except requests.exceptions.RequestException as e:
        return f"获取数据失败: {e}"

# 修改get_foreign_ip()函数
def get_foreign_ip():
    url = 'https://ipinfo.io/json'
    try:
        response = requests.get(url)
        response.raise_for_status()  # 检查请求是否成功
        if response.text:  # 校验响应内容是否为空
            data = response.json()
            ip = data.get('ip', 'N/A')
            country = data.get('country', 'N/A')
            city = data.get('city', 'N/A')
            return f"国外IP地址：IP 地址: {ip},国家: {country},城市: {city}"
        else:
            return "无法获取本地IP"
    except requests.exceptions.RequestException as e:
        return f"获取数据失败: {e}"

# 获取本地IP地址
domestic_ip = get_local_ip()

# 获取国外IP地址
foreign_ip = get_foreign_ip()

# 加载通知服务并发送通知
send_notification = load_send_notification()
if send_notification:
    send_notification("流量杀手-本地青龙通知", f"流量杀手已启动……\n国内IP地址：{domestic_ip}\n{foreign_ip}\n┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄")
else:
    print('通知服务加载失败，请重试！')
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
        os.system("pkill wget")
        if i < 200:
            print("等待5秒后重新开始下载...\n┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄ ┄")
            time.sleep(5)

download_file(url)
