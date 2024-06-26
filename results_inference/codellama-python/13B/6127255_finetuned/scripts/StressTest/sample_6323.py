chess_players_premise = 4
chess_players_hypothesis = 4

# the hypothesis refers to the number of chess players in the premise
if chess_players_hypothesis >= chess_players_premise:
    # check if the hypothesis value contradicts the exact number of 'chess_players_premise'
    label = "contradiction"
else:
    # the premise gives an exact number of chess players
    # any number of chess players less than 'chess_players_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
