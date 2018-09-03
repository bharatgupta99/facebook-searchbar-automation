from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

 
usr=input('enter email')
pwd=input('enter password')
 
driver = webdriver.Chrome()
driver.get('https://www.facebook.com/')
print ("Opened facebook")
sleep(1)
 
username_box = driver.find_element_by_id('email')
username_box.send_keys(usr)
print ("Email Id entered")
sleep(1)
 
password_box = driver.find_element_by_id('pass')
password_box.send_keys(pwd)
print ("Password entered")
 
login_box = driver.find_element_by_id('loginbutton')
login_box.click()

query = input('enter your query ')

search_box = driver.find_element_by_xpath("//input[@name='q']")
search_box.send_keys(query)
search_box.send_keys(Keys.RETURN)
sleep(1)


print ("Done")
input('Press anything to quit')
driver.quit()
print("Finished")