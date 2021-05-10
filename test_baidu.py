import configparser
import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import allure

@allure.feature('Test Baidu WebUI')
class TestBaidu:
    def get_config(self):
        config = configparser.ConfigParser()
        config.read('config.ini', encoding='utf-8')
        # driver = config.get('driver','chrome_driver')
        print(config)
        return config

    def setup(self):
        config = self.get_config()
        try:
            using_headless = os.environ["using_headless"]
        except Exception:
            using_headless = None
            print('没有配置环境变量 using_headless, 按照有界面方式运行自动化测试')
        options = Options()
        if using_headless is not None and using_headless.lower() == 'true':
            print('使用无界面方式运行')
            options.add_argument('--headless')
        # self.driver = webdriver.Chrome(executable_path=config.get('driver', 'chrome_driver'), chrome_options=options)
        self.driver = webdriver.Remote("http://192.168.1.89:5001/wd/hub", desired_capabilities={"browserName": 'chrome'})

        self.driver.get('http://www.baidu.com')
        print('打开浏览器，访问百度首页')
        assert '百度一下' in self.driver.title

    def teardown(self):
        self.driver.quit()
        print('关闭浏览器')

    @pytest.mark.parametrize('keywords', ['今日头条', '王者荣耀'])
    @allure.story('百度搜索')
    def test_case(self, keywords):
        self.driver.find_element_by_id('kw').send_keys(keywords)
        self.driver.find_element_by_id('su').click()
        print(f'搜索关键词~{keywords}')
        time.sleep(2)
        assert f'{keywords}' in self.driver.title
