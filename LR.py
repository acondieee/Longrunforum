from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# Define your forum credentials and post content
username = "andrea.m.condie@gmail.com"
password = "Hillhouse97*"
post_title = "Weekly Long Run Planning"
post_content = """
Post your weekend long run plans in the comments, with the usual info about where/when you'll meet, distance to be run, and anticipated pace/workouts!
"""

# Define the URLs
main_url = "https://www.newhavenroadrunners.com"  # Main URL
forum_url = "https://www.newhavenroadrunners.com/forum/long-run-planning"  # Post page URL

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--incognito")  # Enable incognito mode

# Specify the path to the ChromeDriver executable using the Service class
chrome_service = Service("C:\\Webdriver\\chromedriver-win64\\chromedriver.exe")

# Initialize the WebDriver with Chrome options and service
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

try:
    # Open the main page
    print("Opening the main page...")
    driver.get(main_url)

    # Step 1: Wait for the "Log In" button to appear and click it using JavaScript to avoid any click issues
    print("Waiting for 'Log In' button...")
    log_in_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//button//span[text()='Log In']"))
    )
    driver.execute_script("arguments[0].click();", log_in_button)
    print("Clicked 'Log In' button")
    time.sleep(2)  # Briefly wait for the modal to load

    # Step 2: Wait for the modal to fully load
    print("Waiting for the modal to load...")
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Sign Up')]"))
    )
    print("Modal loaded successfully.")

    # Step 3: Scroll down using the down arrow key to bring "Already a member? Log In" link into view
    print("Scrolling to find 'Already a member? Log In' link...")
    body_element = driver.find_element(By.TAG_NAME, "body")
    for _ in range(20):  # Adjust the range if needed for more scrolling
        body_element.send_keys(Keys.DOWN)
        time.sleep(0.2)  # Adjust delay as needed

    # Step 4: Wait for "Already a member? Log In" link to appear, then click it
    print("Waiting for 'Already a member? Log In' link...")
    already_member_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Already a member? Log In')]"))
    )
    driver.execute_script("arguments[0].click();", already_member_link)
    print("Clicked 'Already a member? Log In' link")
    time.sleep(2)  # Wait for the login form to appear

    # Step 5: Enter the login credentials
    print("Entering login credentials...")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='emailAuth']"))).send_keys(username)
    driver.find_element(By.CSS_SELECTOR, "input[data-testid='passwordAuth']").send_keys(password)

    # Step 6: Click the login button
    print("Clicking login button...")
    login_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='buttonElement']")
    driver.execute_script("arguments[0].click();", login_button)
    time.sleep(3)  # Wait for login to complete

    # Step 7: Navigate to the forum posting page
    print("Navigating to forum posting page...")
    driver.get(forum_url)
    time.sleep(3)  # Wait for the page to load

    # Step 8: Enter the title for the post
    print("Entering post title...")
    driver.find_element(By.CSS_SELECTOR, "[placeholder='Give this post a title']").send_keys(post_title)

    # Step 9: Enter the post content
    print("Entering post content...")
    driver.find_element(By.CSS_SELECTOR, "[placeholder='Write your post here. Add photos, videos and more to get your message across.']").send_keys(post_content)

    # Step 10: Click the publish button
    print("Clicking publish button...")
    driver.find_element(By.XPATH, "//button[contains(text(), 'Publish')]").click()

    print("Post submitted successfully!")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()
