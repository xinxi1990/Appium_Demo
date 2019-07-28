#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import unittest
from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import By
from selenium.webdriver.support import expected_conditions
from pages.function import Funtion
from driver.driver import AppiumDriver



class SearchPage(Funtion):

    _tv_search = (By.ID, "tv_search")
    _search_input_text  = (By.ID,"search_input_text")
    _follow_btn  = (By.ID,"follow_btn")
    followd_btn = (By.ID, "com.xueqiu.android:id/followed_btn") # 已添加
    _next_time = By.XPATH, "//*[@text='下次再说']"
    _clean_btn = By.XPATH, "//*[@text='取消']"
    _display_time = 5
    _search_words = "pdd"

    def __init__(self):
        self.driver = AppiumDriver.getDriver()
        self.fun = Funtion(self.driver)
        self.logger = self.fun.logger

    def add_stock(self):
        """
        增加股票
        :return:
        """
        # self.find_obj(self._display_time,*self._tv_search)
        # self.display_wait(self._display_time,*self._tv_search).click()
        # self.logger.info("点击搜索框...")
        self.display_wait(self._display_time, *self._search_input_text).send_keys(self._search_words)
        self.logger.info("输入:{}...".format(self._search_words))
        if len(self.driver.find_elements(*self.followd_btn)) > 0:
            self.driver.find_element(*self.followd_btn).click()
            self.logger.info("取消已添加股票...")
        self.display_wait(self._display_time, *self._follow_btn).click()
        self.logger.info("点击添加股票...")
        self.display_wait(self._display_time, *self._next_time)
        if len(self.driver.find_elements(*self._next_time)) > 0:
            self.driver.find_element(*self._next_time).click()
            self.logger.info("点击下次再说...")
        return self


    def clean_serach_input(self):
        wl = self.display_wait(self._display_time,*self._clean_btn).click()
        self.logger.info("取消搜索输入...")

