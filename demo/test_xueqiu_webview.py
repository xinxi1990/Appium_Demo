#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import unittest
from appium import webdriver
from time import sleep, time
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions



class TestXueqiu(unittest.TestCase):
    loaded = False

    def setUp(self):
        print("setup")
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "demo"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = "true"
        caps["automationName"] = "UiAutomator2"
        caps["chromedriverExecutable"] = "/Users/xinxi/Desktop/AppiumDemo8_Android/chromedriver2"

        if TestXueqiu.loaded == True:
            caps["noReset"] = "true"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)
        loaded = True
        # self.driver.find_element_by_xpath("//*[@text='好的']").click()


    def test_battery(self):
        print(self.driver.execute_script("mobile:batteryInfo"))

    def test_shell(self):
        print("test_shell")
        print(self.driver.execute_script("mobile:shell",
                                         {"command": "am",
                                          "args": ["start", "-n", "com.luojilab.player/com.luojilab.business.welcome.SplashActivity"]}))


    def test_webview(self):
        self.driver.find_element(By.ID,"com.xueqiu.android:id/image").click()
        print(self.driver.contexts)
        sleep(5)
        contexts_list = self.driver.contexts
        self.driver.switch_to.context(contexts_list[-1])
        print(self.driver.contexts)
        print(self.driver.page_source)
        self.driver.find_element_by_css_selector("#app > div > div > div.turntable_header-box_1RX > div > ul > li:nth-child(5) > div").click()
        print("test_webview test over...")



    def test_demo(self):
        # w = WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(By.XPATH,"//*[@text='好的']"))
        wl =  WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[@text='好的']")))
        wl.click()



    def test_jijin_login(self):

        self.driver.find_element_by_xpath("//*[@text='好的']").click()
        WebDriverWait(self.driver, 10, 0.5).until(
            lambda x: x.find_element_by_xpath("//*[@text='交易' and contains(@resource-id,'tab_name')]"))

        self.driver.find_element_by_xpath("//*[@text='交易']").click()
        self.driver.find_element_by_xpath("//*[@text='基金']").click()
        for i in range(8):
            sleep(0.5)
            print(self.driver.contexts)
            print(self.driver.current_context)
            print(self.driver.page_source)