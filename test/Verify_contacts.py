import re
from model.contact import Contact


def test_verify_contacts(app, db):
    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    for i in range(len(contacts_from_home_page)):
        assert contacts_from_home_page[i].lastname == contacts_from_db[i].lastname
        assert contacts_from_home_page[i].firstname == contacts_from_db[i].firstname
        assert contacts_from_home_page[i].address == contacts_from_db[i].address
        assert contacts_from_home_page[i].all_phones_from_home_page == merge_phones_like_on_home_page(contacts_from_db[i])
        assert contacts_from_home_page[i].all_email_from_home_page == merge_email_like_on_home_page(contacts_from_db[i])


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x),
                                                  [contact.homenumber, contact.mobilenumber,
                                                   contact.worknumber, contact.secondarynumber])))


def merge_email_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x !="",[contact.firstemail, contact.secondemail, contact.therdemail]))