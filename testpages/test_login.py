#!/usr/bin/env python
# -*- coding: utf-8 -*-

import allure
import pytest
from driver.driver import AppiumDriver
from pages.base import BasePage
from pages.home import HomePage
from pages.login import LoginPage
from pages.page_decorator import go_to_login_page


@allure.feature("测试登录")
class TestLogin(BasePage):

    @allure.story('测试参数化登录')
    @pytest.mark.parametrize("account,pwd",[("18513571170", 1233211),("18513571171", 1233211),("18513571171", 1233211)])
    @go_to_login_page()
    def test_more_login(self, account="18513571170",pwd="1233211"):
        print("test_login")
        print(account)
        print(pwd)
        LoginPage().phone_login(account,pwd)

