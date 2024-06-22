# -*- coding: UTF-8 -*-
"""
Project ：web_test 
File    ：one.py
Author  ：张以白
Date    ：2024/6/19 1:15 
Desc    :
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys # 文本框

driver = webdriver.Chrome()
# driver.get('http://localhost/ecshop/user.php?act=register')

# driver.find_element(By.ID, 'username')
# time.sleep(1)
# driver.find_element(By.NAME, 'email').send_keys('123456@163.com')  # 输入文本函数
# driver.find_element(By.XPATH, '//input[@name="Submit"]')  # 点击函数
# time.sleep(1)
# sel = Select(driver.find_element(By.NAME, 'sel_question'))
# sel.select_by_index(3) # 通过下拉选项的索引去获取
# time.sleep(1)
# sel.select_by_value('favorite_movie') # 通过下拉选项标签的value值定位
# time.sleep(1)
# sel.select_by_visible_text('我最大的爱好？')  # 通过下拉选项的标签的文本内容定位
# time.sleep(1)
#
# sel.deselect_by_index(2)  # 当下拉选项多选的情况下，通过索引取消选择
# time.sleep(1)
# sel.deselect_by_value('favorite_movie')  # 通过标签的value值取消选择
# time.sleep(1)
# sel.deselect_by_visible_text('我最大的爱好？')  # 通过标签文本取消选择
# time.sleep(1)
# sel.deselect_all()  # 取消全部下拉选项
#
# alert=driver.switch_to.alert
# alert.accept()
# alert = driver.switch_to.alert
# time.sleep(3)
# alert.accept()


driver.get('https://www.leafground.com/input.xhtml')
 # 滑动条处理 1.定位滑动条 2.获取滑块元素大小 3.计算偏移量
slider=driver.find_element(By.ID,'j_idt106:j_idt120')

slider_width=slider.size['width']
offset=slider_width/5

# 使用ActionChains进行拖动操作
action=ActionChains(driver)
action.click_and_hold(slider).move_by_offset(offset,0).release().perform() # 点击并保持 移动偏移量 释放鼠标  执行以上动作链条


#文本框自增自减操作
number_input=driver.find_element(By.ID,'j_idt106:j_idt118_input')
#清空
number_input.clear()
#手动输入值
number_input.send_keys("10")

number_input.send_keys(Keys.ARROW_UP)
time.sleep(1)
number_input.send_keys(Keys.ARROW_DOWN)

#文本框点击弹出日期

date_input=driver.find_element(By.ID,'j_idt106:j_idt116_input')
date_input.click()
date_element=driver.find_element(By.XPATH,'//*[@id="j_idt106:j_idt116_panel"]/div/div[2]/table/tbody/tr[2]/td[5]/a')
date_element.click()

# 窗口最大化
driver.maximize_window()
time.sleep(1)
# 页面截图
driver.save_screenshot('test.png')