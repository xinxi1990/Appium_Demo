#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
首页
'''

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
from appium.webdriver.common.mobileby import By
from pages.function import Funtion
from driver.driver import AppiumDriver


class HomePage(Funtion):

    _tv_search = (By.ID, "tv_search")
    _user_profile = (By.ID, "user_profile_icon")
    _display_time = 5

    def __init__(self):
        self.driver = AppiumDriver.getDriver()
        self.fun = Funtion(self.driver)
        self.logger = self.fun.logger

    def home_serch(self):
        self.display_wait(self._display_time, *self._tv_search).click()
        self.logger.info("点击首页搜索")

    def home_user(self):
        self.display_wait(self._display_time, *self._user_profile).click()
        self.logger.info("点击首页头像")


homePage = HomePage()