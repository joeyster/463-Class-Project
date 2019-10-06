from item import Item

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
            row.append(0)
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
    for y in range(board[row_index].index(0), board[row_index].index(0)+item.length):
        temp = row_index
        for _ in range(item.width):
            board[temp][y] = 1
            temp = temp + 1


# board = 2D array
warehouse_x = 10
warehouse_y = 10
board = init_board(warehouse_x, warehouse_y)
available_area = warehouse_x * warehouse_y

# bunch of test items
item1 = Item("001", 5, 5)
item2 = Item("002", 5, 3)
item3 = Item("003", 5, 2)
item4 = Item("004", 4, 2)

# put items in the array
item_array = [item1, item2, item3, item4]

while item_array:
    if check_available_area(item_array):
        for row_index in range(len(board)):  # row by row
            if board[row_index].count(0) == 0:
                continue
            for item in item_array:
                if item.length <= board[row_index].count(0):  # if fits
                    fill_board(board, row_index, item)
                    item_array.pop(0)
                    break
            break

show_board(board)
