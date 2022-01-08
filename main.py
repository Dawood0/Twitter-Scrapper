import csv
from getpass import getpass
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome,Firefox

driver=Chrome(executable_path='chromedriver.exe')
# driver=Firefox(executable_path='geckodriver.exe')
driver.get('https://www.twitter.com/login')
username=driver.find_element_by_xpath('//input[@name="text"]')
print("##########################",username)

# driver.quit()