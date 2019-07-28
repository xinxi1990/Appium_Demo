#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

current_path = os.path.abspath(os.path.dirname(__file__))
screenshot_folder = os.path.join(current_path,"screenshot")
if not os.path.exists(screenshot_folder):
   os.mkdir(screenshot_folder)
   print "创建截图目录:{}".format(screenshot_folder)