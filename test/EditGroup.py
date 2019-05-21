from model.group import Group
import random


def test_edit_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="group_1", footer="group_1", header="group_1"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    group_up = Group(name="New_Edit_group2", footer="Edit group2", header="Edit_group_header2", id=group.id)
    app.group.edit_group_by_id(group.id, group_up)
    new_groups = db.get_group_list()
    index = old_groups.index(group)
    old_groups[index] = group_up
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

