balls_types_premise = 5
board_games_types_premise = 6
balls_types_hypothesis = 3
board_games_types_hypothesis = 6

# the hypothesis talks about the number of ball types and board games types, which are also mentioned in the premise
if balls_types_hypothesis <= balls_types_premise and board_games_types_hypothesis <= board_games_types_premise:
    # check if the number of ball types and board games types in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the number of ball types and board games types in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
