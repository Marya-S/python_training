class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.open_new_contact()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.homenumber)
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobilenumber)
        wd.find_element_by_name("submit").click()

    def delete(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@type ='checkbox'][1]").click()
        wd.find_element_by_xpath("//tr[@name ='entry'][1]//img[@title='Edit']").click()
        wd.find_element_by_xpath("//input[@value = 'Delete']").click()

    def edit(self, contact):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@type ='checkbox'][1]").click()
        wd.find_element_by_xpath("//tr[@name ='entry'][1]//img[@title='Edit']").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.homenumber)
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobilenumber)
        wd.find_element_by_xpath("//input[@value = 'Update']").click()

    def open_new_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()