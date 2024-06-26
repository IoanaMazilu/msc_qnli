semifinal_games_premise = 2
semifinal_games_hypothesis = 2
final_game_premise = 1
final_game_hypothesis = 1

# the hypothesis mentions the number of national semifinal games and the final game, which are also mentioned in the premise
if semifinal_games_hypothesis!= semifinal_games_premise:
    # check if the number of semifinal games in the hypothesis contradicts the number of semifinal games reported in the premise
    label = "contradiction"
elif final_game_hypothesis!= final_game_premise:
    # check if the number of final games from the hypothesis contradicts the number of final games in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
