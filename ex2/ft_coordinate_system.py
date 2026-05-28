#!/usr/bin/python3

import math

def get_player_pos() -> None:
    while True:
        try:
            tmp_list = input("Enter new coordinates as floats in format 'x,y,z': ").split(",")
            
            if len(tmp_list) != 3:
                print("Invalid syntax")
                continue
            
            x = float(tmp_list[0])
            y = float(tmp_list[1])
            z = float(tmp_list[2])
            return (x, y, z)
        
        except ValueError:
            print("Invalid syntax")


def calculate_distance(pos_1: tuple[float, float, float], pos_2: tuple[float, float, float]) -> float:
    x1, y1, z1 = pos_1
    x2, y2, z2 = pos_2
    return round(math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2), 4)


def main() -> None:
    print("=== Game Coordinate System ===\n")

    print("Get a first set of coordinates")
    pos_1 = get_player_pos()
    print(f"Got a first tuple: {pos_1}")
    print(f"It includes: X={pos_1[0]}, Y={pos_1[1]}, Z={pos_1[2]}")
    print(f"Distance to center: {calculate_distance(pos_1, (0.0, 0.0, 0.0))}\n")

    print("Get a second set of coordiantes")
    pos_2 = get_player_pos()
    print(f"Distance between the 2 sets of coordinates: {calculate_distance(pos_1, pos_2)}")

if __name__ == "__main__":
    main()
