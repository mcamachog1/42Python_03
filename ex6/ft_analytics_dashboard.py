#!/usr/bin/env python3


def load_game_data() -> list[dict]:
    players = [
        {
            'id': 1,
            'player': 'frank',
            'event_type': 'login',
            'timestamp': '2024-01-01T23:17',
            'data': {'level': 16, 'score_delta': 128, 'zone': 'pixel_zone_2'}
        },
        {
            'id': 2,
            'player': 'frank',
            'event_type': 'login',
            'timestamp': '2024-01-22T23:57',
            'data': {'level': 35, 'score_delta': -11, 'zone': 'pixel_zone_5'}
        },
        {
            'id': 3,
            'player': 'diana',
            'event_type': 'login',
            'timestamp': '2024-01-01T02:13',
            'data': {'level': 15, 'score_delta': 417, 'zone': 'pixel_zone_5'}
        },
        {
            'id': 4,
            'player': 'alice',
            'event_type': 'level_up',
            'timestamp': '2024-01-07T22:41',
            'data': {'level': 45, 'score_delta': 458, 'zone': 'pixel_zone_4'}
        },
        {
            'id': 5,
            'player': 'bob',
            'event_type': 'death',
            'timestamp': '2024-01-19T08:51',
            'data': {'level': 1, 'score_delta': 63, 'zone': 'pixel_zone_4'}
        },
        {
            'id': 6,
            'player': 'charlie',
            'event_type': 'kill',
            'timestamp': '2024-01-05T06:48',
            'data': {'level': 22, 'score_delta': 4, 'zone': 'pixel_zone_1'}
        },
        {
            'id': 7,
            'player': 'diana',
            'event_type': 'login',
            'timestamp': '2024-01-12T11:38',
            'data': {'level': 17, 'score_delta': -56, 'zone': 'pixel_zone_4'}
        },
        {
            'id': 8,
            'player': 'eve',
            'event_type': 'login',
            'timestamp': '2024-01-30T12:05',
            'data': {'level': 36, 'score_delta': 200, 'zone': 'pixel_zone_5'}
        },
        {
            'id': 9,
            'player': 'charlie',
            'event_type': 'level_up',
            'timestamp': '2024-01-07T22:04',
            'data': {'level': 3, 'score_delta': 133, 'zone': 'pixel_zone_3'}
        },
        {
            'id': 10,
            'player': 'alice',
            'event_type': 'logout',
            'timestamp': '2024-01-28T03:24',
            'data': {'level': 18, 'score_delta': 364, 'zone': 'pixel_zone_3'}
        },
        {
            'id': 11,
            'player': 'bob',
            'event_type': 'kill',
            'timestamp': '2024-01-12T06:42',
            'data': {'level': 18, 'score_delta': -27, 'zone': 'pixel_zone_5'}
        },
        {
            'id': 12,
            'player': 'frank',
            'event_type': 'logout',
            'timestamp': '2024-01-18T23:15',
            'data': {'level': 11, 'score_delta': 373, 'zone': 'pixel_zone_4'}
        },
        {
            'id': 13,
            'player': 'charlie',
            'event_type': 'item_found',
            'timestamp': '2024-01-23T17:14',
            'data': {'level': 44, 'score_delta': 232, 'zone': 'pixel_zone_1'}
        },
        {
            'id': 14,
            'player': 'bob',
            'event_type': 'login',
            'timestamp': '2024-01-26T10:25',
            'data': {'level': 18, 'score_delta': -33, 'zone': 'pixel_zone_2'}
        },
        {
            'id': 15,
            'player': 'eve',
            'event_type': 'item_found',
            'timestamp': '2024-01-11T06:41',
            'data': {'level': 32, 'score_delta': 305, 'zone': 'pixel_zone_4'}
        },
        {
            'id': 16,
            'player': 'bob',
            'event_type': 'kill',
            'timestamp': '2024-01-05T07:47',
            'data': {'level': 36, 'score_delta': 451, 'zone': 'pixel_zone_3'}
        },
        {
            'id': 17,
            'player': 'frank',
            'event_type': 'level_up',
            'timestamp': '2024-01-14T18:25',
            'data': {'level': 24, 'score_delta': 124, 'zone': 'pixel_zone_2'}
        },
        {
            'id': 18,
            'player': 'eve',
            'event_type': 'death',
            'timestamp': '2024-01-03T01:55',
            'data': {'level': 8, 'score_delta': 56, 'zone': 'pixel_zone_2'}
        },
        {
            'id': 19,
            'player': 'frank',
            'event_type': 'death',
            'timestamp': '2024-01-20T02:24',
            'data': {'level': 25, 'score_delta': 379, 'zone': 'pixel_zone_5'}
        },
        {
            'id': 20,
            'player': 'charlie',
            'event_type': 'level_up',
            'timestamp': '2024-01-28T00:43',
            'data': {'level': 47, 'score_delta': 17, 'zone': 'pixel_zone_5'}
        },
        {
            'id': 21,
            'player': 'charlie',
            'event_type': 'item_found',
            'timestamp': '2024-01-11T03:18',
            'data': {'level': 28, 'score_delta': 61, 'zone': 'pixel_zone_4'}
        },
        {
            'id': 22,
            'player': 'alice',
            'event_type': 'item_found',
            'timestamp': '2024-01-29T23:16',
            'data': {'level': 33, 'score_delta': 82, 'zone': 'pixel_zone_5'}
        },
        {
            'id': 23,
            'player': 'alice',
            'event_type': 'item_found',
            'timestamp': '2024-01-10T20:32',
            'data': {'level': 39, 'score_delta': 103, 'zone': 'pixel_zone_2'}
        },
        {
            'id': 24,
            'player': 'charlie',
            'event_type': 'logout',
            'timestamp': '2024-01-18T16:58',
            'data': {'level': 1, 'score_delta': 231, 'zone': 'pixel_zone_4'}
        },
        {
            'id': 25,
            'player': 'alice',
            'event_type': 'login',
            'timestamp': '2024-01-30T11:56',
            'data': {'level': 20, 'score_delta': 145, 'zone': 'pixel_zone_1'}
        },
        {
            'id': 26,
            'player': 'bob',
            'event_type': 'level_up',
            'timestamp': '2024-01-03T02:46',
            'data': {'level': 32, 'score_delta': -30, 'zone': 'pixel_zone_5'}
        },
        {
            'id': 27,
            'player': 'bob',
            'event_type': 'logout',
            'timestamp': '2024-01-22T15:35',
            'data': {'level': 11, 'score_delta': 171, 'zone': 'pixel_zone_5'}
        },
        {
            'id': 28,
            'player': 'eve',
            'event_type': 'death',
            'timestamp': '2024-01-07T17:48',
            'data': {'level': 47, 'score_delta': 105, 'zone': 'pixel_zone_3'}
        },
        {
            'id': 29,
            'player': 'diana',
            'event_type': 'item_found',
            'timestamp': '2024-01-21T11:28',
            'data': {'level': 34, 'score_delta': 362, 'zone': 'pixel_zone_1'}
        },
        {
            'id': 30,
            'player': 'bob',
            'event_type': 'logout',
            'timestamp': '2024-01-03T10:01',
            'data': {'level': 38, 'score_delta': 467, 'zone': 'pixel_zone_2'}
        },
        {
            'id': 31,
            'player': 'eve',
            'event_type': 'logout',
            'timestamp': '2024-01-01T02:45',
            'data': {'level': 41, 'score_delta': -40, 'zone': 'pixel_zone_2'}
        },
        {
            'id': 32,
            'player': 'alice',
            'event_type': 'login',
            'timestamp': '2024-01-28T10:04',
            'data': {'level': 33, 'score_delta': 143, 'zone': 'pixel_zone_3'}
        },
        {
            'id': 33,
            'player': 'frank',
            'event_type': 'death',
            'timestamp': '2024-01-07T17:08',
            'data': {'level': 47, 'score_delta': 484, 'zone': 'pixel_zone_5'}
        },
        {
            'id': 34,
            'player': 'diana',
            'event_type': 'logout',
            'timestamp': '2024-01-26T15:51',
            'data': {'level': 27, 'score_delta': 94, 'zone': 'pixel_zone_1'}
        },
        {
            'id': 35,
            'player': 'alice',
            'event_type': 'item_found',
            'timestamp': '2024-01-14T11:27',
            'data': {'level': 27, 'score_delta': 378, 'zone': 'pixel_zone_1'}
        },
        {
            'id': 36,
            'player': 'frank',
            'event_type': 'item_found',
            'timestamp': '2024-01-21T03:03',
            'data': {'level': 26, 'score_delta': 247, 'zone': 'pixel_zone_1'}
        },
        {
            'id': 37,
            'player': 'bob',
            'event_type': 'logout',
            'timestamp': '2024-01-07T17:28',
            'data': {'level': 9, 'score_delta': 332, 'zone': 'pixel_zone_2'}
        },
        {
            'id': 38,
            'player': 'charlie',
            'event_type': 'death',
            'timestamp': '2024-01-08T02:28',
            'data': {'level': 36, 'score_delta': 0, 'zone': 'pixel_zone_1'}
        },
        {
            'id': 39,
            'player': 'frank',
            'event_type': 'level_up',
            'timestamp': '2024-01-27T00:05',
            'data': {'level': 49, 'score_delta': 142, 'zone': 'pixel_zone_2'}
        },
        {
            'id': 40,
            'player': 'diana',
            'event_type': 'death',
            'timestamp': '2024-01-16T06:55',
            'data': {'level': 26, 'score_delta': -40, 'zone': 'pixel_zone_2'}
        },
        {
            'id': 41,
            'player': 'diana',
            'event_type': 'login',
            'timestamp': '2024-01-13T08:59',
            'data': {'level': 30, 'score_delta': 192, 'zone': 'pixel_zone_4'}
        },
        {
            'id': 42,
            'player': 'frank',
            'event_type': 'item_found',
            'timestamp': '2024-01-26T17:42',
            'data': {'level': 46, 'score_delta': 398, 'zone': 'pixel_zone_2'}
        },
        {
            'id': 43,
            'player': 'bob',
            'event_type': 'kill',
            'timestamp': '2024-01-07T01:37',
            'data': {'level': 48, 'score_delta': 455, 'zone': 'pixel_zone_1'}
        },
        {
            'id': 44,
            'player': 'frank',
            'event_type': 'kill',
            'timestamp': '2024-01-02T01:37',
            'data': {'level': 31, 'score_delta': 414, 'zone': 'pixel_zone_5'}
        },
        {
            'id': 45,
            'player': 'bob',
            'event_type': 'login',
            'timestamp': '2024-01-17T02:54',
            'data': {'level': 12, 'score_delta': -30, 'zone': 'pixel_zone_5'}
        },
        {
            'id': 46,
            'player': 'alice',
            'event_type': 'item_found',
            'timestamp': '2024-01-28T07:25',
            'data': {'level': 8, 'score_delta': 483, 'zone': 'pixel_zone_2'}
        },
        {
            'id': 47,
            'player': 'eve',
            'event_type': 'level_up',
            'timestamp': '2024-01-02T19:05',
            'data': {'level': 27, 'score_delta': 497, 'zone': 'pixel_zone_5'}
        },
        {
            'id': 48,
            'player': 'eve',
            'event_type': 'kill',
            'timestamp': '2024-01-30T08:13',
            'data': {'level': 43, 'score_delta': 221, 'zone': 'pixel_zone_2'}
        },
        {
            'id': 49,
            'player': 'charlie',
            'event_type': 'death',
            'timestamp': '2024-01-05T21:41',
            'data': {'level': 20, 'score_delta': 368, 'zone': 'pixel_zone_3'}
        },
        {
            'id': 50,
            'player': 'alice',
            'event_type': 'login',
            'timestamp': '2024-01-15T19:36',
            'data': {'level': 7, 'score_delta': -25, 'zone': 'pixel_zone_5'}
        }
    ]
    return players


def list_comprehension() -> None:
    print("\n=== List Comprehension Examples ===")
    # Load example data
    events: list = load_game_data()

    # === PLAYERS IN TWO LAST LEVELS ===
    # List with a condition
    high_levels = [e['player'] for e in events if e['data']['level'] > 47]
    print(f"High level players (level > 47): {high_levels}")

    # === COUNT PLAYERS IN LEVEL 1 ===
    # List with a condition
    players_in_level = [e['player'] for e in events if e['data']['level'] == 1]
    print(f"Players in level (1): {players_in_level}")

    # === TOP 5 SCORES ===
    # List just with the scores
    all_scores = [e['data']['score_delta'] for e in events]
    # Get the first 5 elements from an ordered list (from greatest to least)
    top_5_scores = sorted(all_scores, reverse=True)[:5]
    print(f"Top 5 scores: {top_5_scores}")

    # === SCORES OF A PLAYER SORTED ===
    # Sort list comprehension with a condition
    scores = sorted(
        [e['data']['score_delta']
            for e in events if e['player'] == "alice"],
        reverse=True
        )
    print(f"alice's scores: {scores}")


def dict_comprehension() -> None:
    print("\n=== Dict Comprehension Examples ===")
    # Load example data
    events: list = load_game_data()

    # ==== TOP 5 SCORE WITH PLAYERS ===

    # === EACH PLAYER MAX SCORE
    # 1.- lista (set) unica de jugadores
    unique_players = {e['player'] for e in events}
    # 2.- Dictionary player:max_score
    max_score_by_player = {
        player: max(e['data']['score_delta']
                    for e in events if e['player'] == player)
        for player in unique_players
        }
    # 3.- Sort greatest to least and get first 5
    top_5 = sorted(
        max_score_by_player.items(),
        key=lambda item: item[1],
        reverse=True
        )[:5]
    print(f"Top 5 players: {top_5}")

    # === NUMBERS OF PLAYER BY LEVEL ===
    # Make a list with each ocurrence of level
    all_levels = [e['data']['level'] for e in events]
    # Make a dictionary key=level_name and value=count_levels
    level_counts = {lvl: all_levels.count(lvl) for lvl in set(all_levels)}
    print(f"Players by level: {level_counts}")

    # === MAKE CATEGORIES AND COUNT PLAYERS IN EACH CATEGORY ===
    # 1. Define categories: Beginners, Intermediate, Pro
    def get_range(level) -> str:
        if level <= 10:
            return "Beginner"
        if level <= 20:
            return "Intermediate"
        return "Pro"
    # 2. Extract all levels
    all_levels = [e['data']['level'] for e in events]
    # 3. Create the distribution dictionary (Dict Comprehension)
    # For each category count all level ocurrences
    # if it belongs to the category
    ranges = ["Beginner", "Intermediate", "Pro"]
    level_distribution = {
        r: sum(1 for lvl in all_levels if get_range(lvl) == r)
        for r in ranges
    }
    print(f"Level categories: {level_distribution}")


def set_comprehension() -> None:
    print("\n=== Set Comprehension Examples ===")
    # Load example data
    events: list = load_game_data()

    # === UNIQUE PLAYERS ===
    # Like a list but without duplicate elements (SET)
    unique_players = {e['player'] for e in events}

    # === UNIQUE EVENTS ===
    # Like a list but without duplicate elements (SET)
    unique_events = {e['event_type'] for e in events}

    # === UNIQUE ZONES ===
    # Like a list but without duplicate elements (SET)
    active_zones = {e['data']['zone'] for e in events}

    print(f"Unique players: {unique_players}")
    print(f"Unique events: {unique_events}")
    print(f"Active zones: {active_zones}")


def combined_analysis() -> None:
    print("\n== Combined Analysis ===")
    # Load example data
    events: list = load_game_data()

    # === COUNT UNIQUE PLAYERS ===
    # set
    unique_players = {e['player'] for e in events}
    # count set elements
    total_players = len(unique_players)

    # === COUNT UNIQUE EVENTS ===
    # set
    unique_events = {e['event_type'] for e in events}
    # count set elements
    total_unique_e = len(unique_events)

    # === EACH PLAYER MAX SCORE
    # 1.- lista (set) unica de jugadores
    unique_players = {e['player'] for e in events}
    # 2.- Dictionary player:max_score
    max_score_by_player = {
        player: max(e['data']['score_delta']
                    for e in events if e['player'] == player)
        for player in unique_players
        }

    # === EACH PLAYER TOTAL SCORE ===
    # 1.- Dictionary player:total_score
    total_score_by_player = {
        player: sum(e['data']['score_delta']
                    for e in events if e['player'] == player)
        for player in unique_players
        }

    # === AVERAGE SCORE ===
    values = total_score_by_player.values()
    average = sum(values)/len(values)

    # === PLAYER WITH THE GREATEST SCORE ===
    max_value: int = 0
    max_key: str = ''
    for k, v in total_score_by_player.items():
        if v > max_value:
            max_value = v
            max_key = k

    print(f"Total players: {total_players}")
    print(f"Total unique events: {total_unique_e}")
    print(f"Max score by achievement: {max_score_by_player}")
    print(f"Total score: {total_score_by_player}")
    print(f"Average score: {average}")
    print(f"Top performer: {max_key} ({max_value} points)")


if __name__ == "__main__":
    print("=== Game Analytics Dashboard ===")
    list_comprehension()
    dict_comprehension()
    set_comprehension()
    combined_analysis()
