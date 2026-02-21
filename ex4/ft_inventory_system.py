#!/usr/bin/env python3

import sys

def restock(inventory:dict, min: int) -> list:
    needed: list = []
    for k, v in inventory.items():
        if v < min:
            needed.append(k)
    return needed

def make_nested(inventory: dict, n:int) -> dict:
    moderate: dict = {}
    scarce: dict = {}
    nested: dict = {}
    for key, value in inventory.items():
        if value < n:
            scarce[key] = value
        else:
            moderate[key] = value
    nested["Moderate"] = moderate
    nested["Scarce"] = scarce
    return nested

def get_max_value(inventory: dict) -> tuple:
    items: list = list(inventory.items())
    max: int = 0
    for t in items:
        if t[1] > max:
            max = t[1]
            key = t[0]        
    return (key, max)

def get_min_value(inventory: dict) -> tuple:
    min_item = min(inventory.items(), key=lambda item: item[1])
    return min_item

def order_dict(inventory: dict) -> list:
    items: list = []
    for key in inventory:
        item = [key, inventory[key]]
        items.append(item)
    end = len(items) - 1
    for i in range(len(items) - 1):
        for j in range(end):
            if end > 0:
                if items[j][1] < items[j + 1][1]:
                    temp = items[j + 1]
                    items[j + 1]= items[j]
                    items[j] = temp
        end -= 1
    return items

def main() -> None:
    print("=== Inventory System Analysis ===")
    if len(sys.argv) == 1:
        print(
            "No items provided. "
            f"Usage: python3 {sys.argv[0]} <item1:qty1> <item2:qty2> ...")
        return
    inventory: dict = {}
    for i in range(1, len(sys.argv)):
        try:
            pair = sys.argv[i].split(":")
            if len(pair) != 2 or not pair[0] or not pair[1]:
                print(
                    "Error in items provided. "
                    f"Usage: python3 {sys.argv[0]} <item1:qty1> <item2:qty2> ...")
                return
            inventory[pair[0]] = int(pair[1])
        except ValueError as e:
            print(f"{e}")

    print(f"Total items in inventory: {sum(inventory.values())}")
    print(f"Unique item types: {len(inventory.keys())}")

    print("\n=== Current Inventory ===")
    total_qty = sum(inventory.values())
    if total_qty == 0:
        print("Inventory is empty.")
    else:
        order_list = order_dict(inventory)
        for name, qty in order_list:
            print(f"{name}: {qty} units ({qty/total_qty * 100:.1f}%)")
    print("\n=== Inventory Statistics ===")
    max_name, max_qty = get_max_value(inventory)
    min_name, min_qty = get_min_value(inventory)
    max_unit = "units"
    min_unit = "units"
    if max_unit == 1:
        max_qty = "unit"
    if min_qty == 1:
        min_unit = "unit"
    print(f"Most abundant: {max_name} ({max_qty} {max_unit})")
    print(f"Least abundant: {min_name} ({min_qty} {min_unit})")    

    print("\n=== Item Categories ===")
    nested_dict: dict = make_nested(inventory, 5)
    for key, value in nested_dict.items():
        print(f"{key}: {value}")

    print("\n===  Management Suggestions ===")
    print(f"Restock needed: {restock(inventory, 2)}")

    print("\n=== Dictionary Properties Demo ===")
    keys = list(inventory.keys())
    values = list(inventory.values())
    str_values = []
    for n in values:
        str_values.append(str(n))
    print(f"Dictionary keys: {", ".join(keys)}")
    print(f"Dictionary values: {", ".join(str_values)}")
    item_to_find = 'sword'
    exists = item_to_find in inventory
    print(f"Sample lookup - '{item_to_find}' in inventory: {exists}")

    print("\n=== Dictionary Extra Demo ===")    
    result_ok = inventory.get(item_to_find, "Item not found")
    print(f"Sample lookup - '{item_to_find}' qty in inventory: {result_ok}")
    item_to_find = 'not_exists'
    exists = item_to_find in inventory
    print(f"Sample lookup - '{item_to_find}' in inventory: {exists}")


if __name__ == "__main__":
    main()