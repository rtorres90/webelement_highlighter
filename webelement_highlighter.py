import time


class WebElementHighlighter(object):
    BORDER_COLOR_JS = "arguments[0].style.border = '%s %s %s';"
    ONE_PARAMETER_BORDER_COLOR_JS = "arguments[0].style.border = '%s';"
    BACKGROUND_COLOR_JS = "arguments[0].style.backgroundColor = '%s';"

    def __init__(self, driver):
        self.driver = driver
        self._previous_border_color = ""
        self._previous_background_color = ""
        self._changed_elements = []
        # TODO: store changed elements by this lib.

    @property
    def previous_border_color(self):
        return self._previous_border_color

    @previous_border_color.setter
    def previous_border_color(self, border_color):
        self._previous_border_color = border_color

    @property
    def previous_background_color(self):
        return self._previous_background_color

    @previous_background_color.setter
    def previous_background_color(self, background_color):
        self._previous_background_color = background_color

    def change_border_color(self, webelement, border_width="2px", border_style="solid", border_color="red"):
        self.previous_border_color = webelement.value_of_css_property('border')
        self.driver.execute_script(self.BORDER_COLOR_JS % (border_width, border_style, border_color), webelement)

    def change_border_color_by_complete_css_value(self, webelement, border_style="2px"):
        self.previous_border_color = webelement.value_of_css_property('border')
        self.driver.execute_script(self.ONE_PARAMETER_BORDER_COLOR_JS % border_style, webelement)

    def change_to_default_border_color(self, webelement):
        self.change_border_color_by_complete_css_value(webelement, self._previous_border_color)

    def change_background_color(self, webelement, background_color="yellow"):
        self._previous_background_color = webelement.value_of_css_property("background-color")
        self.driver.execute_script(self.BACKGROUND_COLOR_JS % background_color, webelement)

    def change_to_default_background_color(self, webelement):
        self.change_background_color(webelement, self._previous_background_color)

    def make_it_blink(self, webelement, times=10, interval=50):
        for _ in xrange(times):
            self.change_background_color(webelement)
            self.change_border_color(webelement)
            time.sleep(interval / 1000.0)

            self.change_to_default_background_color(webelement)
            self.change_to_default_border_color(webelement)
            time.sleep(interval / 1000.0)

    def make_them_blink(self, webelements, times=10, interval=50):
        for _ in xrange(times):
            for webelement in webelements:
                self.change_background_color(webelement)
                self.change_border_color(webelement)
            time.sleep(interval / 1000.0)

            for webelement in webelements:
                self.change_background_color(webelement)
                self.change_border_color(webelement)
            time.sleep(interval / 1000.0)