import os
import re
import mysql.connector

from tkinter import messagebox

os.environ["PATH"] += os.pathsep + r'C:/Project/project/Testing'

from selenium import webdriver as wd


driver = wd.Chrome()
try:
    driver.get("http://127.0.0.1:8000/Billing_System/register/")
except:
    messagebox.showwarning("Error","Please check network")

driver.find_element_by_name("email").send_keys("abc@gmail.com")
driver.find_element_by_name("username").send_keys("abc")
driver.find_element_by_name("password1").send_keys("Abc@1234")
driver.find_element_by_name("password2").send_keys("Abc@1234")
driver.find_element_by_name("Phone_number").send_keys("9765432198")
driver.find_element_by_name("meter_no").send_keys("12345")
driver.find_element_by_xpath("//button[@type='submit']").click()
# create connection object
con = mysql.connector.connect(host="localhost", user="root",password="", database="project_db")
  
# create cursor object
cursor = con.cursor()
  
# assign data query
query1 = "select * from login_login where meter_no = 12345"
  
# executing cursor
cursor.execute(query1)
  
# display all records
table = cursor.fetchall()

if(table):
    messagebox.showinfo("Success","Meter No. exist")
else:
    messagebox.showerror("Fail","something wrong")
# closing cursor connection
cursor.close()
  
# closing connection object
con.close()

driver.quit()