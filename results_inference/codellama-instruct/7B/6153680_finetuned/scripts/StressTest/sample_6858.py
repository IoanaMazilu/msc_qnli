distance_walked_premise = 4
distance_walked_hypothesis = 3

# the hypothesis refers to the distance walked by Jack, which is also mentioned in the premise
if distance_walked_hypothesis >= distance_walked_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)