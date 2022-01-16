from selenium import webdriver
import time 
import math


link = "http://suninjuly.github.io/get_attribute.html"


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)


    people_radio = browser.find_element_by_id("peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"

    robots_radio = browser.find_element_by_id("robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    print("value of robots radio: ", robots_checked)
    assert robots_checked is None

    x_element_hidden = browser.find_element_by_css_selector("#treasure")
    x_element = x_element_hidden.get_attribute("valuex")
    x = x_element
    y = calc(x)

    
    answer = browser.find_element_by_css_selector("#answer")
    answer.send_keys(str(y))

    robot_ia = browser.find_element_by_css_selector("#robotCheckbox")
    robot_ia.click()

    robot = browser.find_element_by_css_selector("#robotsRule")
    robot.click()

    time.sleep(0.5)

    submit = browser.find_element_by_css_selector("button.btn")
    submit.click()


finally:
    time.sleep(30)
    browser.quit()


