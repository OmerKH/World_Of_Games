from selenium import webdriver
from selenium.webdriver.common.by import By
import sys

# Test the web service by checking if the score is a number between 1 and 1000
# :param app_url: URL of the web service
# :return: True if score is valid, False otherwise


def test_scores_service(app_url):
    try:
        # Set up Chrome options
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')  # Run in headless mode
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        # Initialize Chrome driver
        driver = webdriver.Chrome(options=options)
        driver.get(app_url)

        # Find the score element
        score_element = driver.find_element(By.ID, 'score')
        score_text = score_element.text

        # Validate the score
        if score_text.isdigit():
            score = int(score_text)
            return 1 <= score <= 1000
        return False

    except Exception as e:
        print(f"Error during test: {str(e)}")
        return False
    finally:
        driver.quit()


def main_function():
    """
    Main function to run the test and return appropriate exit code
    :return: 0 if test passes, -1 if test fails
    """
    #    app_url = "http://localhost:5000"
    app_url = "http://host.docker.internal:5000"  # Updated URL for Docker

    if test_scores_service(app_url):
        print("Test passed!")
        return 0
    else:
        print("Test failed!")
        return -1


if __name__ == "__main__":
    sys.exit(main_function())
