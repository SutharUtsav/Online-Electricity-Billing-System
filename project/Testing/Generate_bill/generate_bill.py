import os
import re
from tkinter import messagebox
from selenium.webdriver.support.ui import Select

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


#two iteration for both invalid and valid entries
for i in range(0,2):
    #get generate bill link
    driver.get("http://127.0.0.1:8000/Billing_System/generate_bill/")
    #unit consumed
    if i == 0:
        #valid
        driver.find_element_by_name("unit").send_keys("20")
    else:
        #invalid
        driver.find_element_by_name("unit").send_keys("xx")
    #click on generate
    driver.find_element_by_xpath("//input[@value='Generate']").click()

    url = driver.current_url
    if url == "http://127.0.0.1:8000/Billing_System/view_bill/":
        messagebox.showinfo("Success","Bill Generated")
        
    else:
        messagebox.showerror("Fail","invalid input")
        driver.quit()







