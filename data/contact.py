from model.contact import Contact
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", lastname="", homenumber="", mobilenumber="")]  + [
    Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 15),
            homenumber=random_string("home", 15), mobilenumber=random_string("mobile", 15))
    for i in range(3)
]

