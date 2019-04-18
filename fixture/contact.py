from model.contact import Contact
class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.open_new_contact()
        self.fill_contact(contact)
        wd.find_element_by_name("submit").click()

    def delete(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@type ='checkbox'][1]").click()
        wd.find_element_by_xpath("//input[@value = 'Delete']").click()
        wd.switch_to_alert().accept()

    def edit(self, contact):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_xpath("//input[@type ='checkbox'][1]").click()
        wd.find_element_by_xpath("//tr[@name ='entry'][1]//img[@title='Edit']").click()
        self.fill_contact(contact)
        wd.find_element_by_xpath("//input[@value = 'Update']").click()

    def fill_contact(self, contact):
        wd = self.app.wd
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

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_xpath("//td[@class ='center'][1]"))

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_xpath("//a[@title=\"Sort on “Last name”\"]")) > 0):
            wd.find_element_by_link_text("home").click()

    def open_new_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def get_contact_list(self):
        wd = self.app.wd
        self.open_home_page()
        contacts=[]
        for element in wd.find_elements_by_xpath("//tr[@name=\"entry\"]"):
            id = element.find_element_by_name('selected[]').get_attribute("value")
            lastname = element.find_element_by_xpath("//tr[@name=\"entry\"]/td[2]").text
            firstname = element.find_element_by_xpath("//tr[@name=\"entry\"]/td[3]").text
            contacts.append(Contact(id=id, firstname=firstname, lastname=lastname))
        return contacts

