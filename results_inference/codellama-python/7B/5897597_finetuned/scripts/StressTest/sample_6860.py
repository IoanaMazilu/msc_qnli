distance_walked_premise = 4
distance_walked_hypothesis = 4
time_walked = 1.25 # 1 hour and 15 minutes converted to hours

# the hypothesis refers to the distance walked by Jack mentioned in the premise
if distance_walked_hypothesis <= distance_walked_premise:
    # check if the hypothesis value contradicts the distance walked in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
