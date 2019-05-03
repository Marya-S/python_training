from model.contact import Contact
class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.open_new_contact()
        self.fill_contact(contact)
        wd.find_element_by_name("submit").click()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.select_contact(index)
        wd.find_element_by_xpath("//input[@value = 'Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def edit_first_contact(self, contact):
        self.edit_contact_by_index(contact, 0)

    def edit_contact_by_index(self, contact, index):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact(index)
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()
        self.fill_contact(contact)
        wd.find_element_by_xpath("//input[@value = 'Update']").click()
        self.contact_cache = None

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

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache=[]
            for element in wd.find_elements_by_xpath("//tr[@name=\"entry\"]"):
                id = element.find_element_by_name('selected[]').get_attribute("value")
                lastname = element.find_element_by_xpath(".//td[2]").text
                firstname = element.find_element_by_xpath(".//td[3]").text
                self.contact_cache.append(Contact(id=id, firstname=firstname, lastname=lastname))
        return list(self.contact_cache)

    def select_contact(self, index):
        wd = self.app.wd
        wd.find_elements_by_name('selected[]')[index].click()

