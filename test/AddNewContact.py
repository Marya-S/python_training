from model.contact import Contact


def test_create_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Irina", lastname="Ivanova", homenumber="84997774747", mobilenumber="89051114512"))
    app.session.logout()

