import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class CeShi(unittest.TestCase):
    @classmethod
    def setUp(cls) -> None:
        # cls.driver = webdriver.Chrome(r'E:\PythonDaiMa\aaa\chromedriver.exe')
        cls.driver = webdriver.Chrome()
        cls.base_url =  "https://www.baidu.com/"

    @classmethod
    def tearDown(cls) -> None:
        cls.driver.close()

    def test_AAA(self):
        self.driver.get(url=self.base_url)
        self.driver.find_element(By.XPATH,'//*[@id="kw"]').send_keys("壁纸")
        self.driver.find_element(By.XPATH,'//*[@id="su"]').click()

if __name__ == '__main__':
    unittest.main()
