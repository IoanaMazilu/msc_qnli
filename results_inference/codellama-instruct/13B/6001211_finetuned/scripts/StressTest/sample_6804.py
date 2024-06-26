distance_premise = 31
distance_hypothesis = 81

# the hypothesis refers to the distance between X and Y mentioned in the premise
if distance_premise >= distance_hypothesis:
    # check if the estimate of 'distance_hypothesis' contradicts the distance in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
