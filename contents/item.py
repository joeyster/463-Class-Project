class Item():
    def __init__(self, item_id, packing_id, name, length, width):
        self.item_id = item_id  # 001
        self.packing_id = packing_id  # "A"
        self.name = name  # laptop
        self.length = length
        self.width = width
        self.area = length * width

    def __str__(self):
        return self.item_id

    def __repr__(self):
        return self.item_id
