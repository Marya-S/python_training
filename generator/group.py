from model.group import Group
import random
import string
import os
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Group(name="", footer="", header="")] + [
    Group(name=random_string("group_name", 10), header=random_string("group_header", 15),
          footer=random_string("group_footer", 15))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
jsonpickle.set_encoder_options('json', indent=2)
with open(file, "w") as out:
    out.write(jsonpickle.encode(testdata))
