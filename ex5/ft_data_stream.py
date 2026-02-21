#!/usr/bin/env python3

from typing import Generator

class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.level = 0
        self.events = []
    
    def level_up(self, level_name: str) -> None:
        self.level += 1
        self.events.append(level_name)

    def __str__(self) -> str:
        if self.events:
            return f"Player {self.name} (level {self.level}) {self.events[-1]}"
        else:
            return f"Player {self.name} (level {self.level}) has not completed any events."


def stream_events(players: list[Player]) -> Generator[str, None, None]:
    for player in players:
        yield str(player)


def main() -> None:
    players = [Player("alice"), Player("bob"), Player("charlie")]
    players[0].level_up("killed monster")
    players[1].level_up("found treasure")
    players[2].level_up("leveled up")
    
    iterator = iter(stream_events(players))
    i = 0
    end_of_stream = "END_OF_STREAM"

    while True:
        event = next(iterator, end_of_stream)
        if event == end_of_stream:
            break
        print(f"Event {i}: {event}")
        i += 1

if __name__ == "__main__":
    main()
