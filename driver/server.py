#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,subprocess,time
from libs.logger import init_logger
logger = init_logger()  # 初始化日志


class AppiumServer:
    def __init__(self, host, port, timeout):
        self.host = host
        self.port = port
        self.timeout = timeout

    def start_server(self):
        self.stop_server()
        cmd = "appium --session-override -a %s -p %s" % (self.host, self.port)
        appium_process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1,
                                          close_fds=True)

        logger.info("启动appium命令:{}".format(cmd))
        is_start = False
        start_time = time.time()
        while not is_start and (time.time() - start_time) < float(self.timeout):
            appium_line = appium_process.stdout.readline().strip().decode()
            time.sleep(1)
            logger.info("---------启动服务中----------")
            if 'listener started' in appium_line:
                logger.info("---------启动服务成功----------")
                is_start = True
        return is_start


    def stop_server(self):
        cmd = "lsof -i:%s" % self.port
        plist = os.popen(cmd).readlines()
        if len(plist) > 1:
            line = plist[1]
            temp_line = line.split("    ")[1]
            temp_pid = temp_line.split(" ")[0]
            os.popen("kill -9 %s" % temp_pid)