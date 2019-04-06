from model.contact import Contact


def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(firstname="Del", lastname="Del", homenumber="84997774747", mobilenumber="89051114512"))
    app.contact.delete()
