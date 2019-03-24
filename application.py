from selenium import webdriver


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def return_group_page(self):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

    def create_new_group(self, group):
        wd = self.wd
        self.open_group_page()
        wd.find_element_by_name("new").click()
        # fiil group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # send form
        wd.find_element_by_name("submit").click()
        self.return_group_page()

    def open_group_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def open_start_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def login(self,username, password):
        wd = self.wd
        self.open_start_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@type='submit']").click()

    def destroy(self):
        self.wd.quit()