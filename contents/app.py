from item import Item
from visualize import VisualizeWarehouse
from event_handler import EventHandler
from copy import deepcopy

# print("Welcome to warehouse!")
# length, width = input("Enter length, width of warehouse: ").split()

# items_amt = input("How many items? ")

# itemArray = []
# for item in range(int(items_amt)):
#   print(f"item {item+1}")
#   length, width, height = input("Enter length, width: ").split()
#   itemArray.append(Item(item+1, length, width))

# print(itemArray[0])


def init_board(x_dim, y_dim):
    """
    creates a 2D array representing warehouse
    """
    board = []
    for _ in range(x_dim):
        row = []
        for _ in range(y_dim):
            row.append("0")
        board.append(row)
    return board


def show_board(board):
    for row in board:
        print(row)


def check_available_area(item_array):
    """
    calculate area item_array will take up
    returns true if available space, false if not enough
    """
    total_item_area = 0
    for index in range(len(item_array)):
        total_item_area = total_item_area + item_array[index].area
    if total_item_area > available_area:
        return False
    else:
        return True


def fill_board(board, row_index, item):
    """
    fills the item inside the board
    """
    for y in range(board[row_index].index("0"), board[row_index].index("0")+item.length):
        temp = row_index
        for _ in range(item.width):
            board[temp][y] = item.item_id
            temp = temp + 1

def packing(item_array, board):
    item_array_copy = deepcopy(item_array)
    while item_array_copy:  # while item_array has something in it
        if check_available_area(item_array_copy):  # has space overall
            for item in item_array:
                for row_index in range(len(board)):  # row by row
                    if item.length <= board[row_index].count("0"):  # if fits
                        fill_board(board, row_index, item)
                        item_array_copy.pop(0)
                        break
        else:
            print("item array area does not fit in warehouse area")
            break
    return board

if __name__ == "__main__":
    # board = 2D array
    warehouse_x = 10
    warehouse_y = 10
    board = init_board(warehouse_x, warehouse_y)
    available_area = warehouse_x * warehouse_y

    # bunch of test items
    item1 = Item("001", "laptop", 5, 2)
    item2 = Item("002", "laptop", 4, 2)
    item3 = Item("003", "laptop", 1, 1)
    item4 = Item("004", "laptop", 1, 2)
    item5 = Item("005", "laptop", 4, 4)

    # put items in the array
    item_array = [item1, item2, item3, item4, item5]

    board = packing(item_array, board)
    
    show_board(board)
    vis = VisualizeWarehouse()
    vis.create_screen()
    event_handler = EventHandler()
    vis.form_display(board=board, item_list=item_array)
    vis.draw_display()

    while True:
        event_handler.check_events()
