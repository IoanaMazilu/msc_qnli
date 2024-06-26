chess_players_premise = 4
chess_players_hypothesis = 4

# the hypothesis refers to the number of chess players mentioned in the premise
if chess_players_hypothesis >= chess_players_premise:
    # check if the hypothesis value contradicts the number of chess players in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
