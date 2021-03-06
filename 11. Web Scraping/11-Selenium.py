# Controlling the browser with the Selenium module
from selenium import webdriver
browser = webdriver.Firefox()
type(browser)
browser.get('http://inventwithpython.com')

# Finding elements with Selenium
browser.find_element_by_class_name(name)
browser.find_elements_by_class_name(name)

browser.find_element_by_css_selector(selector)
browser.find_elements_by_css_selector(selector)

browser.find_element_by_id(id)
browser.find_elements_by_id(id)

browser.find_element_by_link_text(text)
browser.find_elements_by_link_text(text)

browser.find_element_by_partial_link_text(text)
browser.find_elements_by_partial_link_text(text)

browser.find_element_by_name(name)
browser.find_elements_by_name(name)

# Only method that is NOT case sensitive
browser.find_element_by_tag_name(name)
browser.find_elements_by_tag_name(name)

# Methods
tag_name
The tag name, such as  'a' for an  <a> element

get_attribute(name)
The value for the element’s  name attribute

text
The text within the element, such as  'hello' in <span>hello</span>

clear()
For text field or text area elements, clears the text typed into it

is_displayed()
Returns  True if the element is visible; otherwise returns False

is_enabled()
For input elements, returns True if the element is enabled;
otherwise False

is_selected()
For checkbox or radio button elements, returns  True if the element is selected;
otherwise False

location
A dictionary with keys  'x' and  'y' for the position of the element in the page

# Using the click() method to simulate a mouse
# First we find the element, then we "click" it

linkElem = browser.find_element_by_link_text('Example text')
type(linkElem)
linkElem.click()

# Filling out and submitting forms
# Usually it involves finding the  <input> or  <textarea> elements
# and calling the send_keys() methods

# Example with email

emailELem = browser.find_element_by_id('login-username')
emailELem.send_keys('just_an_email@email.com')
passwordElem = browser.find_elements_by_id('login-passwd')
passwordElem.send_keys('BesT_PasSwORd')
passwordElem.submit()

# Selenium can also simulate other keyboard keys which are not strings
# e.g. arrow keys using the selenium.webdriver.common.keys module

# Common browser buttons
browser.back()
browser.forward()
browser.refresh()
browser.quit()
