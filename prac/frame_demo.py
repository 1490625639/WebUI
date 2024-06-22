# -*- coding: UTF-8 -*-
"""
Project ：web_test 
File    ：frame_demo.py
Author  ：张以白
Date    ：2024/6/19 21:08 
Desc    :
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome()
driver.get('https://www.leafground.com/frame.xhtml')
# 切换frame窗口
driver.switch_to.frame(0)
# 定位元素
driver.find_element(By.XPATH,'//*[@id="Click"]').click()
# 返回父窗口
driver.switch_to.default_content()
