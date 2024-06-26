distance_traveled_premise = 1/2
distance_traveled_hypothesis = 8/2

# the hypothesis refers to the distance traveled by Maria, which is also mentioned in the premise
if distance_traveled_hypothesis <= distance_traveled_premise:
    # check if the hypothesis value contradicts the premise
    label = "entailment"
else:
    # if the hypothesis value is greater than the premise, it contradicts the premise
    label = "contradiction"

print(label)
