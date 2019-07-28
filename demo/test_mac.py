#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest,allure,unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import utilities
import time

class TestMac(unittest.TestCase):


    windowPath = "/AXApplication[@AXTitle='Calculator']/AXWindow[0]"
    resultGroupPath = windowPath + "/AXGroup[0]"
    basicGroupPath = windowPath + "/AXGroup[1]"
    scientificGroupPath = windowPath + "/AXGroup[2]"
    programmerGroupPath = windowPath + "/AXGroup[1]"

    def setUp(self):
        print("setup")
        caps = {}
        caps["platformName"] = "Mac"
        caps["deviceName"] = "Mac"
        caps["noReset"] = "true"
        caps["fullReset"] = "false"
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def test_demo(self):
        print("test_demo")
        self.driver.get("Calculator")
        time.sleep(3)
        # button_clear = self.driver.find_element_by_xpath(self.basicGroupPath + "/AXButton[@AXDescription='clear']")
        e = self.driver.find_element_by_xpath("/AXApplication[@AXTitle='Calculator']/AXWindow[0]/AXGroup[1]/AXButton[@AXDescription='clear']")
        ActionChains(self.driver).click(e).perform()
        # self.driver.find_element_by_name('clear').click()

        # print 'Opening the "Safari" app'
        # self.driver.get("Safari")
        # time.sleep(3)
        # b = self.driver.page_source
        # print(b)
        # print 'Finding the Text Area'
        # search_field = self.driver.find_element_by_id('WEB_BROWSER_ADDRESS_AND_SEARCH_FIELD')
        # self.driver.find_element_by_id("NSAccessibilitySegment").click()