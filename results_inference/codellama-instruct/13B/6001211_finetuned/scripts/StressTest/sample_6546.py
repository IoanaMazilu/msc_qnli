distance_premise = 15
distance_hypothesis = 85

# the hypothesis refers to the distance between West-Town to East-Town mentioned in the premise
if distance_premise > distance_hypothesis:
    # check if the distance in the premise contradicts the estimate of less than 'distance_hypothesis'
    label = "contradiction"
elif distance_premise < distance_hypothesis:
    # check if the distance in the premise is less than the 'distance_hypothesis'
    label = "entailment"
else:
    # if the distance in the premise is equal to the 'distance_hypothesis', it is consistent with the hypothesis but cannot be explicitly entailed from it
    label = "neutral"

print(label)
