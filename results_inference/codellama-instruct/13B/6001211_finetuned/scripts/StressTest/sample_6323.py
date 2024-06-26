chess_players_premise = 4
chess_players_hypothesis = 4

# the hypothesis refers to the number of chess players in Villa's chess club tournament mentioned in the premise
if chess_players_hypothesis >= chess_players_premise:
    # check if the hypothesis value contradicts the exact number of 'chess_players_premise'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
