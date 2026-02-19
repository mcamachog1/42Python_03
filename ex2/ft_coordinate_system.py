#!/usr/bin/env python3

import sys
import math


def create_coordinate(coords_str: str) -> tuple:
    coords: list = coords_str.split(",")
    if (len(coords) != 3):
        raise ValueError("Coordinate string "
                         "does not have 3 values as expected")
    try:
        x: int = int(coords[0])
        y: int = int(coords[1])
        z: int = int(coords[2])
    except ValueError as e:
        raise ValueError(f"{e}")
    coordinate_3D: tuple = (x, y, z)
    return coordinate_3D


def distance(p1: tuple, p2: tuple) -> float:
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    try:
        d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
    except TypeError as e:
        err_type = e.__class__.__name__
        err_args = e.args
        raise TypeError(f"Type Error: {err_type}, Args: {err_args}")
    return d


def test_1(c_str: str) -> None:
    try:
        point_1: tuple = create_coordinate(c_str)
        print(f"Position created: {point_1}")
        point_2: tuple = (0, 0, 0)
        print(f"Distance between {point_2} and {point_1}: "
              f"{distance(point_1, point_2):.2f}")
    except ValueError as e:
        print(f"{e}")


def test_2(c_str: str) -> None:
    try:
        print(f'Parsing coordinates: "{c_str}"')
        point_1: tuple = create_coordinate(c_str)
        print(f"Parsed position: {point_1}")
        point_2: tuple = (0, 0, 0)
        print(f"Distance between {point_2} and {point_1}: "
              f"{distance(point_1, point_2):.1f}")
    except ValueError as e:
        print(f"{e}")


def test_3(c_str: str) -> None:
    try:
        print(f'Parsing invalid coordinates: "{c_str}"')
        point_1: tuple = create_coordinate(c_str)
        print(f"Parsed position: {point_1}")
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        err_type = e.__class__.__name__
        err_args = e.args
        print(f"Error details - Type: {err_type}, Args: {err_args}")


def test_4(coords: str) -> None:
    print("Unpacking demonstration:")
    try:
        coord: tuple = create_coordinate(coords)
        x, y, z = coord
        X, Y, Z = coord
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates X={X}, Y={Y}, Z={Z}")
    except ValueError as e:
        print(f"{e}")


def test_5() -> None:
    if len(sys.argv) == 1:
        return
    try:
        coords: str = ",".join(sys.argv[1:])
        coord_3D = create_coordinate(coords)
        print(f"{coord_3D}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    print("=== Game Coordinate System  ===\n")
    if len(sys.argv) == 1:
        test_1("10,20,5")
        print()
        test_2("3,4,0")
        print()
        test_3("abc,def,ghi")
        print()
        test_4("3,4,0")
    else:
        test_5()
