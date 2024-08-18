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
    registration_form.type_subjects('Computer Science')
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
                                        '8.png',
                                        'India',
                                        'Rajasthan Jaiselmer')
