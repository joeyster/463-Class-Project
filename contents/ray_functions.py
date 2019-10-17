def search():
    # O(n) but can be O(1) if we have a dictionary
    input_name = print("Which item would you like find? ")
    for item in item_array:
        if item == input_name:
            print("found")
            #highlights item in warehouse diagram
            break
    print("item not found")  # or return False

#maybe we don't need this function?
def show_quantity(number):
    print("Displaying quantity of each item: ")
    for item in item_array:
        print(f'{item.name}: {item.quantity}')

def edit_quantity(number):
    item_quant= print("New quantity ")
    self.item_quant = number  # assuming this is in Item class