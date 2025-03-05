from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

# Input username between quotes
username = ''

# Options so chrome doesn't automatically close
chrome_options = Options() 
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# Get Game Report
driver.get("https://chess.wintrcat.uk/")

# Click dropdown to open dropdown
dropdown_btn = driver.find_element(By.ID, 'load-type-dropdown')
dropdown_btn.click()

# Use arrow keys to select chesscom to trigger verify/arrow button
dropdown_btn.send_keys(Keys.ARROW_DOWN)
dropdown_btn.send_keys(Keys.RETURN)

# Input username into textarea
textarea = driver.find_element(By.ID, 'chess-site-username')
textarea.clear()
textarea.send_keys(username) 

# Click the arrow button that appears
username_verify_btn = driver.find_element(By.CLASS_NAME, 'usernameVerifyBtnIcon')
username_verify_btn.click()

# Click latest game
games_listings = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, 'game-listing'))
)
if games_listings:
    games_listings[0].click()

# Click analyze
analyze_btn = driver.find_element(By.ID, 'review-button')
analyze_btn.click()

# Click reCAPTCHA
WebDriverWait(driver, 60).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[title='reCAPTCHA']")))
WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.recaptcha-checkbox-border"))).click()