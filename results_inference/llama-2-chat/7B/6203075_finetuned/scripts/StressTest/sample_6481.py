balls_premise = 4
balls_hypothesis = 3
board_games_premise = 6
board_games_hypothesis = 6

# the hypothesis refers to the number of types of balls and board games in the toy store
if balls_premise <= balls_hypothesis and board_games_premise == board_games_hypothesis:
    # check if the number of types of balls and board games in the hypothesis contradicts the premise
    label = "contradiction"
elif balls_premise > balls_hypothesis:
    # if the number of types of balls in the hypothesis is less than in the premise, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
