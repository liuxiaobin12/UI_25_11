import allure
from selenium import webdriver


class Test_num1:
    def setup_class(self):
        self.driver=webdriver.Chrome()
        self.driver.get('http://baidu.com')



    @allure.step('登录')
    def test_num1(self):
        print('我是测试报告')

        allure.attach(self.driver.get_screenshot_as_png(),'截图演示',allure.attachment_type.PNG)


    def teardown_class(self):
        self.driver.quit()