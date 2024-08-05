import pytest
from pages.login_page import LoginPage

def test_login_success(browser):
    browser.get("http://demo.testarena.pl/zaloguj")
    login_page = LoginPage(browser)
    login_page.login("administrator@testarena.pl", "sumXQQ72$L")
    assert login_page.is_logged_in()
