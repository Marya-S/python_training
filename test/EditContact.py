from model.contact import Contact
import random


def test_edit_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(firstname="Del", lastname="Del", homenumber="84997774747", mobilenumber="89051114512"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact_up = Contact(firstname="Svetlana", lastname="Smirnova", homenumber="84997774747", mobilenumber="89051114512",
                         id=contact.id)
    app.contact.edit_contact_by_id(contact.id, contact_up)
    new_contacts = db.get_contact_list()
    index = old_contacts.index(contact)
    old_contacts[index] = contact_up
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


