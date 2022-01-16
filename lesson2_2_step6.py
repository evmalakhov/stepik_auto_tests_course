from selenium import webdriver
import time 
import math


link = "http://suninjuly.github.io/execute_script.html"


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)

    
    answer = browser.find_element_by_css_selector("#answer")
    answer.send_keys(str(y))

    robot_ia = browser.find_element_by_css_selector("#robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot_ia)
    robot_ia.click()

    robot = browser.find_element_by_css_selector("#robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot)
    robot.click()

    time.sleep(0.5)

    submit = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
    submit.click()


finally:
    time.sleep(30)
    browser.quit()


