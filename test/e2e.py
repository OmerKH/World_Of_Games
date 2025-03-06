import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import sys


# Test the web service by checking if the score is a number between 1 and 1000
# :param app_url: URL of the web service
# :return: True if score is valid, False otherwise


# def setup_webdriver_options():
#     options = webdriver.ChromeOptions()
#     chromedriver_autoinstaller.install()  # Install ChromeDriver if not found
#     options.add_argument('--headless')  # Run in headless mode
#     options.add_argument('--no-sandbox')
#     options.add_argument('--disable-dev-shm-usage')
#     return options


def test_scores_service(app_url):
    # Set up the Chrome driver
    chromedriver_autoinstaller.install()
    chrome_options = Options()
    chrome_options.add_argument('--headless')

    driver = webdriver.Chrome(options=chrome_options)

    # Open the application URL
    driver.get(app_url)

    # Check if the score element is found
    score_element = driver.find_element(By.ID, 'score')
    if score_element:
        score = int(score_element.text)
        # Check if the score is between 1 and 1000
        if 1 <= score <= 1000:
            return True
        else:
            return False
    else:
        return False
    driver.quit()


def main_function():
    """
    Main function to run the test and return appropriate exit code
    :return: 0 if test passes, -1 if test fails
    """
    app_url = "http://localhost:5000"
    if test_scores_service(app_url):
        print("Test passed!")
        return 0
    else:
        print("Test failed!")
        return -1


if __name__ == "__main__":
    sys.exit(main_function())
