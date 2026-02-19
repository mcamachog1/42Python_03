#!/usr/bin/env python3


def main() -> None:

    a: list[str] = [
        "first_kill",
        "level_10",
        "treasure_hunter",
        "speed_demon",
        "boss_slayer",
        "collector",
        "perfectionist"
        ]
    alice = {a[0], a[1], a[2], a[3]}
    bob = {a[0], a[1], a[4], a[5]}
    charlie = {a[1], a[2], a[4], a[3], a[6]}
    all = alice.union(bob, charlie)

    # Rare achievement
    rare_alice = alice.difference(bob.union(charlie))
    rare_bob = bob.difference(alice.union(charlie))
    rare_charlie = charlie.difference(bob.union(alice))
    rare = rare_alice.union(rare_bob, rare_charlie)

    print("=== Achievement Tracker System ===\n")
    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")
    print()
    print("=== Achievement Analytics ===")
    print(f"All unique achievements: {all}")
    print(f"Total unique achievements: {len(all)}")
    print()
    print(f"Common to all players: {alice.intersection(bob, charlie)}")
    print(f"Rare achievements (1 player): {rare}")
    print("")
    print(f"Alice vs Bob common: {alice.intersection(bob)}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")


if __name__ == "__main__":
    main()
