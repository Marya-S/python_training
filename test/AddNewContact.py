from model.contact import Contact


def test_create_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Irina", lastname="Ivanova", homenumber="84997774747", mobilenumber="89051114512")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_create_second_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Sergey", lastname="Petrov", homenumber="84951234312", mobilenumber="890311143443")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list(contact)
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
