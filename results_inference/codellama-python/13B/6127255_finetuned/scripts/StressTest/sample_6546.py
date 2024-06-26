distance_premise = 15
distance_hypothesis = 85

# the hypothesis refers to the distance between West-Town to East-Town mentioned in the premise
if distance_premise > distance_hypothesis:
    # check if the distance in the premise contradicts the estimate of less than 'distance_hypothesis'
    label = "contradiction"
elif distance_premise == distance_hypothesis:
    # check if the distance in the premise equals the estimate of 'distance_hypothesis'
    label = "contradiction"
else:
    # if the distance in the premise is less than 'distance_hypothesis', we can infer entailment
    label = "entailment"

print(label)
