#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys,os,time,allure
reload(sys)
sys.setdefaultencoding( "utf-8" )
from functools import wraps
from allure.constants import AttachmentType
from conftest import adb_screen_shot
from lxml import etree
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from libs.logger import init_logger
logger = init_logger()  # 初始化日志



class Funtion():

    black_words_list = [u"//*[@text='好的']"]
    # 检查元素黑名单

    def __init__(self,driver):
        self.driver = driver
        self.logger = logger  # 初始化日志


    def display_wait(self, wait_time=5, *loc):
        '''
        封装显示等待
        :return:
        '''
        el = None
        try:
            el = WebDriverWait(self.driver, wait_time).until(expected_conditions.visibility_of_element_located(loc))
        except Exception as e:
            self.logger.info("显示等待元素:{},异常:{}".format(loc, e))
        finally:
            return el


    def find_obj(self, wait_time, *loc):
        '''
        封装点击操作
        :return:
        '''
        try:
            el = self.display_wait(wait_time, *loc)
            if not el == None:
                return el
            else:
                raise Exception
        except Exception as e:
            page_source = self.driver.page_source
            xml=etree.XML(str(page_source).encode("utf-8"))
            for w in self.black_words_list:
                if (len(xml.xpath(w))) > 0:
                    self.driver.find_element(By.XPATH,w).click()
                    self.logger.info("点击黑名单元素:{}".format(w))

    def assert_obj_exits(self, wait_time=5, *loc):
        '''
        断言元素是否存在
        :return:
        '''
        if not self.display_wait(wait_time,*loc) == None:
           self.logger.error("{}:元素断言存在成功...".format(str(loc)))
           assert True
        else:
            self.logger.error("{}:元素断言存在失败...".format(str(loc)))
            assert False


    def screenshot(self,func):
        def wrapper(self, first, second, msg=None):
            try:
                func(self, first, second, msg=None)
            except AssertionError:  # 等待AssertionError
                path = os.getcwd() + "/screenshot"
                timestamp = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
                os.popen("adb wait-for-device")
                os.popen("adb shell screencap -p /data/local/tmp/tmp.png")
                if not os.path.isdir(os.getcwd() + "/screenshot"):
                    os.makedirs(path)
                os.popen("adb pull /data/local/tmp/tmp.png " + path + "/" + timestamp + ".png")
                os.popen("adb shell rm /data/local/tmp/tmp.png")
            raise AssertionError, msg  # 抛出AssertionError和信息
        return wrapper


    @staticmethod
    def screen_shot_cut(text):
        def decorator(func):
            def wrapper(*args, **kw):
                logger.info('%s %s():' % (text, func.__name__))
                with allure.step('添加截图'):
                    allure.attach('添加截图', adb_screen_shot(), type=AttachmentType.PNG)
                f = func(*args, **kw)
                with allure.step('添加截图'):
                    allure.attach('添加截图', adb_screen_shot(), type=AttachmentType.PNG)
                return  f
            return wrapper
        return decorator


    def find_text(self,*loc):
        get_text = self.driver.find_element(*loc).text
        self.logger.info("获取的文案:{}".format(get_text))
        return get_text


