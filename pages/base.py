#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest,unittest
from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from driver.driver import AppiumDriver
from appium.webdriver.common.mobileby import By
from lxml import etree
from libs.logger import init_logger
logger = init_logger()  # 初始化日志


class BasePage(unittest.TestCase):

    _good_btn = By.XPATH, "//*[@text='好的']"
    wait_time = 5

    def close_ad(self):
        '''
        关闭启动弹框
        :return:
        '''
        if len(self.driver.find_elements(*self._good_btn)) > 0:
            self.driver.find_element(*self._good_btn).click()
            logger.info("处理启动弹框...")

    def setUp(self):
        self.driver = AppiumDriver.initDriver()
        print("appium id:{}".format(id(self.driver)))
        self.close_ad()





