class Item():
    def __init__(self, item_id, length, width):
        self.item_id = item_id
        self.length = length
        self.width = width
        self.area = length * width

    def __str__(self):
        return self.item_id

    def __repr__(self):
        return self.item_id
