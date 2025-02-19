import sys
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_scores_service(app_url):
    """
    Test the web service by checking if the score is a number between 1 and 1000.
    :param app_url: The URL of the web application
    :return: True if the score is valid, False otherwise
    """
    driver = webdriver.Chrome()
    driver.get(app_url)

    score_elements = driver.find_elements(By.ID, "score")
    if not score_elements:
        driver.quit()
        return False

    score_element = score_elements[0]
    score_text = score_element.text.strip()

    if not score_text.isdigit():
        driver.quit()
        return False

    score = int(score_text)
    if not (1 <= score <= 1000):
        driver.quit()
        return False

    driver.quit()
    return True


def main_function():
    """
    Main function to call the test function and return an OS exit code.
    :return: -1 if the test fails, 0 if it passes
    """
    app_url = "http://localhost:5000"  # Default URL, can be modified as needed
    if test_scores_service(app_url):
        return 0
    else:
        return -1


if __name__ == "__main__":
    sys.exit(main_function())
