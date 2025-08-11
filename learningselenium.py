from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://webflow.com/made-in-webflow/dropdown")
assert "Best" in driver.title
elem = driver.find_element(By.ID, "sort")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()

