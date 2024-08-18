from pathlib import Path

from selene import browser, have, command

from test_data.user import User


class RegistrationForm:
    def open(self):
        browser.open('automation-practice-form/')

    def type_first_name(self, first_name):
        browser.element('#firstName').type(first_name)

    def type_last_name(self, last_name):
        browser.element('#lastName').type(last_name)

    def type_email(self, email):
        browser.element('#userEmail').type(email)

    def click_gender(self):
        browser.element('[for="gender-radio-1"]').click()

    def type_user_number(self, user_number):
        browser.element('#userNumber').type(user_number)

    def type_subjects(self, subjects):
        browser.element('#subjectsInput').type(subjects).press_enter()

    def type_birthday(self):
        browser.element('#dateOfBirthInput').perform(command.js.scroll_into_view).click()
        browser.element('.react-datepicker__month-select').click().element('[value="6"]').click()
        browser.element('.react-datepicker__year-select').click().element('[value="1986"]').click()
        browser.element('.react-datepicker__day--008').click()

    def click_hobbies(self):
        browser.element('[for="hobbies-checkbox-2"]').click()

    def upload_picture(self, picture):
        browser.element('#uploadPicture').send_keys(str(Path(__file__).parent.parent.joinpath(f'resources/{picture}')))

    def type_address(self, address):
        browser.element('#currentAddress').type(address)

    def type_state(self, state):
        browser.element('#react-select-3-input').type(state).press_enter()

    def type_city(self, city):
        browser.element('#react-select-4-input').type(city).press_enter()

    def press_submit(self):
        browser.element('#submit').press_enter()

    def should_text(self, text):
        browser.element("#example-modal-sizes-title-lg").should(have.text(text))

    def should_exact_text(self, user: User):
        browser.element('.table').all('td').even.should(have.exact_texts(
            f'{user.first_name} {user.last_name}',
            f'{user.email}',
            f'{user.gender}',
            f'{user.user_number}',
            f'{user.birthday}',
            f'{user.subject}',
            f'{user.hobbies}',
            f'{user.picture}',
            f'{user.address}',
            f'{user.state} {user.city}'))

    def register(self, user: User):
        self.type_first_name(user.first_name)
        self.type_last_name(user.last_name)
        self.type_email(user.email)
        self.click_gender()
        self.type_user_number(user.user_number)
        self.type_birthday()
        self.type_subjects(user.subject)
        self.click_hobbies()
        self.upload_picture(user.picture)
        self.type_address(user.address)
        self.type_state(user.state)
        self.type_city(user.city)
        self.press_submit()
