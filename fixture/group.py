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

    def delete(self):
        wd = self.app.wd
        self.open_group_page()
        wd.find_element_by_xpath("//span[@class='group']/input[1]").click()
        wd.find_element_by_name("delete").click()

    def edit(self, group):
        wd = self.app.wd
        self.open_group_page()
        wd.find_element_by_xpath("//span[@class='group']/input[1]").click()
        wd.find_element_by_name("edit").click()
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
        wd.find_element_by_name("update").click()
        self.return_group_page()



    def open_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()