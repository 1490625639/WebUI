# -*- coding: UTF-8 -*-
"""
Project ：web_test 
File    ：alert_handle.py
Author  ：张以白
Date    ：2024/6/19 21:21 
Desc    :
"""
import time
from time import sleep


from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()


driver.get("https://www.leafground.com/alert.xhtml")

driver.find_element(By.ID,'j_idt88:j_idt91').click()
# 警告框处理
alert=driver.switch_to.alert
alert.accept() #确认

# 有确定跟取消按钮
driver.find_element(By.XPATH,'//*[@id="j_idt88:j_idt93"]/span[2]').click()
alert=driver.switch_to.alert
time.sleep(1)
alert.dismiss()
time.sleep(1)
# 自定义弹窗处理方式

driver.find_element(By.XPATH,'//*[@id="j_idt88:j_idt95"]/span[2]').click()
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="j_idt88:j_idt98"]/span[2]').click()# 如果是内嵌的，需要切换一下frame


# 模态框处理
driver.find_element(By.XPATH,'//*[@id="j_idt88:j_idt100"]/span[2]').click()
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="j_idt88:j_idt101"]/div[1]/a/span').click()
time.sleep(1)