#!/usr/bin/python3

import random


def main() -> None:
    print("=== Game Data Alchemist ===\n")

    players = [
               "Alice", "bob", "Charlie", "dylan", "Emma",
               "Gregory", "john", "kevin", "Liam"
              ]
    all_capitalized = [name.capitalize() for name in players]
    only_capitalized = [name for name in players if name == name.capitalize]

    print(f"Initial list of players: {players}")
    print(f"New list with all names capitalized: {all_capitalized}")
    print(f"New list of capitalized names only: {only_capitalized}\n")

    score_dict = {name: random.randint(1, 1000) for name in all_capitalized}
    score_average = sum(score_dict.values()) / len(score_dict)
    high_scores = {
                   name: score for name, score in score_dict.items()
                   if score > score_average
                  }

    print(f"Score dict: {score_dict}")
    print(f"Score average is {round((score_average), 2)}")
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
