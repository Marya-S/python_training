from sys import maxsize


class Contact:
    def __init__(self, firstname=None, lastname=None, homenumber=None, mobilenumber=None, id=None,
                 secondarynumber=None, worknumber=None, all_phones_from_home_page=None, all_email_from_home_page=None,
                 firstemail=None, secondemail=None, therdemail=None, address=None):
        self.firstname = firstname
        self.lastname = lastname
        self.homenumber = homenumber
        self.mobilenumber = mobilenumber
        self.secondarynumber = secondarynumber
        self.worknumber = worknumber
        self.firstemail = firstemail
        self.secondemail = secondemail
        self.therdemail = therdemail
        self.address = address
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_email_from_home_page = all_email_from_home_page

    def __repr__(self):
        return "%s:%s" % (self.id, self.firstname)

    def __eq__(self, other):
        return (self.id == other.id or self.id is None or other.id is None) and self.firstname == other.firstname and \
               self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
