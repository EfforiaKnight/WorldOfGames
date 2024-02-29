import unittest
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from chromedriver_py import binary_path


class TestScoresService(unittest.TestCase):
    URL = "<URL>"

    def setUp(self):
        svc = webdriver.ChromeService(executable_path=binary_path)
        self.driver = webdriver.Chrome(service=svc)

    def test_score_is_between_1_and_1000(self):
        self.driver.get(self.URL)
        score_element = self.driver.find_element(By.ID, "score")
        score = int(score_element.text)
        self.assertTrue(1 <= score <= 1000, "Score is not between 1 and 1000")

    def tearDown(self):
        self.driver.quit()


def main_function():
    if len(sys.argv) > 1:
        TestScoresService.URL = sys.argv.pop()
    unittest.main()


if __name__ == "__main__":
    main_function()
