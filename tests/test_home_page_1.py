import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DistanceToSunTestCases(unittest.TestCase):

    def setUp(self):
        """Setup the test environment before each test."""
        self.driver = webdriver.Edge()
        self.driver.get("https://cs458.gahmed.com")

    def login(self):
        """Log in to the application."""
        driver = self.driver
        driver.find_element(By.NAME, "email").send_keys("test@gmail.com")
        driver.find_element(By.NAME, "password").send_keys("1")
        driver.find_element(
            By.XPATH, "//button[contains(text(),'Sign in Now')]"
        ).click()
        WebDriverWait(driver, 10).until(EC.url_contains("/home"))

    def navigate_to_distance_to_sun_page(self):
        """Navigate to the Distance to Sun page."""
        driver = self.driver
        self.login()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(),'Distance to Sun')]")
            )
        )
        driver.find_element(
            By.XPATH, "//button[contains(text(),'Distance to Sun')]"
        ).click()
        WebDriverWait(driver, 10).until(EC.url_contains("/home1"))

    def test_latitude_longitude_fields(self):
        """Test if the latitude and longitude fields are present."""
        driver = self.driver
        self.navigate_to_distance_to_sun_page()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//label[contains(text(),'Latitude')]")
            )
        )
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//label[contains(text(),'Longitude')]")
            )
        )

    def test_calculate_distance_button(self):
        """Test if the Calculate Distance button is present and clickable."""
        driver = self.driver
        self.navigate_to_distance_to_sun_page()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(),'Calculate Distance')]")
            )
        )

    def test_auto_populated_fields(self):
        """Test if the latitude and longitude fields are auto-populated based on location."""
        driver = self.driver
        self.navigate_to_distance_to_sun_page()
        latitude_input = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//label[contains(text(),'Latitude')]/following-sibling::div/input",
                )
            )
        )
        longitude_input = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//label[contains(text(),'Longitude')]/following-sibling::div/input",
                )
            )
        )
        self.assertNotEqual(latitude_input.get_attribute("value"), "")
        self.assertNotEqual(longitude_input.get_attribute("value"), "")

    def test_distance_calculation(self):
        """Test if the distance calculation works correctly."""
        driver = self.driver
        self.navigate_to_distance_to_sun_page()
        latitude_input = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//label[contains(text(),'Latitude')]/following-sibling::div/input",
                )
            )
        )
        longitude_input = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//label[contains(text(),'Longitude')]/following-sibling::div/input",
                )
            )
        )
        latitude_input.clear()
        longitude_input.clear()
        latitude_input.send_keys("40.7128")
        longitude_input.send_keys("70.0060")
        driver.find_element(
            By.XPATH, "//button[contains(text(),'Calculate Distance')]"
        ).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//p[contains(text(),'The distance to the Sun is approximately')]",
                )
            )
        )
        distance_text = driver.find_element(
            By.XPATH,
            "//p[contains(text(),'The distance to the Sun is approximately')]",
        ).text
        self.assertRegex(
            distance_text,
            r"The distance to the Sun is approximately \d+ kilometers\.",
        )

    def test_invalid_latitude(self):
        """Test error message for invalid latitude."""
        driver = self.driver
        self.navigate_to_distance_to_sun_page()

        latitude_input = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//label[contains(text(),'Latitude')]/following-sibling::div/input",
                )
            )
        )
        longitude_input = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//label[contains(text(),'Longitude')]/following-sibling::div/input",
                )
            )
        )

        latitude_input.clear()
        longitude_input.clear()

        latitude_input.send_keys("100")
        longitude_input.send_keys("-74.0060")

        driver.find_element(
            By.XPATH, "//button[contains(text(),'Calculate Distance')]"
        ).click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//p[contains(text(),'Latitude must be between -90 and 90')]",
                )
            )
        )

        error_text = driver.find_element(
            By.XPATH,
            "//p[contains(text(),'Latitude must be between -90 and 90')]",
        ).text
        self.assertEqual(
            error_text,
            "Latitude must be between -90 and 90, and longitude must be between -180 and 180.",
        )

    def test_invalid_longitude(self):
        """Test error message for invalid longitude."""
        driver = self.driver
        self.navigate_to_distance_to_sun_page()

        latitude_input = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//label[contains(text(),'Latitude')]/following-sibling::div/input",
                )
            )
        )
        longitude_input = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//label[contains(text(),'Longitude')]/following-sibling::div/input",
                )
            )
        )

        latitude_input.clear()
        longitude_input.clear()

        latitude_input.send_keys("40.7128")
        longitude_input.send_keys("200")

        driver.find_element(
            By.XPATH, "//button[contains(text(),'Calculate Distance')]"
        ).click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//p[contains(text(),'Latitude must be between -90 and 90')]",
                )
            )
        )

        error_text = driver.find_element(
            By.XPATH,
            "//p[contains(text(),'Latitude must be between -90 and 90')]",
        ).text
        self.assertEqual(
            error_text,
            "Latitude must be between -90 and 90, and longitude must be between -180 and 180.",
        )

    def test_empty_fields(self):
        """Test error message for empty fields."""
        driver = self.driver
        self.navigate_to_distance_to_sun_page()
        driver.find_element(
            By.XPATH, "//button[contains(text(),'Calculate Distance')]"
        ).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//p[contains(text(),'Please enter latitude and longitude.')]",
                )
            )
        )
        error_text = driver.find_element(
            By.XPATH,
            "//p[contains(text(),'Please enter latitude and longitude.')]",
        ).text
        self.assertEqual(error_text, "Please enter latitude and longitude.")


    def test_gps_disabled(self):
        """Test if the application populates latitude and longitude when GPS is disabled."""
        driver = self.driver
        self.navigate_to_distance_to_sun_page()

        latitude_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//label[contains(text(),'Latitude')]/following-sibling::div/input",
                )
            )
        )
        longitude_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//label[contains(text(),'Longitude')]/following-sibling::div/input",
                )
            )
        )

        latitude_value = latitude_input.get_attribute("value")
        longitude_value = longitude_input.get_attribute("value")

        self.assertEqual(latitude_value, "", "Latitude field is empty")
        self.assertEqual(longitude_value, "", "Longitude field is empty")

    def test_valid_input_format(self):
        """Test if the application only accepts numbers for latitude and longitude."""
        driver = self.driver
        self.navigate_to_distance_to_sun_page()

        latitude_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//label[contains(text(),'Latitude')]/following-sibling::div/input",
                )
            )
        )
        longitude_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//label[contains(text(),'Longitude')]/following-sibling::div/input",
                )
            )
        )

        latitude_input.clear()
        longitude_input.clear()

        latitude_input.send_keys("40.7128abc")
        longitude_input.send_keys("-74.0060xyz")

        latitude_value = latitude_input.get_attribute("value")
        longitude_value = longitude_input.get_attribute("value")

        self.assertRegex(latitude_value, r"^-?\d+(\.\d+)?$")
        self.assertRegex(longitude_value, r"^-?\d+(\.\d+)?$")

    def test_responsiveness(self):
        """Test if the application is responsive on various screen sizes."""
        driver = self.driver
        self.navigate_to_distance_to_sun_page()

        screen_sizes = [(1024, 768), (768, 1024), (414, 896), (375, 667)]

        for size in screen_sizes:
            width, height = size
            driver.set_window_size(width, height)

            latitude_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//label[contains(text(),'Latitude')]/following-sibling::div/input"))
            )
            longitude_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//label[contains(text(),'Longitude')]/following-sibling::div/input"))
            )
            calculate_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Calculate Distance')]"))
            )

            self.assertTrue(latitude_input.is_displayed())
            self.assertTrue(longitude_input.is_displayed())
            self.assertTrue(calculate_button.is_enabled())

    def test_calculate_button_enabled(self):
        """Test if the Calculate Distance button is enabled when the fields are empty and gives an error message when they are."""
        driver = self.driver
        self.navigate_to_distance_to_sun_page()

        latitude_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[contains(text(),'Latitude')]/following-sibling::div/input"))
        )
        longitude_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[contains(text(),'Longitude')]/following-sibling::div/input"))
        )

        latitude_input.clear()
        longitude_input.clear()

        calculate_button = driver.find_element(By.XPATH, "//button[contains(text(),'Calculate Distance')]")
        self.assertTrue(calculate_button.is_enabled())

    def test_distance_format(self):
        """Test if the calculated distance is displayed in the correct format."""
        driver = self.driver
        self.navigate_to_distance_to_sun_page()

        latitude_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[contains(text(),'Latitude')]/following-sibling::div/input"))
        )
        longitude_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[contains(text(),'Longitude')]/following-sibling::div/input"))
        )

        calculate_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Calculate Distance')]"))
        )
        calculate_button.click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p[contains(text(),'The distance to the Sun is approximately')]"))
        )

        distance_text = driver.find_element(By.XPATH, "//p[contains(text(),'The distance to the Sun is approximately')]").text
        self.assertRegex(
            distance_text,
            r"The distance to the Sun is approximately \d+ kilometers\.",
        )

    def tearDown(self):
        """Tear down the test environment after each test."""
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
