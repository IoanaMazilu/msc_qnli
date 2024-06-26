points_premise = 362.75
points_hypothesis = 357.39

# the hypothesis and premise mention the points of the Sensex closing
if points_hypothesis > points_premise:
    # check if the points in the hypothesis contradict the points in the premise
    label = "contradiction"
elif points_hypothesis < points_premise:
    # check if the points in the hypothesis are less than the points in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
