import os
import re

from tkinter import messagebox

os.environ["PATH"] += os.pathsep + r'C:/Project/project/Testing'

from selenium import webdriver as wd

driver = wd.Chrome();
#login
try:
    driver.get("http://127.0.0.1:8000/Billing_System/login_view/")
except:
    messagebox.showwarning("Error","Please check network")

driver.find_element_by_name("email").send_keys("dars@gmail.com")
driver.find_element_by_name("password").send_keys("Yash@1234")
driver.find_element_by_xpath("//button[text()='Log in']").click()
url = driver.current_url
if url == "http://127.0.0.1:8000/Billing_System/login_home/":
    messagebox.showwarning("Success","-->You are successfully log in\n-->Now Your are going to update profile")
    driver.find_element_by_xpath("//a[text()='Update']").click()
    driver.find_element_by_name("username").send_keys("Yooo")
    driver.find_element_by_xpath("//button[text()='Save changes']").click()
    driver.back()
    url = driver.current_url
    if url == "http://127.0.0.1:8000/Billing_System/account/":
        messagebox.showinfo("Success","-->You are successfully update profile ")
        driver.quit()
    else:
        messagebox.showerror("Fail","Fail to update")
else:
        messagebox.showerror("Fail","Something went wrong!!")
driver.quit()

