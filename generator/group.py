from model.group import Group
import random
import string
import os
import jsonpickle


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Group(name="", footer="", header="")] + [
    Group(name=random_string("group_name", 10), header=random_string("group_header", 15),
          footer=random_string("group_footer", 15))
    for i in range(3)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/groups.json")
jsonpickle.set_encoder_options('json', indent=2)
with open(file, "w") as f:
    f.write(jsonpickle.encode(testdata))
