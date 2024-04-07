# Premise: If Jake is 155 km away from Kay at 6 am, and also 155 km away from Kay at 11 am, then how fast is Kay driving (in kilometers per hour)?
# Hypothesis: If Jake is more than 155 km away from Kay at 6 am, and also 155 km away from Kay at 11 am, then how fast is Kay driving (in kilometers per hour)?
# Golden Label: contradiction

jake_distance_premise = 155
jake_distance_hypothesis = 155

# the hypothesis refers to the distance between Jake and Kay mentioned in the premise
if jake_distance_hypothesis < jake_distance_premise:
    # check if the value of 'jake_distance_hypothesis' contradicts the distance mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

