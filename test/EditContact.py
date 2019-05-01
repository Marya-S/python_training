from model.contact import Contact
from random import randrange


def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(firstname="Del", lastname="Del", homenumber="84997774747", mobilenumber="89051114512"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Irina", lastname="Ivanova", homenumber="84997774747", mobilenumber="89051114512")
    contact.id = old_contacts[index].id
    app.contact.edit_group_by_index(contact, index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
