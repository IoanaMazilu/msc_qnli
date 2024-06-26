points_per_game = 21 / 3
points_per_game_premise = 7.0

# the hypothesis refers to the points per game, which is also mentioned in the premise
# the premise gives the exact points per game
if points_per_game_premise!= points_per_game:
    # check if the points per game in the hypothesis contradicts the points per game in the premise
    label = "contradiction"
else:
    # if the points per game in the hypothesis does not contradict the points per game in the premise, we can infer entailment
    label = "entailment"

print(label)
