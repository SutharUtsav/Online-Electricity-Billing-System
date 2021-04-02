import os
import re

from tkinter import messagebox

os.environ["PATH"] += os.pathsep + r'C:/Project/project/Testing'

from selenium import webdriver as wd


driver = wd.Chrome();
#login
driver.get("http://127.0.0.1:8000/Billing_System/login_view/")

#2)invalid emailaddress
driver.find_element_by_name("email").send_keys("devil@gmail.com")#not registered
driver.find_element_by_name("password").send_keys("Devil@1234")#correct
driver.find_element_by_xpath("//button[text()='Log in']").click()




# #3)invalid  password
# driver.find_element_by_name("email").send_keys("devil33516@gmail.com")#correct
# driver.find_element_by_name("password").send_keys("123")#invalid
# driver.find_element_by_xpath("//button[text()='Log in']").click()
