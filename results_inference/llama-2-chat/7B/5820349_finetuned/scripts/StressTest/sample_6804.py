distance_premise = 31
distance_hypothesis = 81

# the hypothesis refers to the distance between X and Y mentioned in the premise
if distance_premise >= distance_hypothesis:
    # check if the distance in the premise contradicts the estimate of less than 'distance_hypothesis'
    label = "contradiction"
else:
    # if the premise value does not contradict the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)
