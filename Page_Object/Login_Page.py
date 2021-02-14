class login_page():

    # Locators
    username_input = "txtUsername"
    password_input = "txtPassword"
    login_btn = "btnLogin"
    welcome_user_label = "welcome"

    def __init__(self, driver):
        self.driver = driver

    # Actions
    def login_in_app(self, username, password):
        username_field = self.driver.find_element_by_id(self.username_input)
        username_field.send_keys(username)

        password_field = self.driver.find_element_by_id(self.password_input)
        password_field.send_keys(password)

        login_button = self.driver.find_element_by_id(self.login_btn)
        login_button.click()

    def is_login_successful(self):
        welcome_user_field = self.driver.find_element_by_id(self.welcome_user_label).is_displayed()
        return welcome_user_field


