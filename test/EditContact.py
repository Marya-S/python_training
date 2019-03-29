from model.contact import Contact


def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit(Contact(firstname="IrinaNew", lastname="IvanovaNew", homenumber="84997774747", mobilenumber="89051114512"))
    app.session.logout()