import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
import sys


def test_scores_service(app_url):
    # Set up the Chrome driver
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome()

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
