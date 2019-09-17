from item import Item

print("Welcome to warehouse!")
length, width, height = input("Enter length, width, and height of warehouse: ").split()

itemsAmt = input("How many items? ")

itemArray = []
for item in range(int(itemsAmt)):
  print(f"item {item+1}")
  length, width, height = input("Enter length, width, and height: ").split()
  itemArray.append(Item(item+1, length, width, height))

print(itemArray[0])