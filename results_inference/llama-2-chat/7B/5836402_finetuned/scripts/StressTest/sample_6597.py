distance_premise = 15
distance_hypothesis = 35

# the hypothesis refers to the distance between Efrida and Frazer mentioned in the premise
if distance_hypothesis >= distance_premise:
    # check if the estimate of 'distance_hypothesis' contradicts the distance mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
