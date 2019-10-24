import sys
from PyQt5.QtWidgets import QApplication
from visualize import VisualizeWarehouse
from main_window import MainWindow
from copy import deepcopy
from item import Item


class Warehouse:
    """Controls the warehouse interactions between front and back end."""
    def __init__(self):
        self.item_list = []
        self.complete_list = []
        self.board = []
        self.warehouse_vs = VisualizeWarehouse()
        self.warehouse_vs.create_screen()
        self.warehouse_surface = self.warehouse_vs.surface
        self.board_width = 0
        self.board_height = 0
        self.app = None
        self.window = None
        self.pygame_qt_switch = 1
        self.setup_ui()

    def setup_ui(self):
        """Sets up the UI using PyQt5."""
        self.app = QApplication(sys.argv)
        self.window = MainWindow(surface=self.warehouse_surface, controller=self)
        #self.window.resize(800, 575)
        self.window.setFixedSize(800, 575)
        self.window.show()
        sys.exit(self.app.exec_())

    def add_item(self, item_parts):
        item = Item(item_id=item_parts[0], name=item_parts[1], quantity=int(item_parts[2]), length=int(item_parts[3]), width=int(item_parts[4]))
        self.item_list.append(item)

    def remove_item(self):
        # Todo: Delete item from item list, repack?
        pass

    def locate_item(self, matching_id):
        # Todo: Get item number from UI then highlight that item in visualization section
        self.packing()
        self.warehouse_vs.form_display(board=self.board, item_list=self.item_list)
        surface = self.warehouse_vs.draw_display(matching_id)
        self.window.update_image(surface=surface)
        self.window.setFixedSize(800, 575 + self.pygame_qt_switch)
        self.pygame_qt_switch = self.pygame_qt_switch * -1

    def change_warehouse_size(self, width, height):
        self.board_width = width
        self.board_height = height
        self.init_board()
        self.packing()
        self.warehouse_vs.form_display(board=self.board, item_list=self.item_list)
        self.warehouse_vs.draw_display()

    def pack_warehouse(self):
        self.packing()
        #self.show_board()
        print("pack_warehouse's self.complete_list: ",self.complete_list)
        self.warehouse_vs.form_display(board=self.board, item_list=self.complete_list)
        surface = self.warehouse_vs.draw_display()
        self.window.update_image(surface=surface)
        #self.window.resize(800, 575 + self.pygame_qt_switch)
        self.window.setFixedSize(800, 575 + self.pygame_qt_switch)
        self.pygame_qt_switch = self.pygame_qt_switch * -1

    def init_board(self):
        """
        creates a 2D array representing warehouse
        """
        self.board = []
        for _ in range(self.board_height):
            row = []
            for _ in range(self.board_width):
                row.append("0")
            self.board.append(row)

    def check_available_area(self, item_list, available_area):
        """
        calculate area item_list will take up
        returns true if available space, false if not enough
        """
        total_item_area = 0
        for index in range(len(item_list)):
            total_item_area = total_item_area + item_list[index].area
        if total_item_area > available_area:
            return False
        else:
            return True

    def fill_board(self, row_index, item):
        """
        fills the item inside the board
        """
        for y in range(self.board[row_index].index("0"), self.board[row_index].index("0") + item.length):
            temp = row_index
            for _ in range(item.width):
                self.board[temp][y] = item.item_id
                temp = temp + 1

    # todo: may not need this, for testing
    def show_board(self):
        for row in self.board:
            print(row)

    def packing(self):
        self.init_board()
        item_list_copy = deepcopy(self.item_list)
        complete_list = []
        # retract quantities
        for item in item_list_copy:
            for amt in range(item.quantity):
                complete_list.append(item)
        print("complete_list: ", complete_list)
        complete_list_copy = deepcopy(complete_list)
        self.complete_list = complete_list

        while complete_list_copy:  # while item_list has something in it
            if self.check_available_area(complete_list_copy, (len(self.board) * len(self.board[0]))):  # has space overall
                for item in complete_list:
                    for row_index in range(len(self.board)):  # row by row
                        if item.length <= self.board[row_index].count("0"):  # if fits
                            self.fill_board(row_index, item)
                            complete_list_copy.pop(0)
                            break
            else:
                print("item list area does not fit in warehouse area")
                break
        print("complete_list: ", complete_list)
        print("complete_list_copy: ", complete_list_copy)
        self.show_board()



if __name__ == "__main__":
    warehouse = Warehouse()
