from random import randint
import re
import unittest

from mock import Mock

from webelement_highlighter import WebElementHighlighter


class TestWebElementHighlighter(unittest.TestCase):
    def setUp(self):
        driver = Mock()

        def handle_property_change(js, webelement):
            style = re.compile(r".*\'(?P<style>.*)\'").match(js).groupdict().get('style')
            if 'backgroundColor' in js:
                webelement.properties['background-color'] = style
            elif 'border' in js:
                webelement.properties['border'] = style

        driver.execute_script = handle_property_change

        self.wh = WebElementHighlighter(driver=driver)

        self.webelement = Mock()
        self.webelement.id = randint(111111, 999999)
        self.webelement.value_of_css_property = lambda property: self.webelement.properties.get(property)

    def test_background_change(self):
        self.webelement.properties = {'background-color': 'white'}

        self.wh.change_background_color(webelement=self.webelement, background_color='yellow')

        self.assertEqual('yellow', self.webelement.value_of_css_property('background-color'))

    def test_background_change_to_default_value(self):
        self.webelement.properties = {'background-color': 'white'}

        self.wh.change_background_color(webelement=self.webelement, background_color='yellow')
        self.wh.change_to_default_background_color(webelement=self.webelement)

        self.assertEqual('white', self.webelement.value_of_css_property('background-color'))

    def test_border_change(self):
        self.webelement.properties = {'border': 'white'}

        self.wh.change_border_color(webelement=self.webelement, border_color='yellow')

        self.assertIn('yellow', self.webelement.value_of_css_property('border'))

    def test_border_change_to_default_value(self):
        self.webelement.properties = {'border': 'white'}

        self.wh.change_border_color(webelement=self.webelement, border_color='pink')
        self.wh.change_to_default_border_color(webelement=self.webelement)

        self.assertIn('white', self.webelement.value_of_css_property('border'))
