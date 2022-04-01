from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

url = "https://web.facebook.com/"

class LoginSupport:


    driver = webdriver.Chrome(executable_path="C:/Users/musab.bilal/PycharmProjects/DemoProject/browser/chromedriver.exe")

    def __init__(self):
        self.obj_generic_exception = BaseException()


    def setUp(self):
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get(url)

    def enter_email_password(self):
        input_email = self.driver.find_element(By.XPATH,"//input[@id= 'email']")
        input_email.send_keys("dummyautomationtesting@gmail.com")

        input_pass = self.driver.find_element(By.XPATH, "//input[@id = 'pass']")
        input_pass.send_keys("TestCod3")

    def click_login_button(self):
        self.driver.find_element(By.XPATH, "//button[@name= 'login']").click()
        self.driver.implicitly_wait(20)


    def verify_user_loggedIn(self):
        username = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a//span//span[contains(text(),'Dimple')]")))
        val = username.is_displayed()
        return val




