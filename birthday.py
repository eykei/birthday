'''
description: Automatically posts 'happy birthday' to friend's wall when it is their birthday

usage: In powershell, navigate to file. then type:
py -3 birthday.py <email> <password>
* Warning must use old version of Firefox 52.02 and geckodriver.exe must be on path

status: working

todo: Make work with chrome
'''


from selenium import webdriver
import time, sys


if len(sys.argv) != 3:
    raise Exception('Not Enough / Too Many Input Arguments.\n Usage: py -3 birthday.py <email> <password>')

fp = webdriver.FirefoxProfile()
fp.set_preference("dom.webnotifications.enabled", False) # suppress web notifications popup asking for permissions
browser = webdriver.Firefox(fp)

browser.get('https://www.facebook.com/')
time.sleep(1)

email=sys.argv[1]
password=sys.argv[2]

print('Logging in...')
userElem=browser.find_element_by_name('email')
userElem.send_keys(email)
passElem=browser.find_element_by_name('pass')
passElem.send_keys(password)
passElem.submit()
time.sleep(1)

browser.get('https://www.facebook.com/events/birthdays')
time.sleep(1)

print('Locating birthdays...')
nameList = []
nameElems = browser.find_elements_by_css_selector("div._tzn a")

for nameElem in nameElems:
    firstName=nameElem.text.split()[0]
    nameList.append(firstName)

textBoxes = browser.find_elements_by_class_name('enter_submit')

print('Writing Message...')
for i in range(len(textBoxes)):
    textBoxes[i].click()
    textBoxes[i].send_keys('Happy Birthday, %s!' % nameList[i])
    textBoxes[i].submit()

print('Done')