from model.group import Group


def test_edit_group(app):

    app.group.edit(Group(name="New_Edit_group2", footer="Edit group2", header="Edit_group_header2"))
