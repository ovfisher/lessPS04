from selenium import webdriver
import time
#Если Chrome
browser = webdriver.Chrome()
browser.get("https://en.wikipedia.org/wiki/Document_Object_Model")
#В кавычках указываем URL сайта, на который нам нужно зайти
#time.sleep(10)
#Задержка в 10 секунд
browser.save_screenshot("dom.png")
time.sleep(5)
browser.get("https://ru.wikipedia.org/wiki/Selenium")
browser.save_screenshot("selenium.png")
time.sleep(3)
browser.refresh()

#browser.quit()