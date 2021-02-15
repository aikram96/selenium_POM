class login_page():

    # Locators
    username_input = "txtUsername"
    password_input = "txtPassword"
    login_btn = "btnLogin"
    welcome_user_label = "welcome"

    forgot_pass_link = '#forgotPasswordLink > a'
    forgot_pass_question = "Forgot"
    username_forgot_input = "securityAuthentication_userName"
    reset_pass_btn = "btnSearchValues"
    instructions_validation = "Sent"

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

    def forgot_section(self):
        forgot = self.driver.find_element_by_css_selector(self.forgot_pass_link)
        forgot.click()

    def is_forgot_link_successful(self):
        forgot_question = self.driver.find_element_by_partial_link_text(self.forgot_pass_question).is_results_found()
        return forgot_question

    def reset_password(self, username_validation):
        username_val = self.driver.find_element_by_id(self.username_forgot_input)
        username_val.send_keys(username_validation)

        reset_button = self.driver.find_element_by_id(self.reset_pass_btn)
        reset_button.click()

    def is_reset_successful(self):
        instructions_sent = self.driver.find_element_by_partial_link_text(self.instructions_validation).is_displayed()
        return instructions_sent




