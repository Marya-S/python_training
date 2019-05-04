from model.contact import Contact
import random
import string
import os
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", lastname="", homenumber="", mobilenumber="")]  + [
    Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 15),
            homenumber=random_string("home", 15), mobilenumber=random_string("mobile", 15))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
jsonpickle.set_encoder_options('json', indent=2)
with open(file, "w") as out:
    out.write(jsonpickle.encode(testdata))