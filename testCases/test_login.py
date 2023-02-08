from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig


class Test_login_001:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        actTitle = self.driver.title
        if actTitle == "Guru99 Bank Manager HomePage":
            assert True
            print("...................Test is passed")
            self.driver.close()
        else:
            print("...................Test is failed")
            self.driver.close()
