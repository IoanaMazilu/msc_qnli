start_floor_premise = 11
start_floor_hypothesis = 71
rate_premise = 87
rate_hypothesis = 87

# the hypothesis refers to the starting floor and rate of the elevator mentioned in the premise
if start_floor_premise!= start_floor_hypothesis:
    # check if the starting floor in the hypothesis contradicts the starting floor reported in the premise
    label = "contradiction"
elif rate_premise!= rate_hypothesis:
    # check if the rate of the elevator in the hypothesis contradicts the rate of the elevator reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
