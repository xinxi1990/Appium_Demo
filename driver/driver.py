#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest,unittest
from time import sleep
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class AppiumDriver():

    loaded = False
    driver = None
    lanuch_time = 5

    @classmethod
    def getDriver(cls):
        return cls.driver

    @classmethod
    def initDriver(cls):
        print("setup")
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "demo"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = True
        # caps["automationName"] = "UiAutomator2"
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(6)
        return cls.driver

