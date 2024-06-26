distance_premise = 31
distance_hypothesis = 81

# the hypothesis refers to the distance between X and Y mentioned in the premise
if distance_premise > distance_hypothesis:
    # check if the distance in the premise contradicts the estimate of less than 'distance_hypothesis'
    label = "contradiction"
elif distance_premise < distance_hypothesis:
    # if the distance in the premise is less than 'distance_hypothesis', we can infer entailment
    label = "entailment"
else:
    # if the distance in the premise is equal to 'distance_hypothesis', it is also entailed
    label = "entailment"

print(label)
