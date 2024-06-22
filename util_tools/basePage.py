# -*- coding: UTF-8 -*-
"""
Project ：WebUI 
File    ：basePage.py
Author  ：张以白
Date    ：2024/6/20 0:07 
Desc    :
"""
import os.path
import time
from datetime import datetime
from time import sleep

from selenium.webdriver import ActionChains, Keys

from util_tools.log_utils.recordlog import logs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from config import setting


class BasePage(object):

    def __init__(self, driver):
        self.__driver = driver
        # 显示等待初始化操作
        self.__wait = WebDriverWait(self.__driver, setting.WAIT_TIME)

    def window_max(self):
        """窗口最大化"""
        self.__driver.maximize_window()

    def window_full(self):
        """全屏显示操作"""
        self.__driver.fullscreen_window()

    def screenshot(self):
        """浏览器截屏"""
        self.__driver.get_screenshot_as_png()

    def open_url(self, url):
        """打开测试页面"""
        self.__driver.get(url)

    @property
    def current_url(self):
        """获取当前页面url"""
        return self.__driver.current_url

    @property
    def get_title(self):
        """获取网页标题"""
        return self.__driver.title

    def refresh(self):
        """页面刷新"""
        self.__driver.refresh()

    @property
    def switch_to(self):
        """切换标签"""

        return self.__driver.switch_to

    def iframe(self, frame):
        """切换到iframe内联框架中"""
        self.switch_to.frame(frame)

    def exit_iframe(self):
        """退到父窗口"""
        self.switch_to.default_content()

    @property  # 使用 @property 装饰器可以将一个方法转换为一个只读属性，使得该方法可以像访问属性一样被调用
    def alert(self):
        """弹窗处理"""
        # return self.switch_to.alert
        return self.__wait.until(ec.alert_is_present())  # 等待 alert 对话框出现并切换到该对话框

    def alert_confirm(self):
        """确认"""
        self.alert.accept()

    def alert_cancel(self):
        self.alert.dismiss()

    def selenium_location(self, by, value):
        """
        二次封装方法，
        :param by:
        :param value:
        :return:
        """
        try:
            element = self.__wait.until(ec.visibility_of_element_located((by, value)))
            logs.info(f"找到元素{by}={value}")
            return element
        except Exception as e:
            logs.error(f"未找到元素{by}={value}")
            raise e

    def send_keys(self, locator: tuple, data):
        try:
            element = self.selenium_location(*locator)
            element.send_keys(data)
            logs.info("发送数据")
        except Exception as e:
            logs.error(f"发动数据时出错了")
            raise e

    def enter(self):
        try:
            # 模拟键盘回车键
            ActionChains(self.__driver).send_keys(Keys.ENTER).perform()
            logs.info("按下回车键")
        except Exception as e:
            logs.error(f"执行回车过程中出错了")
            raise e

    def right_click(self, locator: tuple):
        try:
            # 模拟鼠标右键
            element = self.selenium_location(*locator)
            ActionChains(self.__driver).context_click(element).perform()
            logs.info("模拟鼠标右键操纵")

        except Exception as e:
            logs.error(f"鼠标右键时失败了")
            raise e

    def double_click(self, locator: tuple):
        """鼠标双击操作"""
        try:
            element = self.selenium_location(*locator)
            ActionChains(self.__driver).double_click(element).perform()
            logs.info("鼠标双击执行")

        except Exception as e:
            logs.error(f"鼠标双击时失败了{e}")
            raise e
    def screen_shot(self,image_name):
        """
        封装截图方法
        :param image_name:
        :return:
        """
        current_time=datetime.now().strftime("%Y%m%d%H%M%S")
        file_name=f'{image_name}-{current_time}.png'
        file_path=os.path.join(setting.FILE_PATH['screenshot'],file_name)

        logs.info("封装截图方法")
        print(file_path+file_name)
        self.__driver.get_screenshot_as_file(file_path)
    def clear(self, locator: tuple):
        """
        清空文本
        :param locator:
        :return:
        """
        try:
            element = self.selenium_location(*locator)
            element.clear()
            logs.info("清空文本")

        except Exception as e:
            logs.error(f"清空文本失败{e}")
            raise e



if __name__ == '__main__':
    driver = webdriver.Chrome()

    bros = BasePage(driver)

    bros.open_url("https://www.leafground.com/input.xhtml")
    local = (By.XPATH, '//*[@id="j_idt88:j_idt101"]')
    bros.screen_shot('测试')
    bros.send_keys((local),'第一行数据')
    time.sleep(2)
    bros.enter()
    bros.send_keys((local),'第2行数据')
    time.sleep(2)
    bros.clear(local)
    time.sleep(2)
    # bros.right_click(local)
    # time.sleep(2)
    bros.double_click(local)
    time.sleep(2)
