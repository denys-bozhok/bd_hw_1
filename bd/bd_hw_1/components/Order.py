class Orders:
    def __init__(self, dish_id: int, customer_id: int, id=0):
        self.id = id
        self.customer_id = customer_id
        self.dish_id = dish_id
