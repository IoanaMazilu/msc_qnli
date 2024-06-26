distance_traveled_premise = 1/2
distance_traveled_hypothesis = 8/2

# the hypothesis refers to the distance traveled by Maria during a car trip, also mentioned in the premise
if distance_traveled_hypothesis <= distance_traveled_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
