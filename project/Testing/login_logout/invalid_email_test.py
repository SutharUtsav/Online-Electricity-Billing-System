import os
import re

from tkinter import messagebox

os.environ["PATH"] += os.pathsep + r'C:/Project/project/Testing'

from selenium import webdriver as wd


driver = wd.Chrome();
#login
driver.get("http://127.0.0.1:8000/Billing_System/login_view/")

#1)Invalid mail address
driver.find_element_by_name("email").send_keys("devilh@mail")#invalid
driver.find_element_by_name("password").send_keys("devil@1234")#correct
driver.find_element_by_xpath("//button[text()='Log in']").click()




