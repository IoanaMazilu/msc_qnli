distance_traveled_premise = 1/2
distance_traveled_hypothesis = 7/2

# the hypothesis refers to the distance traveled by Maria before stopping, which is also mentioned in the premise
if distance_traveled_hypothesis == distance_traveled_premise:
    # check if the distance traveled in the hypothesis matches the distance traveled in the premise
    label = "entailment"
elif distance_traveled_hypothesis > distance_traveled_premise:
    # check if the distance traveled in the hypothesis contradicts the distance traveled in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
