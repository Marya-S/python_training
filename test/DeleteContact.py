from model.contact import Contact
import time
import random


def test_delete_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(
            Contact(firstname="Del", lastname="Del", homenumber="84997774747", mobilenumber="89051114512"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    time.sleep(3)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

