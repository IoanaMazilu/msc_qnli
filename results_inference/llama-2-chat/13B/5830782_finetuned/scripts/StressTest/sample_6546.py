distance_premise = 15
distance_hypothesis = 85

# the hypothesis refers to the same distance mentioned in the premise
if distance_premise > distance_hypothesis:
    # check if the distance in the premise contradicts the estimate of less than 'distance_hypothesis'
    label = "contradiction"
elif distance_premise < distance_hypothesis:
    # if the distance in the premise is less than 'distance_hypothesis', we can infer entailment
    label = "entailment"
else:
    # if the distance in the premise is equal to 'distance_hypothesis', it's neutral
    label = "neutral"

print(label)
