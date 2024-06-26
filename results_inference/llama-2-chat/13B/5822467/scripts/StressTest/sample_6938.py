floor_premise = 11
rate_premise = 57
floor_hypothesis = 12
rate_hypothesis = 57

# the hypothesis refers to the floor where Stalin gets on the elevator and the rate at which he rides up
if floor_hypothesis > floor_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif rate_hypothesis!= rate_premise:
    # check if the rate at which Stalin rides up in the hypothesis contradicts the rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
