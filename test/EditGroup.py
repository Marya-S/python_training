from model.group import Group


def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit(Group(name="New_Edit_group2", footer="Edit group2", header="Edit_group_header2"))
    app.session.logout()