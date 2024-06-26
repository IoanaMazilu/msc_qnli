chess_players_premise = 4
chess_players_hypothesis = 8

# the hypothesis refers to the number of chess players in the premise
if chess_players_premise >= chess_players_hypothesis:
    # check if the number of chess players in the premise contradicts the hypothesis
    label = "contradiction"
else:
    # if the number of chess players in the premise does not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)
