from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import sys

# Test the web service by checking if the score is a number between 1 and 1000
# :param app_url: URL of the web service
# :return: True if score is valid, False otherwise


def test_scores_service(app_url):
    driver = None  # Initialize driver variable
    try:
        # Set up Chrome options
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # Run in headless mode
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        # Initialize Chrome driver
        print("Attempting to initialize ChromeDriver...")
        driver = webdriver.Chrome(options=options)
        print("ChromeDriver initialized successfully.")

        driver.get(app_url)

        # Read the score from Scores.txt
        with open("Scores.txt", "r", encoding="utf-8") as file:
            score_text = file.read().strip()

        # Validate the score
        if score_text.isdigit():
            score = int(score_text)
            return 1 <= score <= 1000
        return False

    except Exception as e:
        print(f"Error during test: {str(e)}")
        print("ChromeDriver may not be installed correctly or is not executable.")
        return False
    finally:
        if driver is not None:
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
