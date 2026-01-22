import time

from behave import *

from Utilities import ConfigReader
from features.page_objects.registration_page import RegistrationPage


@given(u'I navigate to the url: "https://www.qa.way2automation.com/"')
def step_impl(context):
    context.reg = RegistrationPage(context.driver)
    context.reg.open(ConfigReader.read_config("basic info", "testsiteurl", context.reg.config_file_path))

@when(u'I validate the page title: {title}')
def step_impl(context, title):
    context.reg.validate_page_title(title)


@when(u'I enter the name as {name}')
def step_impl(context, name):
    context.reg.set_name(name)


@when(u'I enter the phone number as {phone_number}')
def step_impl(context, phone_number):
    context.reg.set_phone_number(phone_number)


@when(u'I enter the email as {email}')
def step_impl(context, email):
    context.reg.set_email(email)


@when(u'I enter the country as {country}')
def step_impl(context, country):
    context.reg.set_country(country)


@when(u'I enter the city as {city}')
def step_impl(context, city):
    context.reg.set_city(city)


@when(u'I enter the user name as {user_name}')
def step_impl(context, user_name):
    context.reg.set_username(user_name)


@when(u'I enter the password as {password}')
def step_impl(context, password):
    context.reg.set_password(password)


@when(u'I submit the registration form')
def step_impl(context):
    context.reg.submit_form()
    time.sleep(3)