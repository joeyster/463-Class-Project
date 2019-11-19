import unittest
from item import Item
from warehouse import Warehouse
from visualize import VisualizeWarehouse


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

    def test_find_starting_index(self):
        visualize = VisualizeWarehouse(test_flag=True)
        test_board = [['0', '0', '1', '1', '0'],
                      ['0', '0', '1', '1', '0'],
                      ['0', '0', '1', '1', '0']]
        result = visualize.find_starting_index(test_board, 1)
        self.assertEqual((2, 0), result, 'Passed')

    def test_find_full_box_size(self):
        visualize = VisualizeWarehouse(test_flag=True)
        test_board = [['0', '0', '1', '1', '0'],
                      ['0', '0', '1', '1', '0'],
                      ['0', '0', '1', '1', '0']]
        result = visualize.find_full_box_size(test_board, 2, 0, 1)
        self.assertEqual((2, 3), result, 'Passed')

    def test_create_rect(self):
        warehouse = Warehouse(test_flag=True)
        visualize = VisualizeWarehouse(test_flag=True)
        visualize.screen_buffer = 10
        visualize.width_segment = 40
        visualize.height_segment = 40
        test_board = [['0', '0', '1', '1', '0'],
                      ['0', '0', '1', '1', '0'],
                      ['0', '0', '1', '1', '0']]
        test_item = [123, 'apples', 1, 6, 6]
        warehouse.add_item(test_item)
        result = visualize.create_item_rect(test_board, warehouse.new_item_list)
        self.assertEqual(1, len(visualize.rectangle_list), 'Passed')


if __name__ == '__main__':
    unittest.main()
