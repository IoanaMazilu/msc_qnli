perfect_score_premise = 21
games_played_premise = 3
points_per_round_hypothesis = 7.0

# the hypothesis refers to the number of points earned per round, which are also mentioned in the premise
# compute the total number of points earned in the premise
total_points_premise = perfect_score_premise * games_played_premise
if total_points_premise!= points_per_round_hypothesis * games_played_premise:
    # check if the number of points in the hypothesis contradicts the number of points from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
