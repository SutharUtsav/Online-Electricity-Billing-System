import os
import re
import mysql.connector

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

#netbanking payment
driver.get("http://127.0.0.1:8000/payment/netbanking/")

#generate bill if not generated
url = driver.current_url
if url == "http://127.0.0.1:8000/Billing_System/generate_bill/":
    driver.get("http://127.0.0.1:8000/Billing_System/generate_bill/")
    driver.find_element_by_name("unit").send_keys("40")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Generate']").click()

#check for payment has already done or not
driver.get("http://127.0.0.1:8000/payment/netbanking/")

# create connection object
con = mysql.connector.connect(host="localhost", user="root",password="", database="project_db")
  
# create cursor object
cursor = con.cursor()
  
# assign data query
query0 = "select id from login_login where email = 'xyz@gmail.com'"
cursor.execute(query0)
id = cursor.fetchall()

query1 = "select bill_no from billing_system_generate_bill where id = (select max(id) from billing_system_generate_bill where key_id = %s )"
# executing cursor
cursor.execute(query1,id[0])
# display all records
bill_no = cursor.fetchall()



query2 = "select * from payment_netbanking where bill_no =%s"
cursor.execute(query2,bill_no[0])
r1 = cursor.fetchall()

query3 = "select * from payment_bhimupi where bill_no =%s"
cursor.execute(query3,bill_no[0])
r2 = cursor.fetchall()

query4 = "select * from payment_mobilebanking where bill_no =%s"
cursor.execute(query4,bill_no[0])
r3 = cursor.fetchall()

query5 = "select * from payment_cradit where bill_no =%s"
cursor.execute(query5,bill_no[0])
r4 = cursor.fetchall()

if r1 or r2 or r3 or r4:
    messagebox.showwarning("Warning","Payment already done")
else:
    driver.get("http://127.0.0.1:8000/payment/netbanking/")
    driver.find_element_by_name("bankName").send_keys("icici")
    driver.find_element_by_name("branchCode").send_keys("icici1234")
    driver.find_element_by_name("accountNumber").send_keys("AC1234")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Pay']").submit()
    url = driver.current_url
    if url == "http://127.0.0.1:8000/payment/netbanking/":
        messagebox.showerror("Error","Invalid input")
    else:
        messagebox.showinfo("Success","Payment done")
driver.quit()

