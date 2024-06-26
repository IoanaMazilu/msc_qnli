points_premise = 1000
points_hypothesis = 1000

# the hypothesis and premise both mention the same number of points lost by Dow
if points_hypothesis != points_premise:
    # check if the number of points in the hypothesis contradicts the number of points in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
