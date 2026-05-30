#!/usr/bin/python3

import random

ACHIVEMENT_LIST = ['Crafting Genius', 'Strategist', 'World Savior',
                   'Speed Runner', 'Survivor', 'Master Explorer',
                   'Treasure Hunter', 'Unstoppable', 'First Steps',
                   'Collector Supreme', 'Untouchable', 'Sharp Mind',
                   'Boss Slayer']


def gen_player_achivements() -> set:
    num_to_pick = random.randint(5, 9)
    random_picks = random.sample(ACHIVEMENT_LIST, num_to_pick)
    return set(random_picks)


def main() -> None:
    print("=== Achievement Tracker System ===\n")

    alice = gen_player_achivements()
    bob = gen_player_achivements()
    charlie = gen_player_achivements()
    dylan = gen_player_achivements()

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}\n")

    all = alice.union(bob, charlie, dylan)
    print(f"All distinct achiements: {all}\n")

    print(f"Common achievements: {alice.intersection(bob, charlie, dylan)}\n")

    print(f"Only Alice has: {alice.difference(bob, charlie, dylan)}")
    print(f"Only Bob has: {bob.difference(alice, charlie, dylan)}")
    print(f"Only Charlie has: {charlie.difference(alice, bob, dylan)}")
    print(f"Only Dylan has: {dylan.difference(alice, bob, charlie)}\n")

    print(f"Alice is missing: {all.difference(alice)}")
    print(f"Bob is missing: {all.difference(bob)}")
    print(f"Charlie is missing: {all.difference(charlie)}")
    print(f"Dylan is missing: {all.difference(dylan)}")


if __name__ == "__main__":
    main()
