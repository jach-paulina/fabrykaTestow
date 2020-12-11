from selenium import webdriver
import time
from Screenshot import Screenshot_Clipping
from selenium.webdriver.common.action_chains import ActionChains
import webdriver_manager

driver = webdriver.Chrome()

def auto():

    driver.get('https://fabrykatestow.pl/')
    driver.maximize_window()
    driver.find_element_by_css_selector('#menu-item-622 > a').click()
    time.sleep(2)
    driver.find_element_by_class_name('elementor-button-text').click()
    time.sleep(2)
    target = driver.find_element_by_xpath('//*[@id="content"]/div/div/div/div/div/div/div/section[15]/div/div/div/div/div/div/div/h2')
    target.location_once_scrolled_into_view


auto()
time.sleep(5)
driver.get_screenshot_as_file("shot.png")
driver.quit()