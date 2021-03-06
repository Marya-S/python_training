import pymysql
from model.group import Group
from model.contact import Contact


class DBFixture():
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password= password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list=[]
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, email, email2, email3, home, mobile, work, "
                           "phone2 from addressbook WHERE deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, email, email2, email3, home, mobile, work,
                           phone2) = row
                list.append(Contact(firstname=firstname, lastname=lastname, id=id, homenumber=home, mobilenumber=mobile,
                       worknumber=work, secondarynumber=phone2,  firstemail=email,
                       secondemail=email2, therdemail=email3, address=address))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()