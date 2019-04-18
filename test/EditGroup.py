from model.group import Group


def test_edit_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="group_1", footer="group_1", header="group_1"))
    old_groups = app.group.get_group_list()
    group = Group(name="New_Edit_group2", footer="Edit group2", header="Edit_group_header2")
    group.id = old_groups[0].id
    app.group.edit(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

