points_per_round_hypothesis = 7.0
points_per_round_premise = 21
games_premise = 3

# the hypothesis refers to the points per round, which are also mentioned in the premise
# compute the total points per round from the premise
total_points_per_round_premise = points_per_round_premise / games_premise
if total_points_per_round_hypothesis!= total_points_per_round_premise:
    # check if the points per round in the hypothesis contradicts the points per round from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
