import pytest

from pages.loginpage import LoginPage
from pages.performancepage import PerformancePage
from utilities.readproperties import ReadConfig


@pytest.mark.usefixtures("setup")
class TestPerformancePage:

    def test_elements_of_performance_page(self):
        lp = LoginPage(self.driver)
        lp.do_login_with_valid_credentials(ReadConfig.getUserName(), ReadConfig.getPassword())
        pp=PerformancePage(self.driver)
        pp.click_on_performance_tab()
        assert pp.verify_logo_with_INC5000_on_performancepage()==True
        assert pp.verify_hiring_logo_on_performancepage()==True
        assert pp.verify_reviewer_of_employee()==ReadConfig.getReviewerName()
