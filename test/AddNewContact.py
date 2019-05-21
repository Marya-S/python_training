from model.contact import Contact


def test_create_contact(app, json_contacts, db, check_ui):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.create(contact)
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        def clean(contact):
            return Contact(firstname=contact.firstname.strip(), lastname=contact.lastname.strip(), id=contact.id,
                           homenumber=contact.homenumber, mobilenumber=contact.mobilenumber,
                           worknumber=contact.worknumber,
                           secondarynumber=contact.secondarynumber, firstemail=contact.firstemail,
                           secondemail=contact.secondemail, therdemail=contact.therdemail,
                           address=contact.address.strip())
        new_contacts = map(clean, db.get_contact_list())
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)




