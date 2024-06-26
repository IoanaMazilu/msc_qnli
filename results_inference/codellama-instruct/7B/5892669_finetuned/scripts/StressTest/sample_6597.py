distance_apart_premise = 15
distance_apart_hypothesis = 35

# the hypothesis refers to the distance between Efrida and Frazer mentioned in the premise
if distance_apart_premise > distance_apart_hypothesis:
    # check if the estimate of 'distance_apart_hypothesis' contradicts the distance in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
