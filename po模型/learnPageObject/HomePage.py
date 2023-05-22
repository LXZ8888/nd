'''首页元素po管理'''
from selenium.webdriver.common.by import By

from InitBrowser import Browser

class HomePage(Browser):
    search_input=(By.ID,'search-input') #元祖
    search_button=(By.ID,'ai-topsearch')

    def _search_input(self,value):
        '''首页输入框输入操作，参数为搜索的关键字'''
        #self.wait_element_visible(HomePage.search_input)
        #self.find_element(HomePage.search_input).send_keys(value)  # 1.输入用户名
        self._send_keys(HomePage.search_input,value)

    def _search_button(self):
        '''搜索按钮的点击'''
        #self.wait_element_visible(HomePage.search_input)
        #self.find_element(HomePage.search_button).click()  # 1.点击登录按钮

        self._click(HomePage.search_button)


    def search(self,value):
        '''搜索的关键字'''
        self._search_input(value)
        self._search_button()