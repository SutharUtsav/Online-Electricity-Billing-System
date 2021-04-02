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
    messagebox.showwarning("Success","-->You are successfully log in\n-->Now Your are going to logout")
    driver.find_element_by_xpath("//a[text()='Logout']").click()
    url = driver.current_url
    if url == "http://127.0.0.1:8000/Billing_System/login_view/":
        messagebox.showinfo("Success","-->You are successfully logout ")
        driver.quit()
    else:
        messagebox.showerror("Fail","Fail to logout")
else:
        messagebox.showerror("Fail","Fail to login")
driver.quit()

