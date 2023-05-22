'''用例类：只有业务关键字+断言'''
import time
import unittest
from selenium import webdriver




class ScTestCases(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:

        '''前置：打开被测项目'''
        self.driver = webdriver.Chrome()  # 浏览器对象
        self.driver.get('http://42.192.6.197/?s=user/loginInfo.html')  # 打开电商商城系统


    def tearDown(self) -> None:
        '''后置：用例运行完成等待几秒'''
        time.sleep(2)

    @classmethod
    def tearDownClass(self) -> None:
        self.driver.quit()

    def test_01_login(self):
        '''普通脚本'''
        driver = self.driver
        driver.find_element_by_name('accounts').send_keys('admin1')
        driver.find_element_by_name('pwd').send_keys('shopxo')
        driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[3]/button").click()

    def test_02_search(self):
         time.sleep(3)
         self.driver.find_element_by_id('search-input').send_keys('手机')
         self.driver.find_element_by_id('ai-topsearch').click()

    # @unittest.skipUnless(3<2,'因为3大于，理由')
    def test_03_search_by_price(self):
        '''用例2：根据价格进行搜索'''
        '''筛选价格'''
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[text()='2000-3000']").click()
        '''断言：搜索3条价格为2-3k的手机'''
        time.sleep(2)
        res = len(self.driver.find_elements_by_xpath("//*[@class='am-animation-scale-up']"))
        self.assertEqual(res, 0)


if __name__ == '__main__':
    unittest.main()
