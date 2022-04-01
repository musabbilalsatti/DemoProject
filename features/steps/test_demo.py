"""Facebook login feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

from features.support.login import LoginSupport

obj_login_support = LoginSupport()


@scenario('test.feature', 'Verify FB Login Functionality')
def test_verify_fb_login_functionality():
    """Verify FB Login Functionality."""


@given('User is on Facebook login page')
def user_is_on_facebook_login_page():
    """User is on Facebook login page."""
    obj_login_support.setUp()


@when('click on login button')
def click_on_login_button():
    """click on login button."""
    obj_login_support.click_login_button()


@when('user enters valid email and password')
def user_enters_valid_email_and_password():
    """user enters valid email and password."""
    obj_login_support.enter_email_password()


@then('verify user is loggedIn successfully')
def verify_user_is_loggedin_successfully():
    """verify user is loggedIn successfully."""
    assert obj_login_support.verify_user_loggedIn()
    obj_login_support.driver.quit()


