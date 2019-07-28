#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : xinxi
@Time    : 2018/12/5 18:34
@describe: 创建driver
"""

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os,sys,subprocess,pytest,time,allure,base64
from allure.constants import AttachmentType
from config import screenshot_folder
sys.path.append('..')
from libs.logger import init_logger
logger = init_logger()  # 初始化日志
from driver.driver import AppiumDriver
from driver.server import AppiumServer
from libs.exceptions import StartServerTimeout



@pytest.fixture(scope="module", autouse=True)
def start_appium():
    appium_server = AppiumServer("127.0.0.1", "4723", "10")
    if not appium_server.start_server():
        raise StartServerTimeout("在指定时间{}秒内未能启动appium server，请手动检查".format("10"))


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    '''
    hook pytest失败
    :param item:
    :param call:
    :return:
    '''
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    # we only look at actual failing test calls, not setup/teardown
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode) as f:
            # let's also access a fixture for the fun of it
            if "tmpdir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
            f.write(rep.nodeid + extra + "\n")
        logger.info("测试失败了")
        with allure.step('添加失败截图...'):
            allure.attach(rep.nodeid, adb_screen_shot(),type=AttachmentType.PNG)




def appium_screen_shot():
    '''
    截图操作
    pic_name:截图名称
    :return:
    '''
    pic_name
    try:
        fail_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        fail_pic = str(fail_time) + "截图"
        pic_name = os.path.join(screenshot_folder, fail_pic)
        AppiumDriver.init_driver().save_screenshot(pic_name)
        logger.info('截图:{}'.format(pic_name))
        f = open(pic_name, 'rb')  # 二进制方式打开图文件
        base64_str = base64.b64encode(f.read())  # 读取文件内容，转换为base64编码
        f.close()
        return base64_str
    except Exception as e:
        logger.info("{}截图失败!{}".format(pic_name, e))



def screen_shot(driver):
    '''
    截图操作
    pic_name:截图名称
    :return:
    '''
    pic_name
    try:
        fail_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        fail_pic = str(fail_time) + "截图"
        pic_name = os.path.join(screenshot_folder, fail_pic)
        driver.screenshot("{}.jpg".format(pic_name))
        logger.info('截图:{}'.format(pic_name))
        f = open(pic_name, 'rb')  # 二进制方式打开图文件
        base64_str = base64.b64encode(f.read())  # 读取文件内容，转换为base64编码
        f.close()
        return base64_str
    except Exception as e:
        logger.info("{}截图失败!{}".format(pic_name, e))


def adb_screen_shot():
    '''
    adb截图
    :return:
    '''
    file_info = ''
    fail_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    fail_pic = str(fail_time) + "失败截图.jpg"
    pic_name = os.path.join(screenshot_folder, fail_pic)
    cmd = 'adb shell /system/bin/screencap -p /sdcard/screenshot.jpg'
    subprocess.call(cmd,shell=True)
    cmd = 'adb pull /sdcard/screenshot.jpg {}'.format(pic_name)
    subprocess.call(cmd, shell=True)
    with open(pic_name, 'rb+') as r:
        file_info = r.read()
        #file_info = base64.b64encode(r.read()).decode('utf-8')  # 读取文件内容，转换为base64编码
    return file_info


