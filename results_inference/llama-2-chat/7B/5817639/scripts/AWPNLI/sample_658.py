per_round_hypothesis = 7.0
total_points_premise = 21

# check if the number of points per round in the hypothesis contradicts the total number of points in the premise
if per_round_hypothesis!= total_points_premise:
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
