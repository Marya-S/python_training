from model.contact import Contact
import time
from random import randrange


def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(firstname="Del", lastname="Del", homenumber="84997774747", mobilenumber="89051114512"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    time.sleep(3)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts
