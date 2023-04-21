import time
from select import select

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.core import driver
from utilities.readproperties import ReadConfig

class InfoPage:
    Info_Tab_Xpath="//*[text()='My Info']"
    Info_Logo_Xpath="//*[contains(@src,'cropped-synerzip-logo-with-Inc5000.png')]"
    Infopage_Hiring_Xpath = "//*[contains(@src, 'hiring_icon.png')]"
    Edit_Ele_Xpath="//*[@value='Edit']"
    First_Name_Xpath="//*[@id='personal_txtEmpFirstName']"
    Middle_Name_Xpath="//*[@id='personal_txtEmpMiddleName']"
    Last_Name_Xpath="//*[@id='personal_txtEmpLastName']"
    Father_Name_Xpath="//*[@id='personal_txtEmpFatherName']"
    Mother_Name_Xpath="//*[@id='personal_txtEmpMotherName']"
    Marital_Xpath="//*[@id='personal_cmbMarital']"
    Physically_Challenged_Xpath="//*[@id='personal_cmbphyChallenge']"
    Save_Info_Xpath="(//*[@value='Save'])[1]"
    No_Records_Found_Xpath="//table[@id='lang_data_table']//tr//td[2]"
    Add_Language_Btn_Xpath="//*[@id='addLanguage']"
    Click_On_Select_Language_Xpath="//*[@id='language_code']"
    Dropdown_Element_Xpath="//*[@id='language_code']"
    #Language_Options_Xpath="//*[@id='language_code']//option[(text()!='-- Select --') and (text()!='other')]"
    Radio_buttons_Xpath="//table[@class='table tablesorter']//tbody//tr //td[3]//input[@type='radio']"
    Language_Save_Button="//*[@id='btnLanguageSave']"
    Checkbox_Xpath="//*[@id='languageCheckAll']"
    Delete_Xpath="//*[@id='delLanguage']"
    Attachment_Add_Button_Xpath = "//*[@id='btnAddAttachment']"
    Select_file_Xpath="//*[@id='ufile']"
    Upload_Button_Xpath="//*[@id='btnSaveAttachment']"
    Attachment_Checkbox_Xpath="//*[@id='attachmentsCheckAll']"
    Attachment_Delete_Button_Xpath="//*[@id='btnDeleteAttachment']"

    def __init__(self, driver):
        self.driver=driver

    def click_on_my_info_tab(self):
        self.driver.find_element(By.XPATH, self.Info_Tab_Xpath).click()

    def verify_logo_with_INC5000_on_infopage(self):
        InpopageLogo_element = self.driver.find_element(By.XPATH, self.Info_Logo_Xpath)
        return bool(InpopageLogo_element)

    def verify_hiring_logo_on_infopage(self):
        InfopageHiringLogo_element = self.driver.find_element(By.XPATH, self.Infopage_Hiring_Xpath)
        return bool(InfopageHiringLogo_element)

    def click_on_edit_button_to_modify_user_details(self):
        self.driver.execute_script("window.scrollBy(0,700)","")
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.Edit_Ele_Xpath).click()

    def enter_first_name(self,first_name):
        self.driver.execute_script("window.scrollBy(0,-700)", "")
        time.sleep(10)
        fname=self.driver.find_element(By.XPATH, self.First_Name_Xpath)
        fname.clear()
        fname.send_keys(first_name)

    def enter_middle_name(self,middle_name):
        mname=self.driver.find_element(By.XPATH, self.Middle_Name_Xpath)
        mname.clear()
        mname.send_keys(middle_name)

    def enter_last_name(self,last_name):
        lname=self.driver.find_element(By.XPATH, self.Last_Name_Xpath)
        lname.clear()
        lname.send_keys(last_name)

    def enter_father_name(self, father_name):
        fathernam=self.driver.find_element(By.XPATH, self.Father_Name_Xpath)
        fathernam.clear()
        fathernam.send_keys(father_name)

    def enter_mother_name(self,mother_name):
        mothernam=self.driver.find_element(By.XPATH, self.Mother_Name_Xpath)
        mothernam.clear()
        mothernam.send_keys(mother_name)

    def select_marital_status(self):
        marital_status=self.driver.find_element(By.XPATH, self.Marital_Xpath)
        marital_status.click()
        select_from_drp=Select(marital_status)
        select_from_drp.select_by_visible_text("Single")
        time.sleep(5)

    def select_physically_challenged_status(self):
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        physically_challenged_ele=self.driver.find_element(By.XPATH, self.Physically_Challenged_Xpath)
        physically_challenged_ele.click()
        status_of_physically_challenged=Select(physically_challenged_ele)
        status_of_physically_challenged.select_by_visible_text("No")
        time.sleep(5)

    def click_on_save_button(self):
        self.driver.find_element(By.XPATH, self.Save_Info_Xpath).click()
        time.sleep(5)

    def verify_text_no_records_found(self):
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        text_ele=self.driver.find_element(By.XPATH, self.No_Records_Found_Xpath)
        return text_ele.text

    def click_on_add_btn_for_adding_languages(self):
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        self.driver.find_element(By.XPATH, self.Add_Language_Btn_Xpath).click()

    def click_on_all_radio_buttons_for_lang_proficiency(self):
        radio_buttons = self.driver.find_elements(By.XPATH, self.Radio_buttons_Xpath)
        for btn in radio_buttons:
            btn.click()

    def click_on_lang_save_button(self):
        lang_save_btn = self.driver.find_element(By.XPATH, self.Language_Save_Button)
        lang_save_btn.click()

    def select_english_language(self):
        self.click_on_add_btn_for_adding_languages()
        lang_options=self.driver.find_element(By.XPATH, self.Dropdown_Element_Xpath)
        lang_ele = Select(lang_options)
        lang_ele.select_by_visible_text(ReadConfig.getLangEnglish())
        self.click_on_all_radio_buttons_for_lang_proficiency()
        self.click_on_lang_save_button()

    def select_hindi_language(self):
        self.click_on_add_btn_for_adding_languages()
        lang_options = self.driver.find_element(By.XPATH, self.Dropdown_Element_Xpath)
        lang_ele = Select(lang_options)
        lang_ele.select_by_visible_text(ReadConfig.getLangHindi())
        self.click_on_all_radio_buttons_for_lang_proficiency()
        self.click_on_lang_save_button()

    def select_marathi_language(self):
        self.click_on_add_btn_for_adding_languages()
        lang_options = self.driver.find_element(By.XPATH, self.Dropdown_Element_Xpath)
        lang_ele = Select(lang_options)
        lang_ele.select_by_visible_text(ReadConfig.getLangMarathi())
        self.click_on_all_radio_buttons_for_lang_proficiency()
        self.click_on_lang_save_button()

    def click_on_checkbox(self):
        lang_checkbox = self.driver.find_element(By.XPATH, self.Checkbox_Xpath)
        lang_checkbox.click()

    def click_on_delete_btn(self):
        delete_lang=self.driver.find_element(By.XPATH, self.Delete_Xpath)
        delete_lang.click()

    def click_on_attachment_add_button(self):
        self.driver.find_element(By.XPATH, self.Attachment_Add_Button_Xpath).click()

    def select_file_to_be_uploaded(self):
        self.driver.find_element(By.XPATH, self.Select_file_Xpath).send_keys("/home/excellarate/Documents/Dhiraj.docx")

    def click_on_upload_button(self):
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.Upload_Button_Xpath).click()

    def click_on_attachment_checkbox(self):
        self.driver.find_element(By.XPATH, self.Attachment_Checkbox_Xpath).click()

    def click_on_delete_attachment_button(self):
        self.driver.find_element(By.XPATH, self.Attachment_Delete_Button_Xpath).click()

    def enter_all_personal_info(self, first_name, middle_name, last_name, father_name, mother_name):
        self.click_on_my_info_tab()
        self.click_on_edit_button_to_modify_user_details()
        self.enter_first_name(first_name)
        self.enter_middle_name(middle_name)
        self.enter_last_name(last_name)
        self.enter_father_name(father_name)
        self.enter_mother_name(mother_name)
        self.select_marital_status()
        self.select_physically_challenged_status()
        self.click_on_save_button()

    def verify_addition_and_deletion_of_languages(self):
        self.select_english_language()
        self.select_hindi_language()
        self.select_marathi_language()
        self.click_on_checkbox()
        self.click_on_delete_btn()

    def verify_file_attachment_operation(self):
        self.click_on_attachment_add_button()
        self.select_file_to_be_uploaded()
        self.click_on_upload_button()
        self.click_on_attachment_checkbox()
        self.click_on_delete_attachment_button()

    def verify_info_page_elements(self,first_name, middle_name, last_name, father_name, mother_name):
        self.enter_all_personal_info(first_name, middle_name, last_name, father_name, mother_name)
        self.verify_addition_and_deletion_of_languages()
        self.verify_file_attachment_operation()











