"""
tzm@20200513:提交个demo试试
"""

from selenium import webdriver
import time

driver = webdriver.Chrome()

url = "http://192.168.0.90/zfcapp/index.html#/login"

driver.get(url)

time.sleep(5)

driver.quit()