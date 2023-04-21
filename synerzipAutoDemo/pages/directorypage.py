import time
from select import select

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.core import driver


class DirectoryPage:
    Directory_Tab_Xpath="//*[@id='menu_pim_viewDirectory']"
    Directory_Logo_Xpath="//*[contains(@src,'cropped-synerzip-logo-with-Inc5000.png')]"
    Directorypage_Hiring_Xpath = "//*[contains(@src, 'hiring_icon.png')]"
    Employee_Name_Xpath="//*[@id='empDir_employee_name']"
    Employee_Id_Xpath="//*[@id='empDir_id']"
    Job_Title_Xpath="//*[@id='empDir_job_title']"
    Business_Unit_Xpath="//*[@id='empDir_sub_unit']"
    Search_btn_Xpath="//*[@id='searchBtn']"
    Employee_details_Xpath="//*[text()='2590, Jyoti Joshi']"


    def __init__(self,driver):
        self.driver = driver

    def click_on_directory_tab(self):
        self.driver.find_element(By.XPATH, self.Directory_Tab_Xpath).click()

    def verify_logo_with_INC5000_on_directory(self):
        directorypageLogo_element = self.driver.find_element(By.XPATH, self.Directory_Logo_Xpath)
        return bool(directorypageLogo_element)

    def verify_hiring_logo_on_directorypage(self):
        directorypageHiringLogo_element = self.driver.find_element(By.XPATH, self.Directorypage_Hiring_Xpath)
        return bool(directorypageHiringLogo_element)

    def enter_employee_name(self,employee_name):
        emp_nam=self.driver.find_element(By.XPATH, self.Employee_Name_Xpath)
        emp_nam.send_keys(employee_name)
        time.sleep(10)

    def enter_employee_id(self, employee_id):
        emp_id_detail=self.driver.find_element(By.XPATH, self.Employee_Id_Xpath)
        emp_id_detail.send_keys(employee_id)
        time.sleep(10)

    def select_job_title_from_dropdown(self):
        job_title_element=self.driver.find_element(By.XPATH, self.Job_Title_Xpath)
        drp_job_title=Select(job_title_element)
        drp_job_title.select_by_visible_text("Lead QA Engineer")
        time.sleep(10)

    def select_business_unit_from_dropdown(self):
        business_unit_element=self.driver.find_element(By.XPATH, self.Business_Unit_Xpath)
        drp_job_title=Select(business_unit_element)
        drp_job_title.select_by_visible_text("BU-7 (Mukund Rajamannar)")

    def click_on_search_button(self):
        self.driver.find_element(By.XPATH, self.Search_btn_Xpath).click()

    def verify_employee_details(self):
        employee_details=self.driver.find_element(By.XPATH, self.Employee_details_Xpath)
        return employee_details.text










