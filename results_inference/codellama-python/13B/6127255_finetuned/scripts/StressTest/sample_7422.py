start_floor_premise = 51
start_floor_hypothesis = 61
rate_premise = 63
rate_hypothesis = 63

# the hypothesis refers to the starting floor and the rate of the elevator ride mentioned in the premise
if start_floor_hypothesis <= start_floor_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif rate_hypothesis!= rate_premise:
    # check if the rate in the hypothesis contradicts the rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
