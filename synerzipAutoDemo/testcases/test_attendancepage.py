import pytest

from pages.attendancepage import AttendancePage
from pages.loginpage import LoginPage
from utilities.readproperties import ReadConfig


@pytest.mark.usefixtures("setup")
class TestAttendance():

    def test_elements_of_attendance_page(self):
        lp = LoginPage(self.driver)
        lp.do_login_with_valid_credentials(ReadConfig.getUserName(), ReadConfig.getPassword())
        ap=AttendancePage(self.driver)
        ap.click_on_attendance_tab()
        assert ap.verify_logo_with_INC5000_on_attendancepage()==True
        assert ap.verify_hiring_logo_on_attendancepage()==True
        ap.select_from_and_to_date_from_calender()
        ap.click_on_view_button()
        assert ap.verify_attendance_record()=="No data available in table"

