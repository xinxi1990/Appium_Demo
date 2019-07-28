#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
登录页面
"""
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
from appium.webdriver.common.mobileby import By
from pages.function import Funtion
from driver.driver import AppiumDriver

class LoginPage(Funtion):

    _login_btn = (By.ID, "tv_login")
    _phone_login = (By.ID, "tv_login_by_phone_or_others")
    _account_login = (By.ID, "tv_login_with_account")
    _login_account = (By.ID, "login_account")
    _login_password= (By.ID, "login_password")
    _button_next= (By.ID, "button_next")
    _sure_btn = (By.XPATH, "//*[@text='确定']")
    _login_text = (By.ID, "md_content")
    _account = "18513571170"
    _pwd = "123321"

    _display_time = 5

    def __init__(self):
        self.driver = AppiumDriver.getDriver()
        self.fun = Funtion(self.driver)
        self.logger = self.fun.logger


    def go_phone_login(self):
        '''
        进入到登录页面
        :return:
        '''
        self.display_wait(self._display_time, *self._login_btn).click()
        self.logger.info("点击登录")
        self.display_wait(self._display_time, *self._phone_login).click()
        self.logger.info("点击手机登录")
        self.display_wait(self._display_time, *self._account_login).click()
        self.logger.info("点击账号登录")



    def phone_login(self,account,pwd):
        self.display_wait(self._display_time, *self._login_account).clear().send_keys(account)
        self.logger.info("输入账号:{}".format(account))
        self.display_wait(self._display_time, *self._login_password).clear().send_keys(pwd)
        self.logger.info("输入密码:{}".format(pwd))
        self.display_wait(self._display_time, *self._button_next).click()
        self.logger.info("点击登录")
        self.sure = self.display_wait(self._display_time, *self._sure_btn)
        if self.sure != None:
            login_fail_text = self.find_text(*self._login_text)
            self.logger.info("登录失败,原因:" + login_fail_text)
            self.sure.click()
            self.logger.info("点击确定")
        else:
            self.logger.info("登录成功...")


loginPage = LoginPage()