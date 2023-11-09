from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
import time
import csv

# Specify the path to your WebDriver
driver = webdriver.Chrome()

# Navigate to the initial page with the list view
driver.get('https://www.bundestag.de/en/members')

# Locate and click the "list view" button
list_view_button = driver.find_element(By.CSS_SELECTOR, 'a.bt-link-list')
list_view_button.click()

# Wait for the page to load (you can adjust the time as needed)
driver.implicitly_wait(10)

# Lists to store data
name_list = []
email_list = []
social_media_list = []

# Scroll down the page to load more members
body = driver.find_element(By.TAG_NAME, 'body')
for _ in range(15):  # You may need to adjust the number of scrolls to load all members
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(2)  # Add a delay to ensure content is loaded

# Locate and extract member information
members = driver.find_elements(By.CSS_SELECTOR, 'h3')  # Select h3 elements containing member names
#print(members)

for member in members:
    time.sleep(2)

    link = member.find_element(By.XPATH, './ancestor::a').get_attribute('href')
    print(link)
    driver.get(link)


    try:
        # Extract the name
        name_element = driver.find_element(By.CSS_SELECTOR, '.bt-biografie-name h3')
        name = name_element.text.strip()
        print("Name:", name)
    
        # Locate the div containing social media links
        div_element = driver.find_element(By.XPATH, '//div[h5[text()="Profile im Internet"]]')

        # Find all the li elements within the div
        li_elements = div_element.find_elements(By.CSS_SELECTOR, 'ul.bt-linkliste li')

        # Extract social media links and titles
        social_media_links = []
        for li_element in li_elements:
            a_element = li_element.find_element(By.CSS_SELECTOR, 'a')
            title = a_element.get_attribute('title')
            link = a_element.get_attribute('href')
            social_media_links.append((title, link))
            print(f"{title}: {link}")

    

        # Extract email contact link
        email_element = driver.find_element(By.CSS_SELECTOR, 'span a[title="Kontakt"]')
        email_link = email_element.get_attribute('href')
        email_list.append(email_link)
        print("Email Contact Link:", email_link)

    except StaleElementReferenceException:
        print("Element became stale. Retrying...")
        continue

# Close the browser
driver.quit()

# Create a list of tuples containing email addresses and full names
data = [(name, email, social_media) for name, email, social_media in zip(name_list, email_list, social_media_list)]

# Specify the CSV file name
csv_file = './Bundestag/parliamentarians.csv'

# Write the data to the CSV file
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Email', 'Social Media'])  # Write header row
    writer.writerows(data)  # Write email addresses and full names
