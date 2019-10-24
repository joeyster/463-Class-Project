class Item():
    def __init__(self, item_id, name, quantity, length, width):
        self.item_id = item_id  # 001
        self.name = name  # laptop
        self.quantity = quantity
        self.length = length
        self.width = width
        self.area = length * width
        self.warehouse_rect = None

    def __str__(self):
        return self.item_id

    def __repr__(self):
        return self.item_id
