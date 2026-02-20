#!/usr/bin/env python3

import sys

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

    print("=== Current Inventory ===")
    total_qty = sum(inventory.values())
    
    if total_qty == 0:
        print("Inventory is empty.")
    else:
        order_list = order_dict(inventory)
        for name, qty in order_list:
            print(f"{name}: {qty} units ({qty/total_qty * 100:.1f}%)")


if __name__ == "__main__":
    main()