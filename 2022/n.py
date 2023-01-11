from itertools import combinations
for n in range(4, 15):
    pairings = []
    players = range(n)
    for chosen_players in combinations(players, 4):
        for pairing1 in combinations(chosen_players, 2):
            pairing2 = tuple(player for player in chosen_players if player not in pairing1)
            pairing1 = sorted(pairing1)
            pairing2 = sorted(pairing2)
            lineup = sorted([pairing1, pairing2])
            if lineup not in pairings:
                pairings.append(lineup)
    print(f'with {n} players there are {len(pairings)}')
       