import pytest

from pages.infopage import InfoPage
from pages.loginpage import LoginPage
from utilities.readproperties import ReadConfig


@pytest.mark.usefixtures("setup")
class TestInfoPage:

    def test_elements_of_info_page(self):
        lp = LoginPage(self.driver)
        lp.do_login_with_valid_credentials(ReadConfig.getUserName(), ReadConfig.getPassword())
        ip=InfoPage(self.driver)
        assert ip.verify_logo_with_INC5000_on_infopage()==True
        assert ip.verify_hiring_logo_on_infopage()==True
        ip.verify_info_page_elements(ReadConfig.getFirstName(),ReadConfig.getMiddleName(),ReadConfig.getLastName(),ReadConfig.getFatherName(),ReadConfig.getMotherName())
        assert ip.verify_text_no_records_found() == ReadConfig.getLangRecords()