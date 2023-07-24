import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Test_Selenium_Webdriver:
    # First class letter need to be in Uppercase to recognize as a test
    def setup_method(self):
        self.driver = webdriver.Chrome('C:/Users/Vitor/Desktop/Vitor/Cursos/Python2023/PyIterasys/driver/114/chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
    def teardown_method(self):
        self.driver.quit()
    @pytest.mark.parametrize('term, course, price',[
        ('python', 'Introdução ao Python', 'R$ 27,90'),
        ('Introdução ao Java', 'Introdução ao Java', 'R$ 27,90'),
    ])
    def test_python_course(self, term, course, price):
        self.driver.get('https://www.iterasys.com.br')
        self.driver.find_element(By.ID, '16237702146520').click()
        self.driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/input[1]').click()
        self.driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/input[1]').clear()
        self.driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/input[1]').send_keys(term)
        #self.driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/main[1]/a[1]/main[1]/h3[1]').click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.text_to_be_present_in_element((By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/main[1]/a[1]/main[1]/h3[1]'), course))
        self.driver.find_element(By.XPATH,'/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/main[1]/a[1]/main[1]/h3[1]').click()
        assert self.driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/p[1]').text == price
        assert self.driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/h1[1]').text == course
