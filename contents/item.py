class Item():
  def __init__(self, item_id, length, width, height):
    self.item_id = item_id
    self.length = length
    self.width = width
    self.height = height
    self.area = length * width * height

  def __str__(self):
    return self.item_id