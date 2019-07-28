#!/usr/bin/env python
# -*- coding: utf-8 -*-

import allure,unittest


from pages.base import BasePage
from pages.optional import OptionalPage
from pages.home import HomePage
from pages.serach import SearchPage
from pages.function import Funtion


@allure.feature("测试自选")
class TestOptional(BasePage):

    def setUp(self):
        super(TestOptional, self).setUp()
        self.optional_page = OptionalPage()
        self.home_page = HomePage()
        self.search_page = SearchPage()
        self.wait_time = 5


    @allure.story('测试首页自选:删除股票-添加股票')
    @Funtion.screen_shot_cut("测试首页自选:删除股票-添加股票")
    def test_select_stock(self):
        self.optional_page.get_optional()
        search = self.search_page.add_stock()
        self.search_page.assert_obj_exits(self.wait_time, *search.followd_btn)
        self.search_page.logger.info("股票添加成功...")
