from model.contact import Contact


def test_create_contact(app):
    app.contact.create(Contact(firstname="Irina", lastname="Ivanova", homenumber="84997774747", mobilenumber="89051114512"))


def test_create_second_contact(app):
    app.contact.create(Contact(firstname="Sergey", lastname="Petrov", homenumber="84951234312", mobilenumber="890311143443"))

