import pprint


def DisplayInventory(inventory):
    a = 0
    for i in inventory.keys():
        a = a + inventory[i]
    c = pprint.pformat(inventory)
    c = "Inventory:\n" + c + "\nTotal number of items:" + str(a)
    print(c)

def DisplayFcn():
    print("Goodbye world")

#spam = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
#DisplayInventory(spam)
