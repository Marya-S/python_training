from model.group import Group
class GroupHelper:

    def __init__(self, app):
        self.app = app

    def return_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        wd.find_element_by_name("new").click()
        # fiil group form
        self.fill_form(group)
        # send form
        wd.find_element_by_name("submit").click()
        self.return_group_page()
        self.group_cache = None

    def delete_first_group(self):
        self.delete_group_by_index(0)


    def fill_form(self, group):
        wd = self.app.wd
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    def edit_first_group(self, group):
        self.edit_group_by_index(group, 0)

    def edit_group_by_index(self, group, index):
        wd = self.app.wd
        self.open_group_page()
        self.select_group(index)
        wd.find_element_by_name("edit").click()
        # fiil group form
        self.fill_form(group)
        # send form
        wd.find_element_by_name("update").click()
        self.return_group_page()
        self.group_cache = None

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_xpath("//span[@class='group']/input[1]"))

    def open_group_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_group_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name('selected[]').get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_group_page()
        self.select_group(index)
        wd.find_element_by_name("delete").click()
        self.group_cache = None

    def select_group(self, index):
        wd = self.app.wd
        wd.find_elements_by_name('selected[]')[index].click()

