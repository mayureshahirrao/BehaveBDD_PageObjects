from features.page_objects.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open(self, url):
        self.driver.get(url)

    def get_page_title(self):
        return self.driver.title

    def validate_page_title(self, expected_title):
        actual_title = self.get_page_title()
        assert expected_title in actual_title, f"Expected title '{expected_title}' not found in actual title '{actual_title}'"

    def set_name(self, name):
        self.enter_value('name_NAME', name, self.config_file_path)

    def set_phone_number(self, phone_num):
        self.enter_value('phone_CSS', phone_num, self.config_file_path)

    def set_email(self, email):
        self.enter_value('email_XPATH', email, self.config_file_path)

    def set_country(self, country):
        self.select_dropdown('country_XPATH', country, self.config_file_path)

    def set_city(self, city):
        self.enter_value('city_XPATH', city, self.config_file_path)

    def set_username(self, username):
        self.enter_value('username_XPATH', username, self.config_file_path)

    def set_password(self, password):
        self.enter_value('password_XPATH', password, self.config_file_path)

    def submit_form(self):
        self.click('submit_XPATH', self.config_file_path)
