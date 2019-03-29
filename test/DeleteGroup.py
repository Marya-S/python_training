# удаление первой группы


def test_delete_group(app):
    app.session.login(username="admin", password="secret")
    app.group.delete()
    app.session.logout()