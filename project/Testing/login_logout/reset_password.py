import os
import re

from tkinter import messagebox

os.environ["PATH"] += os.pathsep + r'C:/Project/project/Testing'

from selenium import webdriver as wd

driver = wd.Chrome();
#login page
try:
    driver.get("http://127.0.0.1:8000/Billing_System/login_view/")
except:
    messagebox.showwarning("Error","Please check network")
#reset link
driver.find_element_by_class_name("m-auto").click()
#send mail id
driver.find_element_by_name("email").send_keys("dars@gmail.com")
driver.find_element_by_xpath("//button[text()='Send reset email']").click()

url = driver.current_url
if url == "http://127.0.0.1:8000/Billing_System/password_reset/done/":
    messagebox.showwarning("Success","-->Password reset link is sent you\n-->Now you can change password from link")
    driver.find_element_by_xpath("//a[text()='Return to Login page']").click()
    url = driver.current_url
    if url == "http://127.0.0.1:8000/Billing_System/login_view/":
        messagebox.showinfo("Success","-->You are successfully change your password ")
        driver.quit()
    else:
        messagebox.showerror("Fail","fail to reset password")
else:
        messagebox.showerror("Fail","Fail to send reset link")
driver.quit()

