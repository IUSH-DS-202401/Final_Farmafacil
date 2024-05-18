class NodePharmacy:
    def __init__(self, name, nit, password, phone, address, admin, admin_cc):
        self.name = name
        self.nit = nit
        self.password = password
        self.phone = phone
        self.address = address
        self.admin = admin
        self.admin_cc = admin_cc
        self.next = None
        
