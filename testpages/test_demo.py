#!/usr/bin/env python
# -*- coding: utf-8 -*-

import allure
import pytest

from pages.base import BasePage


@allure.feature("测试登录")
class TestDemo(BasePage):

    def setUp(self):
        super(TestDemo, self).setUp()



    @allure.story('测试参数化登录')
    @pytest.mark.parametrize("account,pwd",[("18513571170", 1233211),("18513571171", 1233211),("18513571171", 1233211)])
    # @go_to_login_page()
    def test_login(self, account,pwd):
        print("test_login")
        print(account)
        print(pwd)
