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
        test_list = [123, 'apples', 5, 6, 6]
        warehouse.add_item(test_list)
        warehouse.remove_item(test_list[0])
        self.assertEqual([], warehouse.item_list, 'Passed')

    def test_change_warehouse_size(self):
        warehouse = Warehouse(True)
        warehouse.change_warehouse_size(10, 5)
        self.assertEqual(10, warehouse.board_width, 'Passed')
        self.assertEqual(5, warehouse.board_height, 'Passed')

    def test_init_board(self):
        warehouse = Warehouse(True)
        warehouse.board_width = 10
        warehouse.board_height = 5
        warehouse.init_board()
        self.assertEqual(10, len(warehouse.new_board[0]), 'Passed')
        self.assertEqual(5, len(warehouse.new_board), 'Passed')

    def test_check_available_area(self):
        warehouse = Warehouse(True)
        test_list = [123, 'apples', 1, 6, 6]
        warehouse.add_item(test_list)
        test_list_2 = [456, 'oranges', 2, 2, 2]
        warehouse.add_item(test_list_2)
        test_true = warehouse.check_available_area(warehouse.new_item_list, 44)
        test_false = warehouse.check_available_area(warehouse.new_item_list, 10)
        self.assertEqual(True, test_true, 'Passed')
        self.assertEqual(False, test_false, 'Passed')

    def test_fill_board(self):
        warehouse = Warehouse(True)
        warehouse.board_width = 10
        warehouse.board_height = 10
        warehouse.init_board()
        test_item = [123, 'apples', 1, 6, 6]
        warehouse.add_item(test_item)
        warehouse.fill_board(0, warehouse.new_item_list[0], 1)
        self.assertEqual('1', warehouse.new_board[0][0], 'Passed')

    def test_packing(self):
        warehouse = Warehouse(True)
        warehouse.board_width = 10
        warehouse.board_height = 10
        warehouse.init_board()
        test_item = [123, 'apples', 1, 6, 6]
        warehouse.add_item(test_item)
        self.assertEqual(0, len(warehouse.complete_list), 'Passed')
        warehouse.packing(warehouse.new_item_list)
        self.assertEqual(1, len(warehouse.complete_list), 'Passed')


if __name__ == '__main__':
    unittest.main()
