import os
import re


from tkinter import messagebox

os.environ["PATH"] += os.pathsep + r'C:/Project/project/Testing'

from selenium import webdriver as wd
driver = wd.Chrome()

#login
try:
    driver.get("http://127.0.0.1:8000/Billing_System/login_view/")
except:
    messagebox.showwarning("Error","Please check network")
driver.find_element_by_name("email").send_keys("xyz@gmail.com")
driver.find_element_by_name("password").send_keys("Xyz@1234")
driver.find_element_by_xpath("//button[text()='Log in']").click()


#netbanking payment or any other payment method
driver.get("http://127.0.0.1:8000/payment/netbanking/")

url = driver.current_url
if url == "http://127.0.0.1:8000/Billing_System/generate_bill/":
    messagebox.showwarning("Success","Bill not generated")

else:
    messagebox.showerror("Fail","Something wrong")

driver.quit()