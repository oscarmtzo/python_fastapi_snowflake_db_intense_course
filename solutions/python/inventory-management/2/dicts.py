"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.
    
    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    tracker = {}
     #with for in loop leveraging .get() and access to simple keys
    for item in items:
        if tracker.get(item, "not found") == "not found":
            tracker[item] = 1
        else:
            tracker[item] = tracker[item] + 1
    return tracker
    #pass


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    def create_dicts(some_dict:dict, inventory_list:list):
        for item in inventory_list:
            if some_dict.get(item, "not found") == "not found":
                some_dict[item] = 1
            else:
                some_dict[item] = some_dict[item] + 1
        return some_dict

    if len(inventory.items()) == 0:
        aux_dict = {}
        create_dicts(aux_dict, items)
        return aux_dict
    else:
        return create_dicts(inventory, items)
    pass


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """
    def manage_dict_decrement(some_dict:dict,inventory_list :list):
        for item in inventory_list:
            #if some_dict.get(item, "not found"):
            #    pass
            if some_dict.get(item, 0) > 0:
                #print(some_dict[item])
                some_dict[item] = some_dict[item] - 1 #decrement 1 item count of the list

            #else:
            #    some_dict[item] = 0 #manage when item is not within the dict, add it to the list but with 0 amount of items to it 
                
        return some_dict
    if len(inventory) == 0:
        aux_dict = {}
        return manage_dict_decrement(aux_dict, items)
    else:
        return manage_dict_decrement(inventory, items)
    pass


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """
    if inventory.get(item, "not found") == "not found":
        return inventory
    else:
        inventory.pop(item)
        return inventory
    pass


def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    new_list = list()
    for key_name, item_value in inventory.items():
        if item_value > 0:
            new_list.append((key_name, item_value))
    return new_list
    pass

if __name__ == "__main__":
    print(
        f"testing create_invetory output: \n\t{
            create_inventory(
                ["coal", "wood", "wood", "diamond", "diamond", "diamond"]
            )
        }"
    )
    print(
        f"testing empty dict() – add_items output: \n\t{
            add_items(
                {},
                ["coal", "wood", "wood", "diamond", "diamond", "diamond"]
            )
        }"
    )
    print(
        f"testing dict() with key-value pairs – add_items output: \n\t{
            add_items(
                {"coal":1}, ["wood", "iron", "coal", "wood"]
            )
        }"
    )
    print(
        f"testing empty dict() – decrement_items output: \n\t{
            decrement_items(
                {},
                ["coal", "coal", "wood", "wood", "diamond"]
            )
        }"
    )
    print(
        f"testing dict() with key-value pairs – decrement_items output: \n\t{
            decrement_items(
                {"coal":2, "wood":1, "diamond":2}, ["coal", "coal", "wood", "wood", "diamond"]
            )
        }"
    )
    print(
        f"testing empty dict() – remove_item output: \n\t{
            remove_item(
                {},
                "gold"
            )
        }"
    )
    print(
        f"testing dict() with key-value pairs – remove_item output: \n\t{
            remove_item(
                {"coal":2, "wood":1, "diamond":2}, "gold"
            )
        }"
    )
    print(
        f"testing empty dict() – list_inventory output: \n\t{
            list_inventory(
                {"coal":0, "wood":0, "diamond":0, "iron":0, "silver":0}
            )
        }"
    )
    print(
        f"testing dict() with key-value pairs – list_inventory output: \n\t{
            list_inventory(
                {"coal":7, "wood":11, "diamond":2, "iron":7, "silver":0}
            )
        }"
    )
    