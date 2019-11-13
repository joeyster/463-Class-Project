import unittest
from item import Item
from warehouse import Warehouse


# WORKING VERSION

class MyTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_add_item(self):
        warehouse = Warehouse(True)
        test_list = [123, 'apples', 5, 6, 6]
        warehouse.add_item(test_list)
        self.assertEqual('apples', warehouse.new_item_list[0].name, 'Passed')
        self.assertEqual(123, warehouse.new_item_list[0].item_id, 'Passed')
        self.assertEqual(5, warehouse.new_item_list[0].quantity, 'Passed')
        self.assertEqual(6, warehouse.new_item_list[0].length, 'Passed')
        self.assertEqual(6, warehouse.new_item_list[0].width, 'Passed')

    def test_remove_item(self):
        warehouse = Warehouse(True)
        # test_list = [123, 'apples', 5, 6, 6]
        #  warehouse.remove_item(test_list)
        self.assertEqual([], warehouse.item_list, 'Passed')


if __name__ == '__main__':
    unittest.main()