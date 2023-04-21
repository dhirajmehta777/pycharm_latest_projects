from selenium.webdriver.common.by import By
import datetime
from selenium.webdriver.support.color import Color
import requests


class HomePage:
    HomeTab_Xpath = "//*[text()='Home']"
    Attendance_Xpath="//*[text()='Attendance']"
    current_dt_Xpath="(//*[contains(@class,'ui-state-highlight')])[1]"
    Rwards_Links_Xpath="//table[@id='rr_integration']//a"
    Todays_Birthday_Xpath="//fieldset[@id='panel-birthday']//div//strong"
    Leave_Balance_Xpath="(//table[@style='width:100%']//tr//td)[2]"
    Homepage_logo_Xpath="//*[contains(@src,'cropped-synerzip-logo-with-Inc5000.png')]"
    Homepage_Hiring_Xpath="//*[contains(@src, 'hiring_icon.png')]"

    def __init__(self,driver):
        self.driver=driver

    def verify_logo_with_INC5000_on_homepage(self):
        HomepageLogo_element = self.driver.find_element(By.XPATH, self.Homepage_logo_Xpath)
        return bool(HomepageLogo_element)

    def verify_hiring_logo_on_homepage(self):
        HomepageHiringLogo_element = self.driver.find_element(By.XPATH, self.Homepage_Hiring_Xpath)
        return bool(HomepageHiringLogo_element)

    def is_hometab_exists(self):
        hometab_element=self.driver.find_element(By.XPATH, self.HomeTab_Xpath)
        return bool(hometab_element)

    def is_attendancetab_exists(self):
        attendancetab_element=self.driver.find_element(By.XPATH, self.Attendance_Xpath)
        return bool(attendancetab_element)

    def get_CurrentDate(self):
        current_dt = datetime.datetime.now()
        print(current_dt.strftime("%d-%m-%Y"))

    def verify_background_color_of_current_date(self):
        bc_color=self.driver.find_element(By.XPATH, self.current_dt_Xpath).value_of_css_property("background-color")
        hex_bc_color=Color.from_string(bc_color).hex
        return hex_bc_color

    def verify_broken_links_of_rewards_and_recognition_panel(self):
        all_links=self.driver.find_elements(By.XPATH, self.Rwards_Links_Xpath)
        count=0
        for link in all_links:
            url=link.get_attribute('href')
            res=requests.head(url)
            if res.status_code >= 400:
                print(url,"is a broken link")
                count += 1
            else:
                print(url,"is valid link")
        print("Total number of broken links:",count)

    def verify_todays_birthday(self):
        List_of_birthdays=self.driver.find_elements(By.XPATH, self.Todays_Birthday_Xpath)
        print("Total Number of Birthday's Today:",len(List_of_birthdays))
        for birthday in List_of_birthdays:
            print(birthday.text)

    def verify_paid_leave_balance(self):
        leave_bal=self.driver.find_element(By.XPATH, self.Leave_Balance_Xpath)
        return leave_bal.text









