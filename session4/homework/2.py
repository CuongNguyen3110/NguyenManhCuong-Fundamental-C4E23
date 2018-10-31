inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

inventory["pocket"] = ["seashell", "strangeberry", "lint"]
print(inventory)
inventory["backpack"].pop(1)
print(inventory)
inventory["gold"] = 50
print(inventory)