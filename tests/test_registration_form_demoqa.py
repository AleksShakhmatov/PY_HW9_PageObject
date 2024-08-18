from pages.page_form_demoqa import RegistrationForm
from test_data.user import User


def test_registration_form_complete():
    page_form_demoqa = RegistrationForm()
    user = User(first_name='Coluchy', last_name='Aleksandr', email='AC@ya.com', gender='Male', user_number='4455667788',
                birthday='08 July,1986', subject='Computer Science', hobbies='Reading', picture='8.png',
                address='India', state='Rajasthan', city='Jaiselmer')
    page_form_demoqa.open()
    page_form_demoqa.register(user)
    page_form_demoqa.should_exact_text(user)
