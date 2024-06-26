chess_players_premise = 4
chess_players_hypothesis = 8

# the hypothesis talks about the number of chess players, referenced also in the premise
if chess_players_premise >= chess_players_hypothesis:
    # check if the number of chess players in the premise contradicts the hypothesis estimate of less than 'chess_players_hypothesis'
    label = "contradiction"
else:
    # the hypothesis gives an estimate for the number of chess players
    # any number of chess players less than 'chess_players_hypothesis' is consistent with the hypothesis, but cannot be explicitly entailed from the hypothesis
    label = "entailment"

print(label)
