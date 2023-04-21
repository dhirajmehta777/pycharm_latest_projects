import pytest

from pages.loginpage import LoginPage
from utilities.readproperties import ReadConfig


@pytest.mark.usefixtures("setup")
class TestLoginPage:

    def test_login_page(self):
        lp=LoginPage(self.driver)
        lp.verify_existance_of_all_elements_of_loginPage()
        assert lp.get_login_page_title()==ReadConfig.getExpectedTitleOfPage()
        assert lp.is_logo_exists()==True
        assert lp.is_signin_exists()==True
        assert lp.is_forgot_your_pwd_link_exists()==True
        assert lp.is_signin_with_google_exists()==True
        assert lp.is_linkedin_link_exists()==True
        assert lp.is_facebook_link_exists()==True
        assert lp.is_twitter_link_exists()==True
        assert lp.is_youtube_link_exists()==True
        lp.do_login_with_valid_credentials(ReadConfig.getUserName(),ReadConfig.getPassword())
        lp.do_login_with_invalid_credentials(ReadConfig.getInvalidUserName(),ReadConfig.getInvalidPassword())
        assert lp.is_invalid_credential_message_displayed()==ReadConfig.getExpectedInvaliCredentialMessage()

# actual_title=lp.get_login_page_title()
        # if actual_title == "SYNERZIP":
        #     assert True
        # else:
        #     self.driver.save_screenshot(".//screenshots//" + "login_Page_title.png")
        #     assert False
        # assert lp.is_signinWithGoogle_exists()==True