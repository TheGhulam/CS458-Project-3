import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginTestCases(unittest.TestCase):

    def setUp(self):
        """Setup the test environment before each test."""
        self.driver = webdriver.Edge()
        self.driver.get("https://cs458.gahmed.com")

    def test_successful_login(self):
        """Test user can login successfully with correct credentials."""
        driver = self.driver
        driver.find_element(By.NAME, "email").send_keys("test@gmail.com")
        driver.find_element(By.NAME, "password").send_keys("1")
        driver.find_element(By.XPATH, "//button[contains(text(),'Sign in Now')]").click()
        WebDriverWait(driver, 10).until(EC.url_contains("/home"))

    def test_invalid_login(self):
        """Test system behavior with invalid login credentials."""
        driver = self.driver
        driver.find_element(By.NAME, "email").send_keys("wrong@example.com")
        driver.find_element(By.NAME, "password").send_keys("wrongpassword")
        driver.find_element(By.XPATH, "//button[contains(text(),'Sign in Now')]").click()
       
        WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(@class,'Toastify__toast--error')]"))
        )
        error_message = driver.find_element(By.XPATH, "//div[contains(@class,'Toastify__toast--error')]")
        self.assertIn("Invalid credentials", error_message.text)
   
    def test_login_with_enter(self):
        """Test login functionality by pressing Enter key."""
        driver = self.driver
        driver.find_element(By.NAME, "email").send_keys("test@gmail.com")
        driver.find_element(By.NAME, "password").send_keys("1" + Keys.ENTER)
        WebDriverWait(driver, 10).until(EC.url_contains("/home"))

    def test_incorrect_email_field_format(self):
        """Test validation messages for incorrect email field format."""
        driver = self.driver
        driver.find_element(By.NAME, "email").send_keys("test.gmail")

        email_error = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "p.MuiFormHelperText-root.Mui-error"))
        )
        self.assertIn("Invalid email", email_error.text)

    def test_empty_fields(self):
        """Test validation messages for empty fields."""
        driver = self.driver
        driver.find_element(By.XPATH, "//button[contains(text(),'Sign in Now')]").click()

        email_error = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "p.MuiFormHelperText-root.Mui-error"))
        )
        self.assertIn("Invalid email", email_error.text)

        all_errors = WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "p.MuiFormHelperText-root.Mui-error"))
        )
        password_error = all_errors[1] if len(all_errors) > 1 else None
        self.assertIn("String must contain at least 1 character(s)", password_error.text if password_error else "")

    # def test_google_login(self):
    #     """Test logging in using Google OAuth."""
    #     driver = self.driver
    #     main_window_handle = driver.current_window_handle

    #     WebDriverWait(driver, 10).until(
    #         EC.element_to_be_clickable((By.XPATH, "//div[@role='button'][@aria-labelledby='button-label']"))
    #     )

    #     google_sign_in_button = driver.find_element(By.XPATH, "//div[@role='button'][@aria-labelledby='button-label']")
    #     google_sign_in_button.click()

    #     WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

    #     google_login_window_handle = [handle for handle in driver.window_handles if handle != main_window_handle][0]
    #     driver.switch_to.window(google_login_window_handle)

    #     WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "identifierId"))).send_keys("test@gmail.com")
    #     driver.find_element(By.ID, "identifierNext").click()

    #     WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "password"))).send_keys("1")
    #     driver.find_element(By.ID, "passwordNext").click()

    #     WebDriverWait(driver, 20).until(EC.number_of_windows_to_be(1))
    #     driver.switch_to.window(main_window_handle)

    #     WebDriverWait(driver, 10).until(EC.url_contains("/home"))

    def test_ui_elements_presence(self):
        """Check all UI elements are present."""
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email")))
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Sign in Now')]")))

    def tearDown(self):
        """Tear down the test environment after each test."""
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()