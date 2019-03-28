# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="New_group2", footer="create group2", header="new_group_header2"))
    app.session.logout()
