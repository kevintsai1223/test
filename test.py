from selenium import webdriver
import unittest
import time

class test_fetnet(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url="https://www.fetnet.net"
        
    def test_fetnet(self):
        driver=self.driver
        driver.get(self.base_url+"/")
        time.sleep(2)

        driver.find_element_by_xpath("//*[@id='pIcon-0']/div/button/span/img").click()
        time.sleep(2)
        #driver.find_element_by_class_name("登入/註冊").click()
        driver.find_element_by_xpath("//*[@id='pIcon-1']/div/div[1]/a/span").click()
        
        # 輸入登入資訊
        driver.find_element_by_id("UserID").send_keys("0955217534")
        driver.find_element_by_id("login_btn").click()        
        driver.find_element_by_id("password-field").send_keys("mingjen1223")
        driver.find_element_by_id("loginBtn").click()
        time.sleep(2)
        
        driver.find_element_by_xpath("//*[@id='pIcon-2']/div/button/span/img").click()
        time.sleep(2)
        #driver.find_element_by_class_name("登出").click()
        driver.find_element_by_xpath("//*[@id='pIcon-2']/div/div/div/div[1]/div/span").click()

    #@unittest.skip("skip fetnet customer service")
    def test_customer_service(self):
        driver=self.driver
        driver.get(self.base_url+"/")
        time.sleep(2)

        driver.find_element_by_link_text("用戶服務").click()
        time.sleep(2)
        driver.find_element_by_link_text("帳單/繳費/儲值").click()
        time.sleep(2)
        driver.find_element_by_link_text("帳單/費用").click()
        time.sleep(2)
        driver.find_element_by_link_text("了解更多").click()
        time.sleep(5)

        # 輸入登入資訊
        driver.find_element_by_id("userId").send_keys("0955217534")
        driver.find_element_by_id("newPassword").send_keys("mingjen1223")
        driver.find_element_by_id("showRuningCircle").click()
        time.sleep(5)

        driver.find_element_by_link_text("登出").click()

    def test_facebook(self):
        driver=self.driver
        driver.get(self.base_url+"/")
        time.sleep(2)

        fetnet_window = driver.current_window_handle

        driver.find_element_by_link_text("登入").click()

        # 輸入登入資訊
        driver.find_element_by_id("userId").clear()
        driver.find_element_by_id("newPassword").clear()
        driver.find_element_by_xpath(
            "//*[@id='membership-Wrap']/section[1]/div[3]/div/div/div[2]/div[2]/div[1]").click()

        all_handles = driver.window_handles
        # FACEBOOK
        for handle in all_handles:
            if handle != fetnet_window:
                driver.switch_to.window(handle)

                driver.find_element_by_id("email").send_keys("kevin.tsai1223@gmail.com")
                driver.find_element_by_id("pass").send_keys("mingjen1223")
                driver.find_element_by_id("loginbutton").click()
                time.sleep(2)

        # FETNET
        for handle in all_handles:
            if handle == fetnet_window:
                driver.switch_to.window(handle)

                driver.find_element_by_link_text("登出").click()
                time.sleep(2)

    def test_yahoo(self):
        driver=self.driver
        driver.get(self.base_url+"/")
        time.sleep(2)

        fetnet_window = driver.current_window_handle

        driver.find_element_by_link_text("登入").click()

        # 輸入登入資訊
        driver.find_element_by_id("userId").clear()
        driver.find_element_by_id("newPassword").clear()
        driver.find_element_by_xpath(
            "//*[@id='membership-Wrap']/section[1]/div[3]/div/div/div[2]/div[2]/div[2]").click()

        all_handles = driver.window_handles

        # YAHOO
        for handle in all_handles:
            if handle != fetnet_window:
                driver.switch_to.window(handle)

                driver.find_element_by_id("login-username").send_keys("kevin.tsai1223@yahoo.com.tw")
                driver.find_element_by_id("login-signin").click()

                driver.find_element_by_id("login-passwd").send_keys("D2617591")
                driver.find_element_by_id("login-signin").click()

                driver.find_element_by_id("oauth2-agree").click()
                time.sleep(2)

        # FETNET
        for handle in all_handles:
            if handle == fetnet_window:
                driver.switch_to.window(handle)

                driver.find_element_by_link_text("登出").click()
                time.sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    #unittest.main()
    
    suite=unittest.TestSuite()
    suite.addTest(test_fetnet("test_fetnet"))
    """
    suite.addTest(test_fetnet("test_facebook"))
    suite.addTest(test_fetnet("test_yahoo"))
    suite.addTest(test_fetnet("test_customer_service"))
    """
    
    runner=unittest.TextTestRunner()
    runner.run(suite)
    