from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


# Specify the path to your WebDriver
driver = webdriver.Chrome()

# Navigate to the initial page with the list view
driver.get('https://www.bundestag.de/en/members')

# Locate and click the "list view" button
list_view_button = driver.find_element('css selector', 'a.bt-link-list')
list_view_button.click()



# Wait for the page to load (you can adjust the time as needed)
driver.implicitly_wait(10)

# Get the page source
page_source = driver.page_source

# Scroll down the page to load more members
body = driver.find_element(By.TAG_NAME, 'body')


for _ in range(15):  # You may need to adjust the number of scrolls to load all members
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(2)  # Add a delay to ensure content is loaded

# Locate and extract member information
members = driver.find_elements('css selector', 'h3')  # Select h3 elements containing member names
for member in members:
    link = member.find_element(By.XPATH, './ancestor::a').get_attribute('href')
    print(link)

driver.quit()
