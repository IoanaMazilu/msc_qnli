floor_premise = 61
floor_hypothesis = 11
rate_premise = 57
rate_hypothesis = 57

# the hypothesis refers to the floor and rate of the elevator ride mentioned in the premise
if floor_hypothesis >= floor_premise:
    # check if the estimate of 'floor_hypothesis' contradicts the floor in the premise
    label = "contradiction"
elif rate_hypothesis!= rate_premise:
    # check if the rate in the hypothesis contradicts the rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
