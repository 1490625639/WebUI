# -*- coding: UTF-8 -*-
"""
Project ：web_test 
File    ：ele_wait.py
Author  ：张以白
Date    ：2024/6/19 20:43 
Desc    :
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys # 文本框
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver=webdriver.Chrome()
driver.get("https://www.leafground.com/input.xhtml")

#强制等待
# time.sleep(2)
# driver.find_element(By.ID,'j_idt106:thisform:age').click()
#显示等待   明确的要等到某个元素的出现，等不到就一直等，除非在规定的时间内都没有找到，那么就跑出异常
# ele=WebDriverWait(driver,10).until(
#     EC.visibility_of_element_located((By.ID,'j_idt106:thisfm:age'))
# )
# print(ele)
# 隐式等待 作用全局
driver.implicitly_wait(10)

driver.find_element(By.ID,'j_idt106:float-input')