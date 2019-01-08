import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, InvalidArgumentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException

class TestLogin():
    @pytest.fixture()

    def test_setup(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("https://app.stage.nectain.com")
        print(" >> Tests Suit Start << ")
        yield
        # driver.close()
        # driver.quit()
        print(" \n >> Tests Suit Complete << ")

    def test_login(self, test_setup):
        # driver.get("http://corporate-nectain.eastus.cloudapp.azure.com")
        assert "Nectain" in driver.title
        assert "Nectain" in driver.find_element_by_class_name('login_title').text
        assert "Nectain" in driver.find_element_by_css_selector('.login_title').text
        driver.find_element_by_id('login').send_keys("admin")
        driver.find_element_by_id('password').send_keys("admin")
        driver.find_element_by_id('loginSubmitAuth').click()
        wait = WebDriverWait(driver, 10)
        driver.implicitly_wait(10)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'nc-sidebar__logo__logo-normal')))
        print(" >> Test Login << ")

        # >> DEMAND PLANING <<
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'nc-sidebar__logo__triangle')))
        driver.find_element_by_class_name('nc-sidebar__logo__triangle').click()
        button_nectaine = driver.find_element_by_xpath('//div[contains(text(), "Nectain") and @class="nc-sidebar__desktops__item"]')
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, '//div[contains(text(), "Nectain") and @class="nc-sidebar__desktops__item"]')))
        assert "Nectain" in button_nectaine.text
        button_nectaine.click()
        button_eplaning = driver.find_element_by_xpath(
            '//div[@class="el-submenu__title"]/following::div//span[contains(text(), "E-Planning") and @class="el-submenu__name"]')
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, '//div[@class="el-submenu__title"]/following::div//span[contains(text(), "E-Planning") and @class="el-submenu__name"]')))
        button_eplaning.click()
        button_demand = driver.find_element_by_xpath(
            '//li[@class="el-submenu is-opened selected-item"]/ul[@role="menu"]/span/li[contains(text(), "Demand Planning") and @class="el-menu-item"]')
        wait.until(EC.visibility_of_element_located(
            (By.XPATH,
             '//li[@class="el-submenu is-opened selected-item"]/ul[@role="menu"]/span/li[contains(text(), "Demand Planning") and @class="el-menu-item"]')))
        button_demand.click()
        button_import_from_exel = driver.find_element_by_xpath(
            '//span[@class="x-btn-icon-el  x-btn-glyph" and @role="presentation" and @id="button-1082-btnIconEl"]')
        wait.until(EC.visibility_of_element_located(
            (By.XPATH,
             '//span[@class="x-btn-icon-el  x-btn-glyph" and @role="presentation" and @id="button-1082-btnIconEl"]')))
        button_import_from_exel.click()
        print(" >> Test Demand Open << ")
        wait.until(EC.visibility_of_element_located(
            (By.XPATH,
             '//div[@class="el-upload-dragger"]')))
        path_to_file = 'C:/Users/zhurba/PycharmProjects/test-nectaine/tests/test-bdg.xlsx'
        # FOR LINUX or WIN SHOULD CHANGE THE PATH
        # C:/Users/zhurba/PycharmProjects/test-nectaine/tests/test-bdg.xlsx
        # /home/alina/PycharmProjects/test-nectaine/tests/test-bdg.xlsx
        driver.find_element_by_xpath('//input[@class="el-upload__input"]').send_keys(path_to_file)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH,
             '//span[@class="el-dialog__title" and contains(text(), "Select a sheet")]')))
        driver.find_element_by_xpath('//*[@class="el-radio__inner"]').click()
        driver.find_element_by_xpath('//*[@class="el-dialog__body"]//*[@type="button"]').click()



        wait.until(EC.visibility_of_element_located(
            (By.XPATH,
             '//button[@class="excel-import__finish-btn el-tooltip"]')))
        wait.until(EC.element_to_be_clickable(
            (By.XPATH,
             '//button[@class="excel-import__finish-btn el-tooltip"]')))
        while True:
            try:
                driver.find_element_by_xpath('//button[@class="excel-import__finish-btn el-tooltip"]').click()
                x = wait.until(EC.visibility_of_element_located(
                    (By.XPATH, '//div[@class="nc__popup__title"]')))
                if x.is_displayed():
                    assert "Upload confirmation" in driver.find_element_by_xpath(
                        '//div[@class="nc__popup__title"]').text
                    break
            except (TimeoutException, InvalidArgumentException):
                continue

        driver.find_element_by_xpath('//button[@class="nc__btn nc__btn__default"]').click()

        # wait.until(EC.text_to_be_present_in_element_value(
        #     (By.XPATH, '//div[@role="alert" and @class="el-message el-message--success is-closable"]'),
        #     "Data successfully added!"))

        wait.until(EC.visibility_of_element_located(
            (By.XPATH,
             '//div[contains(text(), "Demand Items") and @class="nc__tab__title"]')))



        print(" >> Test Demand Upload << ")
        driver.implicitly_wait(10)
        print(" >> Test Demand Complete<< ")

