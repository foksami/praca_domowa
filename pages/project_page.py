from selenium.webdriver.common.by import By

class ProjectPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_task_button = driver.find_element(By.LINK_TEXT, "Add Task")

    def add_task(self, task_name):
        self.add_task_button.click()
        task_name_input = self.driver.find_element(By.ID, "task_name")
        task_name_input.send_keys(task_name)
        save_button = self.driver.find_element(By.XPATH, "//input[@id='login']")
        save_button.click()

    def is_task_added(self, task_name):
        return task_name in self.driver.page_source
