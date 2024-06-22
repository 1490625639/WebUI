# -*- coding: UTF-8 -*-
"""
Project ：web_test 
File    ：key.py
Author  ：张以白
Date    ：2024/6/19 1:50 
Desc    :
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys # 文本框

driver = webdriver.Chrome()
# driver.get('https://www.leafground.com/input.xhtml')
#
# text_ele=driver.find_element(By.ID,'j_idt88:j_idt101')
#
# text_ele.send_keys("123456")
# # 模拟键盘回车        模拟鼠标键盘操作,最后都要用perform结尾用来执行
# action1=ActionChains(driver).send_keys(Keys.ENTER).perform()
# time.sleep(1)
# text_ele.send_keys("99999")
#
# #模拟鼠标操作
#     # 右键点击
# action2=ActionChains(driver).context_click(text_ele).perform()
#     # 双击
# ele=driver.find_element(By.ID,'j_idt88:j_idt91')
# action3=ActionChains(driver).double_click(ele).perform()
# time.sleep(1)
# ele.clear()
#     #鼠标悬停
# ele2=driver.find_element(By.XPATH,'/html/body/div[1]/div[5]/div[1]/ul/li[4]/a/i')
# action4=ActionChains(driver).move_to_element(ele2).perform()
#     #鼠标拖拽
# # source=driver.find_element(By.XPATH,'//*[@id="menuform:j_idt41"]/a/i[1]')
# # target=driver.find_element(By.ID,'id="j_idt106:float-input"')
# # action5=ActionChains(driver).drag_and_drop(source=source,target=target).perform()
# time.sleep(1)
# # 6）鼠标滚动
# # 使用JavaScript来执行向下滚动到页面底部
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

# 下拉菜单的鼠标滚动
driver.get('https://www.leafground.com/select.xhtml')
ele3=driver.find_element(By.XPATH,'//*[@id="j_idt87:lang"]/div[3]')
ele3.click()
for _ in range(8):

    ActionChains(driver).send_keys(Keys.DOWN).perform()

