from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = ''
driver = webdriver.Chrome()
driver.get(url)

element_founder = driver.find_element_by_name('q')
element_founder.send_keys('selenium')
element_founder.send_keys(Keys.RETURN)

results = driver.find_elements_by_css_selector('h3 > a')
for result in results:
    print(result.text)
