from webelement_highlighter import WebElementHighlighter
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/js/default.asp")

wh = WebElementHighlighter(driver)

we = driver.find_element_by_id("topnavbtn_references")
wes = driver.find_elements_by_class_name("w3-col")

wh.highlight_element(we)
wh.highlight_elements(wes, stop=True)
