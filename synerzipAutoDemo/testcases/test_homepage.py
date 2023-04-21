import pytest

from pages.homepage import HomePage
from pages.loginpage import LoginPage
from utilities.readproperties import ReadConfig


@pytest.mark.usefixtures("setup")
class TestHomePage():

    def test_home_page(self):
        lp=LoginPage(self.driver)
        lp.do_login_with_valid_credentials(ReadConfig.getUserName(),ReadConfig.getPassword())
        hp=HomePage(self.driver)
        assert hp.verify_logo_with_INC5000_on_homepage()==True
        assert hp.verify_hiring_logo_on_homepage()==True
        assert hp.is_hometab_exists()==True
        assert hp.is_attendancetab_exists()==True
        hp.get_CurrentDate()
        assert hp.verify_background_color_of_current_date()==ReadConfig.getExpectedBackGroundColor()
        hp.verify_broken_links_of_rewards_and_recognition_panel()
        hp.verify_todays_birthday()
        assert hp.verify_paid_leave_balance()==ReadConfig.getExpectedLeaveBalance()




