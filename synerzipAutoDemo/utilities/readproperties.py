import configparser


config=configparser.RawConfigParser()
config.read(".//configurations//config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('common info','baseURL')
        return  url

    @staticmethod
    def getUserName():
        usr = config.get('common info', 'username')
        return usr

    @staticmethod
    def getPassword():
        pwd = config.get('common info', 'password')
        return pwd

    @staticmethod
    def getInvalidUserName():
        invalidusr = config.get('common info', 'invalidusername')
        return invalidusr

    @staticmethod
    def getInvalidPassword():
        invalidpwd = config.get('common info', 'invalidpassword')
        return invalidpwd

    @staticmethod
    def getExpectedTitleOfPage():
        title = config.get('common info', 'page_title')
        return title

    @staticmethod
    def getExpectedInvaliCredentialMessage():
        message = config.get('common info', 'invalid_message')
        return message

    @staticmethod
    def getExpectedBackGroundColor():
        color = config.get('common info', 'calender_bc_color')
        return color

    @staticmethod
    def getExpectedLeaveBalance():
        leave = config.get('common info', 'leave_balance')
        return leave

    @staticmethod
    def getEmployeeName():
        name = config.get('common info', 'emp_name')
        return name

    @staticmethod
    def getEmployeeId():
        id = config.get('common info', 'emp_id')
        return id

    @staticmethod
    def getExpectedEmployeeDetails():
        empdetails = config.get('common info', 'emp_details')
        return empdetails

    @staticmethod
    def getFirstName():
        fstname = config.get('common info', 'first')
        return fstname

    @staticmethod
    def getMiddleName():
        midname = config.get('common info', 'middle')
        return midname

    @staticmethod
    def getLastName():
        lstname = config.get('common info', 'last')
        return lstname

    @staticmethod
    def getFatherName():
        fathname = config.get('common info', 'father')
        return fathname

    @staticmethod
    def getMotherName():
        mothname = config.get('common info', 'mother')
        return mothname

    @staticmethod
    def getLangRecords():
        records = config.get('common info', 'lang_records')
        return records

    @staticmethod
    def getLangEnglish():
        english = config.get('common info', 'English_lang')
        return english

    @staticmethod
    def getLangHindi():
        hindi = config.get('common info', 'Hindi_lang')
        return hindi

    @staticmethod
    def getLangMarathi():
        marathi = config.get('common info', 'Marathi_lang')
        return marathi

    @staticmethod
    def getReviewerName():
        reviewer = config.get('common info', 'Reviewer_name')
        return reviewer

    @staticmethod
    def getMonthFrom():
        fmonth = config.get('common info', 'From_month')
        return fmonth

    @staticmethod
    def getYearFrom():
        fyear = config.get('common info', 'From_year')
        return fyear

    @staticmethod
    def getMonthTo():
        tmonth = config.get('common info', 'To_month')
        return tmonth

    @staticmethod
    def getYearTo():
        tyear = config.get('common info', 'To_year')
        return tyear
