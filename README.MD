# 简介
使用appium+pytest+allure进行Android的UI自动化测试

# 环境搭建

## pytest框架
pip install pytest==3.7

## allure报告
```
命令:
py.test --alluredir=reports
allure generate reports
allure generate reports --clean
allure generate --clean reports -o myreport
用火狐浏览器打开,chrome会404
```

## appium官方文档
capability设置 https://appium.io/docs/en/writing-running-appium/caps/<br>


## 运行命令

测试单个方法: pytest -k test_home_search --alluredir=reports -s <br>
测试单个用例:pytest -s testcase/test_find.py <br>
测试PO级Case: pytest -v -m "P0" --alluredir=reports <br>
不测试PO级Case: pytest -v -m "not P0" --alluredir=reports <br>

## 生成报告
allure generate --clean reports -o myreport


## 参考文档
pytest-html<br>
https://www.cnblogs.com/landhu/p/7463631.html

pytest-html<br>
https://blog.csdn.net/liuchunming033/article/details/79624474


Python中的单例模式<br>
http://funhacks.net/2017/01/17/singleton/