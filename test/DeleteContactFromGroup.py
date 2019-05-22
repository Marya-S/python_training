from fixture.orm import ORMFixture
from fixture.contact import Contact
from fixture.group import Group
from random import randrange
db = ORMFixture(host='127.0.0.1', name='addressbook', user='root', password='')


def test_add_contact_in_group(app):
    if len(db.get_contact_list()) == 0:
        app.contact.create(
            Contact(firstname="Test", lastname="Test2", homenumber="84997774747", mobilenumber="89051114512"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="group_test", footer="group_test", header="group_test"))
    gr_index = randrange(len(app.group.get_group_list()))
    group = app.group.get_group_list()[gr_index]
    contact_in_group = db.contacts_in_group(group)
    if len(contact_in_group) == 0:
        index = randrange(len(app.contact.get_contact_list()))
        app.contact.add_contact_in_group(app.contact.get_contact_list()[index], group)
        contact = db.contacts_in_group(group)[0]
    else:
        con_index = randrange(len(contact_in_group))
        contact = contact_in_group[con_index]
    app.group.del_contact_in_group(contact, group)
    assert (contact in db.contacts_not_in_group(group))