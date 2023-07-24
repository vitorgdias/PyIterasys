import os
import time
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Creating the print directory, using datetime to define new directory name and order by date
print_path = 'C:/Users/Vitor/Desktop/Vitor/Cursos/Python2023/PyIterasys/prints/' + datetime.now().strftime('%Y-%m=%d %H-%M-%S') + '/'
class Test_Selenium_Webdriver():
    # First class letter need to be in Uppercase to recognize as a test
    def setup_method(self, method):
        self.driver = webdriver.Chrome('C:/Users/Vitor/Desktop/Vitor/Cursos/Python2023/PyIterasys/driver/114/chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # Create the new directory before the first test
        try:
            os.mkdir(print_path)  # Create the new directory with date time before all methods run
        except:
            print('Directory already exists')

    def teardown_method(self):
        self.driver.quit()

    @pytest.mark.parametrize('id, term, course, price', [
        ('1', 'python', 'Introdução ao Python', 'R$ 27,90'),
        ('2', 'Introdução ao Java', 'Introdução ao Java', 'R$ 27,90'),
    ])
    def test_python_course(self, id, term, course, price):
        self.driver.get('https://www.iterasys.com.br')
        self.driver.get_screenshot_as_file(f'{print_path}test {id} - step 1.png')
        self.driver.find_element(By.ID, '16237702146520').click()
        self.driver.get_screenshot_as_file(f'{print_path}test {id} - step 2.png')
        self.driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/input[1]').click()
        self.driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/input[1]').clear()
        self.driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/input[1]').send_keys(term)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.text_to_be_present_in_element((By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/main[1]/a[1]/main[1]/h3[1]'), course))
        self.driver.get_screenshot_as_file(f'{print_path}test {id} - step 3.png')
        self.driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/main[1]/a[1]/main[1]/h3[1]').click()
        self.driver.get_screenshot_as_file(f'{print_path}test {id} - step 4.png')
        assert self.driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/p[1]').text == price
        assert self.driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/h1[1]').text == course
