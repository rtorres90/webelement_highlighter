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

    def is_the_element_already_stored(self, element_id):
        for element in self._changed_elements:
            if element_id == element.get('element_id'):
                return True
        return False

    def is_the_property_already_set(self, element_id, property):
        return True if self.get_property_value(element_id, property) else False

    def get_element_from_changed_elements(self, element_id):
        if not self.is_the_element_already_stored(element_id):
            return None
        return [element for element in self._changed_elements if element_id == element.get('element_id')][0]

    def get_properties_from_element(self, element_id):
        return self.get_element_from_changed_elements(element_id).get('properties')

    def change_property_value(self, element_id, property, value):
        for prop in self.get_properties_from_element(element_id):
            if prop.get('property') == property:
                prop['value'] = value

    def get_property_value(self, element_id, property):
        try:
            return [prop for prop in self.get_properties_from_element(element_id) if
                    property == prop.get('property')][0].get('value')
        except:
            return None

    def store_changed_elements(self, element_id, property, value):
        element = self.get_element_from_changed_elements(element_id)
        if element:
            if self.is_the_property_already_set(element_id, property):
                self.change_property_value(element_id, property, value)
            else:
                element.get('properties').append({'property': property, 'value': value})
        else:
            self._changed_elements.append(
                {'element_id': element_id, 'properties': [{'property': property, 'value': value}]})

    def change_border_color_to_elements(self, webelements, border_width="2px", border_style="solid",
                                        border_color="red"):
        if len(webelements):
            self.change_border_color(webelements[-1], border_width, border_style, border_color)
            self.change_border_color_to_elements(webelements[:-1], border_width, border_style, border_color)

    def change_border_color(self, webelement, border_width="2px", border_style="solid", border_color="red"):
        self.store_changed_elements(webelement.id, 'border', webelement.value_of_css_property('border'))
        self.driver.execute_script(self.BORDER_COLOR_JS % (border_width, border_style, border_color), webelement)

    def change_border_color_by_complete_css_value(self, webelement, border_style="2px"):
        self.store_changed_elements(webelement.id, 'border', webelement.value_of_css_property('border'))
        self.driver.execute_script(self.ONE_PARAMETER_BORDER_COLOR_JS % border_style, webelement)

    def change_elements_to_default_border_color(self, webelements):
        if len(webelements):
            self.change_to_default_border_color(webelements[-1])
            self.change_elements_to_default_border_color(webelements[:-1])

    def change_to_default_border_color(self, webelement):
        self.change_border_color_by_complete_css_value(webelement, self.get_property_value(webelement.id, 'border'))

    def change_background_color_to_elements(self, webelements, background_color="yellow"):
        if len(webelements):
            self.change_background_color(webelements[-1], background_color)
            self.change_background_color_to_elements(webelements[:-1], background_color)

    def change_background_color(self, webelement, background_color="yellow"):
        self.store_changed_elements(webelement.id, 'background-color',
                                    webelement.value_of_css_property('background-color'))
        self.driver.execute_script(self.BACKGROUND_COLOR_JS % background_color, webelement)

    def change_elements_to_default_background_color(self, webelements):
        if len(webelements):
            self.change_to_default_background_color(webelements[-1])
            self.change_elements_to_default_background_color(webelements[:-1])

    def change_to_default_background_color(self, webelement):
        self.change_background_color(webelement, self.get_property_value(webelement.id, 'background-color'))

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
            self.change_background_color_to_elements(webelements)
            self.change_border_color_to_elements(webelements)
            time.sleep(interval / 1000.0)

            self.change_elements_to_default_background_color(webelements)
            self.change_elements_to_default_border_color(webelements)
            time.sleep(interval / 1000.0)
