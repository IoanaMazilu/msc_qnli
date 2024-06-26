points_premise = 362.75
points_hypothesis = 357.39

# the hypothesis and premise mention the closing points of Sensex and Nifty
if points_hypothesis > points_premise:
    # check if the closing points in the hypothesis contradicts the closing points in the premise
    label = "contradiction"
elif points_hypothesis < points_premise:
    # check if the closing points in the hypothesis contradicts the closing points in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
