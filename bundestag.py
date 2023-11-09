from selenium import webdriver
import time

# Specify the path to your WebDriver
driver = webdriver.Chrome()

# Navigate to the initial page with the list view
driver.get('https://www.bundestag.de/en/members')

# Locate and click the "list view" button
# Locate and click the "list view" button
list_view_button = driver.find_element('css selector', 'a.bt-link-list')
list_view_button.click()


# Wait for the page to load (you can adjust the time as needed)
driver.implicitly_wait(10)

# # Locate and extract member information
# members = driver.find_elements('css selector','div.bt-teaser-person')
# print(members)
import re

# Get the page source
page_source = driver.page_source

# Use regular expressions to find links with a specific pattern
pattern = r'<a title=".+?" href="(.+?)"'
links = re.findall(pattern, page_source)

# Print the links
for link in links:
    print(link)

# for member in members:
#     time.sleep(5) 
#     name = member.text
#     link = member.get_attribute('href')

#     # Navigate to the member's personal page
#     driver.get(link)

#     # Extract the member's email and social media links here

#     # Go back to the list view page for the next member
#     driver.back()

# Close the browser
driver.quit()
