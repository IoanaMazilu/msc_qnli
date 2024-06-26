distance_traveled_premise = 8/2
distance_traveled_hypothesis = 1/2

# the hypothesis refers to the distance traveled by Maria, which is also mentioned in the premise
if distance_traveled_hypothesis >= distance_traveled_premise:
    # check if the distance traveled in the hypothesis contradicts the premise
    label = "contradiction"
elif distance_traveled_hypothesis < distance_traveled_premise:
    # check if the distance traveled in the hypothesis is less than the distance traveled in the premise
    label = "entailment"
else:
    # if the distance traveled in the hypothesis is equal to the distance traveled in the premise, we can infer entailment
    label = "neutral"

print(label)
