from pages.registration_form_demoqa_page import RegistrationForm


def test_registration_form_demoqa():
    registration_form = RegistrationForm()
    registration_form.open()
    registration_form.type_first_name('Coluchy')
    registration_form.type_last_name('Aleksandr')
    registration_form.type_email('AC@ya.com')
    registration_form.click_gender()
    registration_form.type_phone('4455667788')
    registration_form.type_birthday()
    registration_form.type_subjects('Physics')
    registration_form.click_hobbies()
    registration_form.upload_photo('8.png')
    registration_form.type_address('India')
    registration_form.type_state('Rajasthan')
    registration_form.type_city('Jaiselmer')
    registration_form.press_submit()
    registration_form.should_text('Thanks for submitting the form')
    registration_form.should_exact_text('Coluchy Aleksandr',
                                        'AC@ya.com',
                                        'Male',
                                        '4455667788',
                                        '08 July,1986',
                                        'Computer Science',
                                        'Reading',
                                        'img.jpg',
                                        'Test, 65',
                                        'NCR Delhi')













    browser.open('/automation-practice-form')

    browser.element('#firstName').type('Coluchy')
    browser.element('#lastName').type('Aleksandr')
    browser.element('#userEmail').type('AC@ya.com')
    browser.element('[for="gender-radio-1"]').click()
    browser.element("#userNumber").type('4455667788')
    browser.element('#subjectsInput').type('computer').press_enter()
    browser.element('#dateOfBirthInput').perform(command.js.scroll_into_view).click()
    browser.element('.react-datepicker__month-select').click().element('[value="6"]').click()
    browser.element('.react-datepicker__year-select').click().element('[value="1986"]').click()
    browser.element('.react-datepicker__day--008').click()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('../8.png'))
    browser.element('#currentAddress').type('India').press_enter()
    browser.element("#react-select-3-input").type("Rajasthan").press_enter()
    browser.element("#react-select-4-input").type("Jaiselmer").press_enter()
    browser.element('#submit').press_enter()
    browser.element("#example-modal-sizes-title-lg").should(have.text('Thanks for submitting the form'))

    browser.element('.table').all('td').even.should(
        have.exact_texts('Coluchy Aleksandr', 'AC@ya.com', 'Male', '4455667788', '08 July,1986', 'Computer Science',
                         'Sports', '8.png', 'India', 'Rajasthan Jaiselmer'))
