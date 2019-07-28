#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pypom import Page
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox


class Mozilla(Page):

    def tet_demo(self):
        base_url = 'https://www.mozilla.org'
        driver = webdriver.Firefox(
            executable_path="/Users/xinxi/Documents/ideaProjcet/SeleniumDemo/drivers/geckodriver")
        page = Mozilla(driver, base_url).open()



