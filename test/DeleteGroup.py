# удаление первой группы
from model.group import Group


def test_delete_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="group_delete", footer="group_delete", header="group_delete"))
    app.group.delete()
