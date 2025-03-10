import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def test_scores_service(app_url):
    # Set up the Chrome driver with appropriate options
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    # Use the pre-installed ChromeDriver
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Open the application URL
        driver.get(app_url)

        # Check if the score element is found
        score_element = driver.find_element(By.ID, 'score')
        if score_element:
            score = int(score_element.text)
            # Check if the score is between 1 and 1000
            return 1 <= score <= 1000
        return False
    finally:
        driver.quit()


def main_function():

    app_url = "http://localhost:8777"
    if test_scores_service(app_url):
        print("Test passed!")
        return 0
    else:
        print("Test failed!")
        return -1


if __name__ == "__main__":
    sys.exit(main_function())
