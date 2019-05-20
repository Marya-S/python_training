from fixture.orm import ORMFixture
from random import randrange
db = ORMFixture(host='127.0.0.1', name='addressbook', user='root', password='')


def test_add_contact_in_group(app):
    gr_index = randrange(len(app.group.get_group_list()))
    group = app.group.get_group_list()[gr_index]
    contact_not_in_group = db.contacts_not_in_group(group)
    con_index = randrange(len(contact_not_in_group))
    contact = contact_not_in_group[con_index]
    app.contact.add_contact_in_group(contact, group)
    assert (contact in db.contacts_in_group(group))
