
from warehouse import Warehouse
from item import Item
import unittest 

warehouse = Warehouse()

class TestStringMethods(unittest.TestCase):


    def add_item_test(self):
        test_list = ['123', 'apples', 5, 6, 6]
        warehouse.add_item(test_list)
        self.assertEqual('apples', warehouse.new_item_list[0].name)

        
if __name__ == '__main__':
    unittest.main()