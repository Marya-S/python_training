from model.contact import Contact
import re
from selenium.webdriver.support.ui import Select


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
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value = 'Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//input[@value = 'Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def edit_first_contact(self, contact):
        self.edit_contact_by_index(contact, 0)

    def edit_contact_by_index(self, contact, index):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()
        self.fill_contact(contact)
        wd.find_element_by_xpath("//input[@value = 'Update']").click()
        self.contact_cache = None

    def edit_contact_by_id(self, id, contact):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_id(id)
        wd.find_element_by_xpath('//input[@id="%s"]/following::td[7]/a' % id).click()
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
        if not (wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_xpath("//a[@title='Sort on “Last name']")) > 0):
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
            for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
                cells = wd.find_elements_by_tag_name("td")
                id = element.find_element_by_name('selected[]').get_attribute("value")
                lastname = element.find_element_by_xpath(".//td[2]").text
                firstname = element.find_element_by_xpath(".//td[3]").text
                address = element.find_element_by_xpath(".//td[4]").text
                all_phones = element.find_element_by_xpath(".//td[6]").text
                all_emails = element.find_element_by_xpath(".//td[5]").text
                self.contact_cache.append(Contact(id=id, firstname=firstname, lastname=lastname,
                                                  all_phones_from_home_page=all_phones,
                                                  all_email_from_home_page=all_emails, address=address))
        return list(self.contact_cache)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name('selected[]')[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector('input[value="%s"]' % id).click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def open_contact_edit_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homenumber = wd.find_element_by_name("home").get_attribute("value")
        mobilenumber = wd.find_element_by_name("mobile").get_attribute("value")
        worknumber = wd.find_element_by_name("work").get_attribute("value")
        secondarynumber = wd.find_element_by_name("phone2").get_attribute("value")
        firstemail = wd.find_element_by_name("email").get_attribute("value")
        secondemail = wd.find_element_by_name("email2").get_attribute("value")
        therdemail = wd.find_element_by_name("email3").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, homenumber=homenumber, mobilenumber=mobilenumber,
                       worknumber=worknumber, secondarynumber=secondarynumber,  firstemail=firstemail,
                       secondemail=secondemail, therdemail=therdemail, address=address)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homenumber = re.search("H: (.*)", text).group(1)
        mobilenumber = re.search("M: (.*)", text).group(1)
        worknumber = re.search("W: (.*)", text).group(1)
        secondarynumber = re.search("P: (.*)", text).group(1)
        return Contact(homenumber=homenumber, mobilenumber=mobilenumber,
                       worknumber=worknumber, secondarynumber=secondarynumber)

    def add_contact_in_group(self, contact, group):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_id(contact.id)
        Select(wd.find_element_by_name("to_group")).select_by_value(group.id)
        wd.find_element_by_name("add").click()





