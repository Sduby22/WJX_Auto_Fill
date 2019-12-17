# Composer: HittheWall(Sduby22)
# Friend me on Steam!!!
# Working on Python3+

import time
import ujson
import os
from os import path
from selenium import webdriver
from selenium.webdriver.support.ui import Select


# to figure out what's the question asking about
def define_question_kind(question, config):
    content, type_ = '', ''
    titles = question.find_element_by_class_name('div_title_question')
    if titles:
        titles = titles.text
        for key in config:
            value = config[key]
            if any(key_word in titles for key_word in value['key_words']):
                content = key
                break
    if question.find_elements_by_css_selector('textarea'):
        type_ = 'textarea'
    if question.find_elements_by_class_name('ulradiocheck'):
        type_ = 'ulradiocheck'
    if question.find_elements_by_tag_name('tbody'):
        type_ = 'table'
    if question.find_elements_by_css_selector('select'):
        type_ = 'select'
    return content, type_


# Input the info accordingly
def auto_input(question, method, config):
    if method[1] == 'textarea':
        textarea = question.find_element_by_css_selector('textarea')
        textarea.clear()
        textarea.send_keys(config[method[0]]['input'])
    if method[1] == 'ulradiocheck':
        label = question.find_element_by_xpath(
            '//li[contains(label,"{0}")]'.format(config[method[0]]['input']))
        label.click()
    if method[1] == 'select':
        s1 = Select(question.find_element_by_css_selector('select'))
        for option in s1.options:
            if config[method[0]]['input'] in option.text:
                s1.select_by_visible_text(option.text)


# main
if __name__ == "__main__":
    # Read config
    config = {}
    current_path = path.dirname(__file__)
    with open(current_path+'/config.json', "r", encoding='utf8') as f:
        config = ujson.load(f)

    url = input()

    # Open Website
    driver = webdriver.Chrome()
    driver.get(url)

    # Locate Questions
    questions = driver.find_elements_by_class_name('div_question')
    # if question list is empty, it means the sheet hasn't been started yet.
    while not questions:
        time.sleep(0.1)
        driver.get(url)
        questions = driver.find_elements_by_class_name('div_question')
    for question in questions:
        method = define_question_kind(question, config)
        print(method)

        if method[0] and method[1]:  # if the content and type of the question is correctly recognized
            auto_input(question, method, config)

    # Click "submit" button
    button = driver.find_element_by_id('submit_button')
    button.click()

    # If not every single blank is filled, then click "confirm" automatically.
    # The page will automatically go up to the first unfilled blank.
    alert = driver.switch_to.alert
    alert.accept()
