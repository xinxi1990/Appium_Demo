#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
自选页面
"""

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import pytest,unittest
from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import By
from selenium.webdriver.support import expected_conditions
from pages.function import Funtion
from driver.driver import AppiumDriver

class OptionalPage(Funtion):

    _optional_btn = (By.XPATH,"//*[@text='自选' and @resource-id='com.xueqiu.android:id/tab_name' and @class='android.widget.TextView']") # 自选按钮
    _usa_stock_btn = (By.XPATH,"//*[@text='美股' and @resource-id='com.xueqiu.android:id/text']") # 美股按钮
    _portfolio =  (By.ID,"com.xueqiu.android:id/portfolio_whole_item")
    _add_portfolio = (By.ID,"com.xueqiu.android:id/image")
    _del_portfolio = (By.XPATH,"//*[@text='删除' and @resource-id='com.xueqiu.android:id/md_title']")
    _portfolio_serach = (By.ID,"com.xueqiu.android:id/action_create_cube")
    _display_time = 5

    def __init__(self):
        self.driver = AppiumDriver.getDriver()
        self.fun = Funtion(self.driver)
        self.logger = self.fun.logger

    def get_optional(self):
        '''
        点击自选
        :return:
        '''
        self.display_wait(self._display_time,*self._optional_btn).click()
        self.logger.info("点击自选")
        self.display_wait(self._display_time,*self._usa_stock_btn).click()
        self.logger.info("点击美股")
        pf = self.display_wait(self._display_time, *self._portfolio)
        if not pf == None:
            TouchAction(self.driver).long_press(pf).release().perform()
            self.logger.info("长按股票...")
            self.display_wait(self._display_time,*self._del_portfolio).click()
            self.logger.info("删除股票...")
            self.serach_optional()
        else:
            self.add_us_portfolio()


    def add_us_portfolio(self):
        '''
        美股中加股票
        :return:
        '''
        ap = self.display_wait(self._display_time, *self._add_portfolio)
        if not ap == None:
            ap.click()
            self.logger.info("添加股票...")


    def serach_optional(self):
        '''
        美股中加股票
        :return:
        '''
        self.display_wait(self._display_time, *self._portfolio_serach).click()
        self.logger.info("点击搜索股票...")

