class Customer:
    def __init__(self, name: str, surname: str, balance: int, id=0):
        self.id = id
        self.name = name
        self.surname = surname
        self.balance = balance


        @property
        def get_id(self):
            return self.id
        