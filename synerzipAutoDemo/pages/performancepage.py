from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class PerformancePage():

    Performance_Tab_Xpath="//*[text()='Performance']"
    Reviews_Tab_Xpath="//*[@id='menu_performance_Reviews']"
    My_Review_Xpath="//*[text()='My Review']"
    Performancepage_logo_Xpath = "//*[contains(@src,'cropped-synerzip-logo-with-Inc5000.png')]"
    Performancepage_Hiring_Xpath = "//*[contains(@src, 'hiring_icon.png')]"
    Review_Period_Xpath="//table[@id='resultTable']//tbody//tr//td[7]"

    def __init__(self,driver):
        self.driver=driver

    def click_on_performance_tab(self):
        performance_tab=self.driver.find_element(By.XPATH, self.Performance_Tab_Xpath)
        #performance_tab.click()
        review_tab=self.driver.find_element(By.XPATH, self.Reviews_Tab_Xpath)
        my_review=self.driver.find_element(By.XPATH, self.My_Review_Xpath)
        actions=ActionChains(self.driver)
        #actions.move_to_element(performance_tab).move_to_element(review_tab).move_to_element(my_review).click().perform()
        actions.move_to_element(performance_tab).click().perform()
        actions.move_to_element(review_tab).click().perform()
        actions.move_to_element(my_review).click().perform()

    def verify_logo_with_INC5000_on_performancepage(self):
        PerformancepageLogo_element = self.driver.find_element(By.XPATH, self.Performancepage_logo_Xpath)
        return bool(PerformancepageLogo_element)

    def verify_hiring_logo_on_performancepage(self):
        PerformancepageHiringLogo_element = self.driver.find_element(By.XPATH, self.Performancepage_Hiring_Xpath)
        return bool(PerformancepageHiringLogo_element)



    def verify_reviewer_of_employee(self):
        review_period=self.driver.find_element(By.XPATH, self.Review_Period_Xpath)
        return review_period.text
