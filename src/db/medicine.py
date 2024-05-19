class NodeMedicine:
    def __init__(self, name, pharmacy, expiryDate, manufacturer,units):
        self.name = name
        self.pharmacy = pharmacy
        self.expiryDate = expiryDate
        self.manufacturer = manufacturer
        self.units = units
        self.next = None


