from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time

# Initialize Chrome options
options = ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")  
options.add_argument("--disable-gpu") 
options.add_argument("--disable-dev-shm-usage") 
options.add_argument("--window-size=2560,1440")
options.add_argument("--remote-debugging-port=9222") 

# Initialize the driver with the options
driver = webdriver.Chrome(options=options)

try:
    # Open the SauceDemo login page
    driver.get("https://www.saucedemo.com/")

    # Locate the username field, enter the username
    driver.find_element(By.ID, "user-name").send_keys("standard_user")

    # Locate the password field, enter the password
    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    # Locate and click the login button
    driver.find_element(By.ID, "login-button").click()

    # Wait for the next page to load and verify the inventory page is displayed
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
    )

    # If no exceptions were thrown, login was successful
    print("Login successful.")

    driver.save_screenshot("results/login_successful.png")

    # Add items to the cart
    items_added = []
    for i in range(1, 7):
        items = driver.find_elements(By.CLASS_NAME, "btn_inventory")
        print(len(items))
        item=items[i-1]
        items_added.append(item.get_attribute("id").replace('add-to-cart-', ''))
        item.click()
        time.sleep(1)  # Sleep to ensure the item is added before proceeding
    driver.save_screenshot("results/add_cart.png")
    print(f"User 'standard_user' logged in and added items: {items_added}")

    # Remove 4 items from the cart
    items_removed = []
    for i in range(1, 4):
        remove_button = driver.find_element(By.ID, f"remove-{items_added[i]}")
        remove_button.click()
        items_removed.append(f"remove-{items_added[i]}")
        time.sleep(1)  # Sleep to ensure the item is removed before proceeding
    driver.save_screenshot("results/remove_cart.png")

    print(f"Items removed from cart: {items_removed}")

    # Take a screenshot
except Exception as e:
    print(f"Test failed: {e}")

finally:
    # Close the browser window
    driver.quit()
