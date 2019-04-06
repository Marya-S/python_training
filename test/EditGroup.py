from model.group import Group


def test_edit_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="group_1", footer="group_1", header="group_1"))
    app.group.edit(Group(name="New_Edit_group2", footer="Edit group2", header="Edit_group_header2"))
