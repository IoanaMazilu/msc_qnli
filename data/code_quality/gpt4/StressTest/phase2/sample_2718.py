distance_apart_premise = 10
distance_apart_hypothesis = 70

# the hypothesis refers to the distance between Efrida and Frazer mentioned in the premise
if distance_apart_premise > distance_apart_hypothesis:
    # check if the distance in the premise contradicts the estimate of 'distance_apart_hypothesis'
    label = "contradiction"
else:
    # if the 'distance_apart_premise' does not contradict the 'distance_apart_hypothesis', we can infer entailment
    label = "entailment"

print(label)
