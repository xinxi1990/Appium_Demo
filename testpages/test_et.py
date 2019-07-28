#!/usr/bin/env python
# -*- coding: utf-8 -*-

import allure
from driver.driver import AppiumDriver
from pages.base import BasePage
from pages.home import HomePage
from pages.login import LoginPage
from pages.page_decorator import go_to_login_page


@allure.feature("测试...")
class TestET(BasePage):

    # def setUp(self):
    #     super(TestET,self).setUp()
    #     self.home_page = HomePage(self.driver)
    #     self.login_page = LoginPage(self.driver)
    #     #重写父类setUp方法
    #
    #
    # def test_et(self):
    #     self.driver = AppiumDriver.getDriver()
    #     print id(self.driver)
    #     assert False

    @go_to_login_page()
    def test_login(self):
        # self.home_page.home_user()
        # self.login_page.phone_login()
        print("go_to_login_page")