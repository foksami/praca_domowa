import pytest
from pages.login_page import LoginPage

def test_login_failure(browser):
    browser.get("http://demo.testarena.pl/zaloguj")
    login_page = LoginPage(browser)
    login_page.login("administrator@testarena.pl", "wrongpassword")
    assert not login_page.is_logged_in()
