import statistics

players_height: list[float] = []
counter_above_2: int = 0
SENTINEL: int = -999  # const

while True:
    height: float = float(input('whats your height?'))
    if height == SENTINEL:
        break
    if not 1.6 <= height <= 30:
        continue

    # acceptable height
    players_height.append(height)
    if height > 2.0:
        counter_above_2 += 1

#if len(players_height) > 0:
# if [] ==> False
# if [1 or more] ==> True
#if players_height == True:
if players_height:
    players: int = len(players_height)
    tallest_player: float = max(players_height)
    shortest_player: float = min(players_height)
    avg_height: float = statistics.mean(players_height)
    counter_above_avg: int = 0
    for i in range(len(players_height)):
        if players_height[i] > avg_height:
            counter_above_avg += 1
    # print ...

