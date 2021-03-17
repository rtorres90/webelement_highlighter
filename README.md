WebElementHighlighter
=====================
[![Python linting](https://github.com/rtorres90/webelement_highlighter/actions/workflows/python-package.yml/badge.svg?branch=master)](https://github.com/rtorres90/webelement_highlighter/actions/workflows/python-package.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

WebElementHighlighter is library to highlight WebElements. It was made to use it on automated tests, specially when you want to highlight errors on a webpage.

Features.
---------

* You can make WebElements blink changing their background and border styles.
* You can change the background style of WebElements.
* You can change the border styles of WebElements.


How to use.
-----------
```python
from webelement_highlighter import WebElementHighlighter
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/js/default.asp")

wh = WebElementHighlighter(driver)

we = driver.find_element_by_id("topnavbtn_references")
wes = driver.find_elements_by_class_name("w3-col")

wh.make_it_blink(we)
wh.make_them_blink(wes, times=20)

wh.highlight_element(we)
wh.highlight_elements(wes, stop=True)
```

How to install.
---------------

```
pip install webelement_highlighter
```
