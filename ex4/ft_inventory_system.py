#!/usr/bin/python3

import sys


def parse_params() -> dict:
    inventory = {}
    for arg in sys.argv[1:]:
        if not ":" in arg or arg.count(":") != 1:
            print(f"Error - invalid parameter '{arg}'")
            continue

        item, quantity_str = arg.split(":")

        if item in inventory:
            print(f"Redundant item '{item}' - discarding")
            continue

        try:
            quantity = int(quantity_str)
            inventory[item] = quantity
        except ValueError:
            print (f"Quantity error for '{item}': "
                   f"invalid literal for int() with base 10: '{quantity_str}'")


    return inventory


def main () -> None:
    print("=== Inventory System Analysis ===")

    inventory = parse_params()
    print(f"Got inventory: {inventory})")
    print(f"Item list: {inventory.keys()}")

    for quantity in inventory.values():
        total_quantity += quantity
    print(f"Total quantity of the {len(inventory)} items: {total}")

    for item, quantity in inventory.items():
        percentage = (quantity / total_quantity) * 100
        print(f"Item {item} represents {round(percentage, 1)}%")


if __name__ == "__main__":
    main()
