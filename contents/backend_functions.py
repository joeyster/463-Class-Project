from item import Item
def create_warehouse(length, width):

    # todo: get user warehouse size in form from button?

    # todo: get return types needed
    return length * width


def edit_warehouse_size(length, width):
    new_length = length
    new_width = width


    return new_length * new_width

def addItem(item): # accepts item objects and appends to the list
    item_array=[]
    item_array.append(item)
    return item_array

def removeItem(item_id, item_array): # takes item's id and current list of item.

    for i in item_array:
        if item.item_id == item_id:
            del item_array[i]










# itemNameList = []
# itemIdList = []
# itemQuantityList = []
#
# # todo: need to refactor using joeys item class
# def add_item():
#     num_of_item = input ("Enter the number of items that you want to add: ")
#     x = int(num_of_item)
#
#     for i in range(x):
#         item_name = input("Enter the name: ")
#         str(item_name)
#         itemNameList.append(item_name)
#
#         item_id = input("Enter the item's id: ")
#         int(item_id)
#         itemIdList.append(item_id)
#
#         item_quantity = input("Enter the quantity: ")
#         int(item_quantity)
#         itemQuantityList.append(item_quantity)
#     for j in zip(itemNameList, itemIdList, itemQuantityList):
#         print(j)
#     # need to include the size. Ask for help
#
#
# add_item()
#
#
# def remove_item():
#     c = input('Enter X to exit or R to remove an item: ')
#     if c == 'r' or c == 'R':
#         search_item = input("Enter the item's name:")
#         str(search_item)
#         itemNameList.remove(search_item)
#         print(itemNameList)
#     else:
#         exit(0)
# # also need to remove id and quantity
#
#
# remove_item()












