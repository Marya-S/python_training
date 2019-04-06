from model.contact import Contact


def test_edit_contact(app):
    app.contact.edit(Contact(firstname="IrinaNew", lastname="IvanovaNew", homenumber="84997774747", mobilenumber="89051114512"))
