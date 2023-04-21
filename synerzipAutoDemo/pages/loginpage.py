import time

from selenium.webdriver.common.by import By

class LoginPage():
    LogoOfHrms_Xpath="//*[@alt='Synerzip - HRMS']"
    SignInWithGoogle_Xpath = "//a[text()='Sign in with Google']"
    SignIn_Xpath="//*[text()='Sign In']"
    ForgotPwdLink_Xpath="//*[text()='Forgot your password?']"
    Linkedin_Xpath="//*[contains(@src,'linkedin.png')]"
    Facebook_Xpath="//*[contains(@src,'facebook.png')]"
    Twitter_Xpath="//*[contains(@src,'twiter.png')]"
    Youtube_Xpath="//*[contains(@src,'youtube.png')]"
    Username_Id = "txtUsername"
    Password_Id = "txtPassword"
    Login_btn_xpath = "//*[text()='Login ']"
    Welcome_tab_Xpath="//*[text()='Welcome Dhiraj']"
    Logout_tab_Xpath="//*[text()='Logout']"
    Invalid_Credential_Xpath="//*[text()='Invalid credentials']"

    def __init__(self, driver):
        self.driver = driver

    def get_login_page_title(self):
        return self.driver.title

    def is_logo_exists(self):
        hrms_logo_element = self.driver.find_element(By.XPATH, self.LogoOfHrms_Xpath)
        return bool(hrms_logo_element)

    def is_signin_exists(self):
        signin_element = self.driver.find_element(By.XPATH, self.SignIn_Xpath)
        return bool(signin_element)

    def is_forgot_your_pwd_link_exists(self):
        forgot_your_pwd_element = self.driver.find_element(By.XPATH, self.ForgotPwdLink_Xpath)
        return bool(forgot_your_pwd_element)

    def is_signin_with_google_exists(self):
        sign_in_with_google_element=self.driver.find_element(By.XPATH, self.SignInWithGoogle_Xpath)
        return bool(sign_in_with_google_element)

    def is_linkedin_link_exists(self):
        linkedin_element=self.driver.find_element(By.XPATH, self.Linkedin_Xpath)
        return bool(linkedin_element)

    def is_facebook_link_exists(self):
        facebook_element=self.driver.find_element(By.XPATH, self.Facebook_Xpath)
        return bool(facebook_element)

    def is_twitter_link_exists(self):
        twitter_element=self.driver.find_element(By.XPATH, self.Twitter_Xpath)
        return bool(twitter_element)

    def is_youtube_link_exists(self):
        youtube_element=self.driver.find_element(By.XPATH, self.Youtube_Xpath)
        return bool(youtube_element)

    def verify_existance_of_all_elements_of_loginPage(self):
        self.get_login_page_title()
        self.is_logo_exists()
        self.is_signin_exists()
        self.is_forgot_your_pwd_link_exists()
        self.is_signin_with_google_exists()
        self.is_linkedin_link_exists()
        self.is_facebook_link_exists()
        self.is_twitter_link_exists()
        self.is_youtube_link_exists()


    def setUserName(self, username):
        self.driver.find_element(By.ID, self.Username_Id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.Password_Id).send_keys(password)

    def clickOnLoginBtn(self):
        self.driver.find_element(By.XPATH, self.Login_btn_xpath).click()

    def is_invalid_credential_message_displayed(self):
        invalid_credential_message=self.driver.find_element(By.XPATH, self.Invalid_Credential_Xpath)
        return invalid_credential_message.text

    def do_click_on_welcome_tab(self):
        self.driver.find_element(By.XPATH, self.Welcome_tab_Xpath).click()

    def do_click_on_logout_tab(self):
        self.driver.find_element(By.XPATH, self.Logout_tab_Xpath).click()

    def do_login_with_valid_credentials(self,username,password):
        self.setUserName(username)
        self.setPassword(password)
        self.clickOnLoginBtn()
        time.sleep(10)

    def do_login_with_invalid_credentials(self,invalidusername,invalidpassword):
        self.do_click_on_welcome_tab()
        time.sleep(10)
        self.do_click_on_logout_tab()
        time.sleep(10)
        self.setUserName(invalidusername)
        self.setPassword(invalidpassword)
        self.clickOnLoginBtn()
        time.sleep(10)


