#!/usr/bin/env python3
import sys


def average_score(scores: list[int]) -> int:
    return sum(scores)/len(scores)


def print_analytics(scores: list[int]) -> None:
    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {average_score(scores)}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


def main() -> None:
    print("=== Player Score Analytics ===")
    if len(sys.argv) == 1:
        print(
            "No Score provided. "
            f"Usage: python3 {sys.argv[0]} <score1> <score2> ...")
        return
    scores: list[int] = []
    for i in range(1, len(sys.argv)):
        try:
            scores.append(int(sys.argv[i]))
        except ValueError as e:
            print(f"Error: the score '{sys.argv[i]}' must be an integer. {e}")
    print_analytics(scores)


if __name__ == "__main__":
    main()
