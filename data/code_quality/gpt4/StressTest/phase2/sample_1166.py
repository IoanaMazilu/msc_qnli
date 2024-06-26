distance_traveled_premise = 1/2
distance_traveled_hypothesis = 4/2

# the hypothesis refers to the distance Maria traveled during a car trip, mentioned also in the premise
if distance_traveled_premise != distance_traveled_hypothesis:
    # check if the distance traveled in the hypothesis contradicts the distance traveled reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
