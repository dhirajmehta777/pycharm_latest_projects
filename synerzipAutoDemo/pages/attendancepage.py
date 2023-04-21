import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from utilities.readproperties import ReadConfig

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class AttendancePage:

    Attendance_Tab_Xpath="//*[text()='Attendance']"
    My_Records_Xpath="//*[text()='My Records']"
    Attendancepage_logo_Xpath="//*[contains(@src,'cropped-synerzip-logo-with-Inc5000.png')]"
    Attendancepage_Hiring_Xpath="//*[contains(@src, 'hiring_icon.png')]"
    From_Calendar_Xpath="(//*[@class='ui-datepicker-trigger'])[1]"
    Privious_Btn_Xpath="//span[text()='Prev']"
    From_Date_Month_Xpath="//*[@class='ui-datepicker-month']"
    From_Date_Year_Xpath="//*[@class='ui-datepicker-year']"
    From_Date_Xpath="//*[text()='15']"
    To_Calendar_Xpath = "(//*[@class='ui-datepicker-trigger'])[2]"
    To_Date_Month_Xpath = "//*[@class='ui-datepicker-month']"
    To_Date_Year_Xpath = "//*[@class='ui-datepicker-year']"
    To_Date_Xpath="//*[text()='31']"
    View_Btn_Xpath="//*[@id='searchBtn']"
    Attendance_Record_Xpath="//*[@id='resultAttendanceRecords']//tbody//tr//td"

    def __init__(self,driver):
        self.driver=driver

    def click_on_attendance_tab(self):
        attendance_tab=self.driver.find_element(By.XPATH, self.Attendance_Tab_Xpath)
        my_records=self.driver.find_element(By.XPATH, self.My_Records_Xpath)
        actions=ActionChains(self.driver)
        actions.move_to_element(attendance_tab).click().perform()
        actions.move_to_element(my_records).click().perform()

    def verify_logo_with_INC5000_on_attendancepage(self):
        AttendancepageLogo_element = self.driver.find_element(By.XPATH, self.Attendancepage_logo_Xpath)
        return bool(AttendancepageLogo_element)

    def verify_hiring_logo_on_attendancepage(self):
        AttendancepageHiringLogo_element = self.driver.find_element(By.XPATH, self.Attendancepage_Hiring_Xpath)
        return bool(AttendancepageHiringLogo_element)

    def click_on_calendar_to_select_from_date(self):
        self.driver.find_element(By.XPATH, self.From_Calendar_Xpath).click()

    def click_on_previous_button(self):
        self.driver.find_element(By.XPATH, self.Privious_Btn_Xpath).click()
        time.sleep(5)

    def select_month_for_from_date_calendar(self):
        month_from = self.driver.find_element(By.XPATH, self.From_Date_Month_Xpath)
        month_ele_from = Select(month_from)
        month_ele_from.select_by_visible_text(ReadConfig.getMonthFrom())
        time.sleep(2)

    def select_year_for_from_date_calendar(self):
        year_from=self.driver.find_element(By.XPATH, self.From_Date_Year_Xpath)
        year_ele_from=Select(year_from)
        year_ele_from.select_by_visible_text(ReadConfig.getYearFrom())
        time.sleep(2)

    def select_day_for_from_date_calendar(self):
        self.driver.find_element(By.XPATH, self.From_Date_Xpath).click()
        time.sleep(2)

    def click_on_calendar_to_select_to_date(self):
        self.driver.find_element(By.XPATH, self.To_Calendar_Xpath).click()
        self.click_on_previous_button()
        time.sleep(2)

    def select_month_for_to_date_calendar(self):
        month_to=self.driver.find_element(By.XPATH, self.To_Date_Month_Xpath)
        month_ele_to=Select(month_to)
        month_ele_to.select_by_visible_text(ReadConfig.getMonthTo())
        time.sleep(2)

    def select_year_for_to_date_calendar(self):
        year_to=self.driver.find_element(By.XPATH, self.To_Date_Year_Xpath)
        year_ele_to=Select(year_to)
        year_ele_to.select_by_visible_text(ReadConfig.getYearTo())
        time.sleep(2)

    def select_day_for_to_date_calendar(self):
        self.driver.find_element(By.XPATH, self.To_Date_Xpath).click()
        time.sleep(2)

    def select_from_and_to_date_from_calender(self):
        self.click_on_calendar_to_select_from_date()
        self.click_on_previous_button()
        self.select_month_for_from_date_calendar()
        self.select_year_for_from_date_calendar()
        self.select_day_for_from_date_calendar()
        self.click_on_calendar_to_select_to_date()
        self.select_month_for_to_date_calendar()
        self.select_year_for_to_date_calendar()
        self.select_day_for_to_date_calendar()

    def click_on_view_button(self):
        self.driver.find_element(By.XPATH, self.View_Btn_Xpath).click()

    def verify_attendance_record(self):
        record_ele=self.driver.find_element(By.XPATH, self.Attendance_Record_Xpath)
        return record_ele.text







