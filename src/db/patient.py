class NodePatient:
    def _init_(self, name,cc,password,phone,address,birthday,city):
        self.name = name
        self.cc = cc
        self.password = password
        self.phone = phone
        self.address = address
        self.birthday = birthday
        self.city = city
        self.role = None
        self.next = None