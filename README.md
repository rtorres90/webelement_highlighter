WebElementHighlighter
================
[![Build Status](https://travis-ci.org/rtorres90/webelement_highlighter.svg?branch=master)](https://travis-ci.org/rtorres90/webelement_highlighter)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

WebElementHighlighter is library to highlight WebElements.

How to use.

```python
from webelement_highlighter import WebElementHighlighter
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.cl")

wh = WebElementHighlighter(driver)

we = driver.find_element_by_id("lst-ib")
wes = driver.find_elements_by_class_name("gb_P")

wh.make_it_blink(we)
wh.make_them_blink(wes, times=200)
```

How to install.
---------------

```
pip install webelement_highlighter
```
