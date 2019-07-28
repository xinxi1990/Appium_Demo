#!/usr/bin/env python
# -*- coding: utf-8 -*-

import allure
from pages.base import BasePage
from pages.home import Home
from pages.serach import Search


@allure.feature("测试首页")
class TestSearch(BasePage):

    def setUp(self):
        super(TestSearch,self).setUp()
        self.home_page = Home(self.driver)
        self.search_page = Search(self.driver)
        #重写父类setUp方法

    @allure.story('测试首页搜索:拼多多')
    def test_add_stock(self):
        self.home_page.home_serch()
        search = self.search_page.add_stock()
        self.search_page.assert_obj_exits(None,*search.followd_btn)
        self.search_page.logger.info("股票添加成功...")
        search.clean_serach_input()
