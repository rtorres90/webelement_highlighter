from webelement_highlighter import WebElementHighlighter
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/js/default.asp")

wh = WebElementHighlighter(driver)

we = driver.find_element_by_id("topnavbtn_references")
wes = driver.find_elements_by_class_name("w3-col")

wh.make_it_blink(we)
wh.make_them_blink(wes, times=10)
