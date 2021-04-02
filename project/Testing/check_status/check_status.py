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
    
driver.find_element_by_name("email").send_keys("xyz@gmail.com")
driver.find_element_by_name("password").send_keys("Xyz@1234")
driver.find_element_by_xpath("//button[text()='Log in']").click()

#get link
driver.get("http://127.0.0.1:8000/Billing_System/check_status/")
try:
    driver.find_element_by_xpath("//button[text()='View']").click()
except:
    messagebox.showwarning("Warning","There are no bills")

url = driver.current_url
pattern = re.compile("^http://127.0.0.1:8000/Billing_System/status_pdf_view/([0-9]+)/$")
if pattern.match(url):
    messagebox.showinfo("Success","Success View")
    driver.back()
    try:
        driver.find_element_by_xpath("//button[text()='Paid']")
        messagebox.showwarning("Warning","Status is --> Bill Paid.")
    except:
        messagebox.showwarning("Warning","Status is --> Bill not paid.")
        
    driver.find_element_by_xpath("//button[text()='Download']").click()
    messagebox.showwarning("Success","Successfully Download")

else:
    messagebox.showerror("Fail","Fail")
driver.quit()