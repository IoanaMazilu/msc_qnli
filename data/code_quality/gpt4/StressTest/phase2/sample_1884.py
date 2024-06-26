distance_walked_premise = 45
distance_walked_hypothesis = 55

# the hypothesis refers to the distance walked by Matthew, also mentioned in the premise
if distance_walked_premise >= distance_walked_hypothesis:
    # check if the estimate of 'distance_walked_hypothesis' contradicts the distance walked in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
