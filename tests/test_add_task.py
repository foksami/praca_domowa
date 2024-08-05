import pytest
from pages.login_page import LoginPage
from pages.project_page import ProjectPage


def test_add_task(browser):
    browser.get("http://demo.testarena.pl/zaloguj")
    login_page = LoginPage(browser)
    login_page.login("administrator@testarena.pl", "sumXQQ72$L")

    # Navigate to the specific project URL after login
    browser.get("http://demo.testarena.pl/GRU/tasks/1/task_due_date/asc?assignee=1&skipSavedFilter&status=1")

    project_page = ProjectPage(browser)
    task_name = "Nowe Zadanie"
    project_page.add_task(task_name)
    assert project_page.is_task_added(task_name)
