
from warehouse import Warehouse
from item import Item
import unittest 



class Test(unittest.TestCase):


    def test_add_item(self):
        warehouse = Warehouse()
        test_list = ['123', 'apples', 5, 6, 6]
        warehouse.add_item(test_list)
        self.assertEqual('apples', warehouse.new_item_list[0].name, "passed")
        print("passed")

        
if __name__ == '__main__':
    unittest.main()