import os
import re

from tkinter import messagebox

os.environ["PATH"] += os.pathsep + r'C:/Project/project/Testing'

from selenium import webdriver as wd

driver = wd.Chrome()

#register
try:
    driver.get("http://127.0.0.1:8000/Billing_System/register/")
except:
    messagebox.showwarning("Error","Please check network")

driver.find_element_by_name("email").send_keys("xyz@gmail.com")
driver.find_element_by_name("username").send_keys("xyz")
driver.find_element_by_name("password1").send_keys("Xyz@1234")
driver.find_element_by_name("password2").send_keys("Xyz@1234")
driver.find_element_by_name("Phone_number").send_keys("9765432198")
driver.find_element_by_name("meter_no").send_keys("12435")
driver.find_element_by_xpath("//button[@type='submit']").click()
url = driver.current_url
if url == "http://127.0.0.1:8000/Billing_System/login_home/":
    messagebox.showinfo("Success","-->New User Registered")
    driver.quit()
elif url == "http://127.0.0.1:8000/Billing_System/register/":
    messagebox.showerror("Fail","Fail to Register")
driver.quit()

