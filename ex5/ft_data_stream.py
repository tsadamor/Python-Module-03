#!/usr/bin/python3

import random
from typing import Generator


def gen_event() -> Generator[tuple, None, None]:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = [
               "run", "eat", "sleep", "grab",
               "move", "climb", "swim", "release"
              ]

    while True:
        player = random.choice(players)
        action = random.choice(actions)

        yield (player, action)


def consume_event(event_list: list) -> Generator[tuple, None, None]:
    while event_list:
        random_index = random.randint(0, len(event_list) - 1)
        chosen_event = event_list.pop(random_index)

        yield chosen_event


def main() -> None:
    print("=== Game Data Stream Processor ===")

    event_stream = gen_event()

    for i in range(1000):
        event = next(event_stream)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")

    event_list = [next(event_stream) for _ in range(10)]
    print(f"Built list of 10 events: {event_list}")

    for event in consume_event(event_list):
        print(f"Got event from the list: {event}")
        print(f"Remains in the list: {event_list}")


if __name__ == "__main__":
    main()
