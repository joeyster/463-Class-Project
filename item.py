class Item:
    """Holds the attributes of an item to store in the warehouse."""
    def __init__(self, item_id, name, quantity, length, width):
        self.item_id = item_id  # 001
        self.name = name  # laptop
        self.quantity = quantity
        self.length = length
        self.width = width
        self.area = length * width

    def __str__(self):
        """Magic method for printing an item."""
        return self.item_id

    def __repr__(self):
        """Magic method for printing an item."""
        return self.item_id
