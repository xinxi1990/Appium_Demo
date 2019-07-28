# -*- coding: utf-8 -*-

from functools import wraps

from pages.login import LoginPage
from pages.home import HomePage
from libs.exceptions import PageReachedError


def go_to_login_page():
    """装饰器: 进入到首页登录页面"""
    def wrapper(func):
        @wraps(func)
        def _wrapper(*args, **kwargs):
            HomePage().home_user()
            LoginPage().go_phone_login()
            f = func(*args, **kwargs)
            return f
        return _wrapper
    return wrapper


