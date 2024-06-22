# -*- coding: UTF-8 -*-
"""
Project ：WebUI 
File    ：setting.py
Author  ：张以白
Date    ：2024/6/19 22:28 
Desc    :
"""
import os
import sys



DIR_PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #获取脚本目录
sys.path.append(DIR_PATH)
# 文件路径
FILE_PATH={
    'log': os.path.join(DIR_PATH,'log'),
    'screenshot':os.path.join(DIR_PATH,'screenshot')
}
print(FILE_PATH['log'])
print(FILE_PATH['screenshot'])
# 显示等待默认时间设置
WAIT_TIME=10