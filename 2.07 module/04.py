def unity_dict(dict):
    tuple_players = list()
    for key, value in dict.items():
        new_value = key + value
        tuple_players.append(new_value)
    return tuple_players

players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

result = unity_dict(players)
print(result)