import os
import re
import mysql.connector

from tkinter import messagebox

os.environ["PATH"] += os.pathsep + r'C:/Project/project/Testing'

from selenium import webdriver as wd

driver = wd.Chrome();

#register
try:
    driver.get("http://127.0.0.1:8000/Billing_System/register/")
except:
    messagebox.showwarning("Error","Please check network")

driver.find_element_by_name("email").send_keys("test@gmail.com")
driver.find_element_by_name("username").send_keys("Test")
driver.find_element_by_name("password1").send_keys("Test@1234")
driver.find_element_by_name("password2").send_keys("Test@1234")
driver.find_element_by_name("Phone_number").send_keys("1234567890")
driver.find_element_by_name("meter_no").send_keys("100022")
driver.find_element_by_xpath("//button[@type='submit']").click()
url = driver.current_url
if url == "http://127.0.0.1:8000/Billing_System/login_home/":
    messagebox.showinfo("Success","-->New User Registered")
elif url == "http://127.0.0.1:8000/Billing_System/register/":
    messagebox.showerror("Fail","Fail to Register")
    driver.quit()
#logout
driver.find_element_by_xpath("//a[text()='Logout']").click()
url = driver.current_url
if url == "http://127.0.0.1:8000/Billing_System/login_view/":
    messagebox.showinfo("Success","-->You are successfully logout ")
    
else:
    messagebox.showerror("Fail","Fail to logout")
    driver.quit()
#login
try:
    driver.get("http://127.0.0.1:8000/Billing_System/login_view/")
except:
    messagebox.showwarning("Error","Please check network")
    
driver.find_element_by_name("email").send_keys("test@gmail.com")
driver.find_element_by_name("password").send_keys("Test@1234")
driver.find_element_by_xpath("//button[text()='Log in']").click()
url = driver.current_url
if url == "http://127.0.0.1:8000/Billing_System/login_home/":
    messagebox.showwarning("Success","-->You are successfully log in")
    
else:
    messagebox.showerror("Fail","Fail to login")
    driver.quit()

#generate bill
driver.get("http://127.0.0.1:8000/Billing_System/generate_bill/")
#unit consumed
driver.find_element_by_name("unit").send_keys("20")

#click on generate
driver.find_element_by_xpath("//input[@value='Generate']").click()

url = driver.current_url
if url == "http://127.0.0.1:8000/Billing_System/view_bill/":
    messagebox.showinfo("Success","Bill Generated")
else:
    messagebox.showerror("Fail","invalid input")
    driver.quit()

#payment
#netbanking payment
driver.get("http://127.0.0.1:8000/payment/bhim/")

#generate bill if not generated
url = driver.current_url
if url == "http://127.0.0.1:8000/Billing_System/generate_bill/":
    driver.get("http://127.0.0.1:8000/Billing_System/generate_bill/")
    driver.find_element_by_name("unit").send_keys("40")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Generate']").click()


#payment
driver.get("http://127.0.0.1:8000/payment/bhim/")
driver.find_element_by_name("UPI_ID").send_keys("1234@upi")
driver.find_element_by_xpath("//input[@type = 'submit' and @value='Pay']").submit()
url = driver.current_url
if url == "http://127.0.0.1:8000/payment/bhim/":
    messagebox.showerror("Error","Invalid input")
    driver.quit()
else:
    messagebox.showinfo("Success","Payment done")
#view status ,view and download     
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
    messagebox.showerror("Fail","Fail to view")
    driver.quit()

#logout
driver.find_element_by_xpath("//a[text()='Logout']").click()
url = driver.current_url
if url == "http://127.0.0.1:8000/Billing_System/login_view/":
    messagebox.showinfo("Success","-->You are successfully logout ")
    
else:
    messagebox.showerror("Fail","Fail to logout")
driver.quit()

