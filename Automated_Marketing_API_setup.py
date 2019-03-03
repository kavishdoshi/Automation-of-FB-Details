#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 10:49:49 2019

Getting of ADID and Token 

Note: If there is both Facebook Login and Marketing API on the left hand side it will work .. Otherwise comment out the code
    and use the commented code. Beacuse the id changes by 1
"""
#/anaconda3/envs/UN/lib/python3.7/site-packages/selenium/webdriver/chrome/chromedriver
#Login Deatils will be stored in the file Login_Details
username = ""
password = ""
app_name = ""
driver_path = ""
first = int(raw_input("If you want to change/enter(for first time) your login details enter 1 otherwise enter any other number:"))
if first == 1:
    username = raw_input("Enter your username:")
    password = raw_input("Enter your password:")
    app_name = raw_input("Enter your app_name:")
    f = open("Login_Details", "w")
    x = username + "\n"
    f.write(x)
    y = password + "\n"
    f.write(y)
    f.write(app_name)
    f.close()
first = int(raw_input("If you want to change/enter(for first time) your driver path enter 1 otherwise enter any other number:"))
if first == 1:
    driver_path = raw_input("Copy your driverpath:")
    f = open("Driver_Path_Details", "w")
    f.write(driver_path)
    f.close()
f = 'Login_Details'
with open(f) as fp:
    line = fp.readline()
    cnt = 1
    while line:
        if cnt == 1:
            username = line.strip()
            line = fp.readline()
            cnt += 1
        elif cnt == 2:
            password = line.strip()
            line = fp.readline()
            cnt += 1
        elif cnt == 3:
            app_name = line.strip()
            line = fp.readline()
            cnt += 1
        elif cnt == 4:
            driver_path = line.strip()
            line = fp.readline()
            cnt+=1

f1 = 'Driver_Path_Details'
with open(f1) as fp:
    line = fp.readline()
    cnt = 1
    while line:
        if cnt == 1:
            driver_path = line.strip()
            line = fp.readline()
            cnt += 1
    
print(username)
print(password)
print(app_name)
print(driver_path)  #Starts with "/"

x = "//a[@data-tooltip-content='" + app_name +"']"
print(x)

from selenium import webdriver  #importing the webdriver from selenium package
from selenium.webdriver.common.keys import Keys #importing KEYS

import time #to give time for the page to load up to do the next work

#accessing the webdriver chrome.. in paranthesis mention the path of chrome.exe
#Download the chrome.exe
driver = webdriver.Chrome(driver_path)

#Logging into Facebook
driver.get('https://developers.facebook.com/apps/')
driver.find_element_by_name("email").send_keys(username)
driver.find_element_by_name("pass").send_keys(password)
driver.find_element_by_name("login").submit()

time.sleep(1)

#Navigate to the Tools page of Marketing API
driver.find_element_by_xpath(x).click()
driver.find_element_by_xpath('//*[@id="developer_app_content_root"]/nav/div/div[2]/a/i').click()


driver.find_element_by_xpath('//*[@id="developer_app_content_root"]/nav/div/div[3]/div[2]/div/a').click()
#driver.find_element_by_xpath('//*[@id="developer_app_content_root"]/nav/div/div[3]/div/div/a/div[2]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="developer_app_content_root"]/nav/div/div[3]/div/div/div/span[3]/div/a').click()

#clicking all the checkboxes

driver.find_element_by_xpath('//*[@id="u_0_15"]/tbody/tr[1]/td[1]/div/label[1]').click()
driver.find_element_by_xpath('//*[@id="u_0_15"]/tbody/tr[1]/td[2]/div/label[1]').click()
driver.find_element_by_xpath('//*[@id="u_0_15"]/tbody/tr[1]/td[3]/div/label[1]').click()
driver.find_element_by_xpath('//*[@id="u_0_15"]/tbody/tr[2]/td[1]/div/label[1]').click()

driver.find_element_by_xpath('//*[@id="u_0_16"]').click()

'''
driver.find_element_by_xpath('//*[@id="u_0_14"]/tbody/tr[1]/td[1]/div/label[1]').click()
driver.find_element_by_xpath('//*[@id="u_0_14"]/tbody/tr[1]/td[2]/div/label[1]').click()
driver.find_element_by_xpath('//*[@id="u_0_14"]/tbody/tr[1]/td[3]/div/label[1]').click()
driver.find_element_by_xpath('//*[@id="u_0_14"]/tbody/tr[2]/td[1]/div/label[1]').click()

driver.find_element_by_xpath('//*[@id="u_0_15"]').click()
'''

#copying the token

time.sleep(1)
t = driver.find_element_by_xpath('//*[@id="u_0_z"]/div/div[1]/span')
print(t.text)
code = str(t.text)

'''
time.sleep(1)
t = driver.find_element_by_xpath('//*[@id="u_0_y"]/div/div[1]/span')
print(t.text)
code = str(t.text)
'''

#Clicking Tools and going to Access Token Debuger and clicking the extend token button
driver.find_element_by_xpath('//*[@href="/tools/"]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="u_0_4"]/div[1]/div[3]/a').click()

driver.find_element_by_xpath('//*[@id="u_0_8"]/div[1]/input[1]').clear()
driver.find_element_by_xpath('//*[@id="u_0_8"]/div[1]/input[1]').send_keys(code)
driver.find_element_by_xpath('//*[@id="u_0_8"]/div/button').click()
time.sleep(1)

#Copying the extended code
'''
driver.find_element_by_xpath('//*[@id="u_0_9"]/div/button').click()
time.sleep(1)
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
e=driver.find_element_by_xpath('//*[@id="u_0_9"]/div/div/div/div/div[2]/span/pre/div/div[1]')
print(e.text)
code = str(e.text)
print(code)
#Hitting the debug button
driver.find_element_by_xpath('//*[@id="u_0_9"]/div/div/div/div/div[2]/span/pre/div/div[2]/a').click()
'''

time.sleep(3)
#Creating a new tab 
driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't') 
driver.get('https://www.facebook.com/business/')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="u_0_cu"]').click()
time.sleep(3)

#now reached the desired page ... Getting the URL of that page
url = driver.current_url
print(url)

#printing out adid
ADID = ''
leng = len(url)
numbers = ['1','2','3','4','5','6','7','8','9','0']
i = 0
while i<leng:
    if url[i] in numbers:
        ADID += url[i]
    i += 1

print(ADID)

f = open("CREDENTIAL", "w")
x = code + "\n"
f.write(x)
f.write(ADID)
f.close()
