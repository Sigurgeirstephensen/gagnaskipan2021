class Contact:
    def __init__(self, name="", phone=0):
        self.name = name
        self.phone = phone


class DoubleKeyContainer:
    def __init__(self):
        self.names = {}
        self.phones = {}
        self.contacts = {}

    def add_contact(self, id, name, phone):
        if id not in self.contacts.keys():
            self.contacts[id] = Contact(name, phone)
            self.names[name] = id
            self.phones[phone] = id
        else:
            self.contacts[id].name = name
            self.contacts[id].phone = phone

    def get_name_by_id(self, id):
        if id in self.contacts.keys():
            return self.contacts[id].name
        else:
            return None

    def get_name_by_phone(self, phone):
        if phone in self.phones.keys():
            p_id = self.phones[phone]
            if p_id in self.contacts.keys():
                return self.get_name_by_id(p_id)
        else:
            return None

    def remove(self, id):
        if id in self.contacts.keys():
            name, phone = self.contacts[id].name, self.contacts[id].phone
            del self.names[name]
            del self.phones[phone]
            del self.contacts[id]
        else:
            pass


if __name__ == "__main__":

    print("TESTING DOUBLE KEY - MAKE BETTER TESTS!!!\n")

    dkc = DoubleKeyContainer()
    dkc.add_contact(23, "Kári", 23543)
    dkc.add_contact(21, "Sigurður", 12342153)
    dkc.add_contact(13, "Kristmundur", 63567356)
    dkc.add_contact(87, "Eysteinn", 73345)
    dkc.add_contact(3, "Hrafn", 93543)
    dkc.add_contact(24, "Jónni", 8624686)

    print(dkc.get_name_by_id(13))
    print(dkc.get_name_by_phone(23543))
    print(dkc.get_name_by_id(87))
    print(dkc.get_name_by_phone(73345))
    dkc.remove(87)
    print(dkc.get_name_by_id(87))
    print(dkc.get_name_by_phone(73345))

    print(dkc.get_name_by_id(24))
    print(dkc.get_name_by_phone(8624686))
    print(dkc.get_name_by_phone(4564684664866))
    dkc.remove(24)
    print(dkc.get_name_by_id(24))


