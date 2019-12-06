import sys
from PyQt5.QtWidgets import QApplication
from visualize import VisualizeWarehouse
from main_window import MainWindow
from copy import deepcopy
from item import Item

class Warehouse:
    """Controls the warehouse interactions between front and back end."""
    def __init__(self, test_flag=False):
        self.test_flag = test_flag
        self.item_list = []
        self.complete_list = []
        self.new_item_list = []
        self.board = []
        self.new_board = []
        self.warehouse_vs = VisualizeWarehouse()
        self.warehouse_vs.create_screen()
        self.warehouse_surface = self.warehouse_vs.surface
        self.window_size_width = 800
        self.window_size_height = 543
        self.board_width = 0
        self.board_height = 0
        self.filled_area = 0
        self.app = None
        self.window = None
        self.pygame_qt_switch = 1
        if not self.test_flag:
            self.setup_ui()

    def setup_ui(self):
        """Sets up the UI using PyQt5."""
        self.app = QApplication(sys.argv)
        self.window = MainWindow(surface=self.warehouse_surface, controller=self)
        self.window.setFixedSize(self.window_size_width, self.window_size_height)
        self.window.show()
        self.window.ui_widget.startWindow.show()
        sys.exit(self.app.exec_())

    def add_item(self, item_parts):
        """Add an item to the warehouse list."""
        item = Item(item_id=item_parts[0], name=item_parts[1], quantity=int(item_parts[2]), length=int(item_parts[3]), width=int(item_parts[4]))
        self.new_item_list = deepcopy(self.item_list)
        self.new_item_list.append(item)
        if not self.test_flag:
            self.packing(self.new_item_list)
        else:
            self.item_list = deepcopy(self.new_item_list)

    def remove_item(self, item_id):
        """Remove an item from the warehouse list."""
        for i in list(self.item_list):
            if item_id == i.item_id:
                self.item_list.remove(i)

    def locate_item(self, matching_id):
        """Highlight an item in the warehouse view that matches the passed in ID."""
        self.packing(self.item_list)
        self.warehouse_vs.form_display(board=self.board, item_list=self.complete_list)
        surface = self.warehouse_vs.draw_display(matching_id)
        self.window.update_image(surface=surface)
        self.window.setFixedSize(self.window_size_width, self.window_size_height + self.pygame_qt_switch)
        self.pygame_qt_switch = self.pygame_qt_switch * -1

    def change_warehouse_size(self, width, height):
        """Update the warehouse dimensions."""
        self.board_width = width
        self.board_height = height
        self.init_board()
        self.packing(self.item_list)
        self.warehouse_vs.form_display(board=self.board, item_list=self.complete_list)
        self.warehouse_vs.draw_display()

    def pack_warehouse(self):
        """Pack the warehouse pygame view with the list of items."""
        self.warehouse_vs.form_display(board=self.board, item_list=self.complete_list)
        surface = self.warehouse_vs.draw_display()
        self.window.update_image(surface=surface)
        self.window.setFixedSize(self.window_size_width, self.window_size_height + self.pygame_qt_switch)
        self.pygame_qt_switch = self.pygame_qt_switch * -1

    def init_board(self):
        """Create a 2D array representing warehouse."""
        self.new_board = []
        for _ in range(self.board_height):
            row = []
            for _ in range(self.board_width):
                row.append("0")
            self.new_board.append(row)

    def check_available_area(self, item_list, available_area):
        """Calculate the area that item_list will take up; returns true if available space, false if not enough."""
        total_item_area = 0
        for index in range(len(item_list)):
            total_item_area = total_item_area + item_list[index].area
        if total_item_area > available_area:
            return False
        else:
            return True

    def fill_board(self, row_index, item, count):
        """Fill the items inside the board."""
        for y in range(self.new_board[row_index].index("0"), self.new_board[row_index].index("0") + item.length):
            temp = row_index
            for _ in range(item.width):
                self.new_board[temp][y] = str(count)
                temp = temp + 1

    def show_board(self):
        """Display the board to the console for testing."""
        for row in self.board:
            print(row)

    def packing(self, new_item_list):
        """Iterate through the board to attempt to pack the items into the warehouse, check for failures."""
        self.init_board()
        item_list_copy = deepcopy(new_item_list)
        complete_list = []
        # retract quantities
        for item in item_list_copy:
            for amt in range(item.quantity):
                complete_list.append(item)
        complete_list_copy = deepcopy(complete_list)
        count = 1
        items_fit = True
        while complete_list_copy:  # while item_list has something in it
            if self.check_available_area(complete_list_copy, (len(self.new_board) * len(self.new_board[0]))):  # has space overall
                for item in complete_list:
                    for row_index in range(len(self.new_board)):  # row by row
                        if item.length <= self.new_board[row_index].count("0"):  # if fits
                            item.packing_id = count
                            self.fill_board(row_index, item, count)
                            complete_list_copy.pop(0)
                            count = count + 1
                            self.filled_area += item.area
                            if not self.test_flag:
                                self.window.ui_widget.available_space.setText('Space Remaining - {}'.format(str(self.board_height*self.board_width - self.filled_area)))
                            break
            else:
                self.window.display_error("The item list does not fit in warehouse area.")
                items_fit = False
                break
        if items_fit:
            self.board = self.new_board
            self.item_list = deepcopy(new_item_list)
            self.complete_list = deepcopy(complete_list)


if __name__ == "__main__":
    warehouse = Warehouse()
