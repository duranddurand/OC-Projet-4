from Model import Tournament


def pairing(joueurs: Tournament.players) -> list:

    tuples = []

    for j in joueurs:
        tuples.append(j.tupler())

    leaderboard = sorted(tuples, key=lambda player: player[2])
    half = len(leaderboard) // 2
    pairs = []

    for rank in range(half):
        pairs.append((leaderboard[rank], leaderboard[rank + half]))
    return pairs
