import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# Setup Chrome WebDriver with default options
driver = webdriver.Chrome()

# Open the Demoblaze homepage
driver.get("https://www.demoblaze.com/index.html")
time.sleep(2)

# Click on the 'Laptops' section to view the laptop listings
laptops_button = driver.find_element(By.LINK_TEXT, "Laptops")
laptops_button.click()
time.sleep(5)  # Wait for the page to load

# Store the extracted laptop data in a list
laptops_data = []


# Function to scrape data from a single page
def scrape_page():
    # Get the page source after loading
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # Find all laptop cards
    laptop_cards = soup.find_all("div", class_="col-lg-4 col-md-6 mb-4")

    # Extract laptop data (name, price, description)
    page_laptops_data = []
    for card in laptop_cards:
        name = card.find("h4", class_="card-title").text.strip()
        price = card.find("h5").text.strip()
        description = card.find("p", class_="card-text").text.strip()

        laptop = {"name": name, "price": price, "description": description}
        page_laptops_data.append(laptop)

    # Return the data for the current page
    return page_laptops_data


# Scrape the first page
laptops_data.extend(scrape_page())

# Click the next page button and scrape the next page
next_button = driver.find_element(By.ID, "next2")
next_button.click()
time.sleep(5)  # Wait for the page to load

# Scrape the next page and add to the data list
laptops_data.extend(scrape_page())

# Save the scraped data from the next page to a JSON file
with open("laptops_data.json", "w", encoding="utf-8") as json_file:
    json.dump(laptops_data, json_file, indent=4, ensure_ascii=False)

# Close the driver
driver.quit()
