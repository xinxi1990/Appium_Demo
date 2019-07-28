#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import unittest,os
from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions



class TestXueqiuH5(unittest.TestCase):
    loaded = False

    def setUp(self):
        print("setup")
        caps={}
        caps["platformName"]="android"
        caps["deviceName"]="seveniruby"
        caps["browserName"]="chrome"
        caps["noReset"]="true"
        caps["fullReset"]="false"
        caps["forceMjsonwp"]="true"
        caps["dontStopAppOnReset"]="true"
        caps["chromedriverExecutableDir"] = os.getcwd() + "/webdriver"
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)


    def test_webview(self):
        self.driver.get("https://danjuanapp.com/my-money?channel=1300100158&refer=xq_trade")
        self.driver.find_element_by_css_selector(".btns .blank").click()
        self.driver.find_element_by_css_selector(".pass_switch").click()
        self.driver.find_element_by_name("telno").send_keys("15600534760")
        self.driver.find_element_by_name("pass").send_keys("password")
        self.driver.find_element_by_id("next").click()
