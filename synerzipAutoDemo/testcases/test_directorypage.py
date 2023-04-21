import pytest

from pages.directorypage import DirectoryPage
from pages.loginpage import LoginPage
from utilities.readproperties import ReadConfig


@pytest.mark.usefixtures("setup")
class TestDirectoryPage:

    def test_directory_page(self):
        lp = LoginPage(self.driver)
        lp.do_login_with_valid_credentials(ReadConfig.getUserName(), ReadConfig.getPassword())
        dp=DirectoryPage(self.driver)
        dp.click_on_directory_tab()
        assert dp.verify_logo_with_INC5000_on_directory()==True
        assert dp.verify_hiring_logo_on_directorypage()==True
        dp.enter_employee_name(ReadConfig.getEmployeeName())
        dp.enter_employee_id(ReadConfig.getEmployeeId())
        dp.select_job_title_from_dropdown()
        dp.select_business_unit_from_dropdown()
        dp.click_on_search_button()
        assert dp.verify_employee_details()==ReadConfig.getExpectedEmployeeDetails()



