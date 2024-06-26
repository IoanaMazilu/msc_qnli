floor_premise = 51
floor_hypothesis = 61
elevator_rate_premise = 63
elevator_rate_hypothesis = 63

# the hypothesis refers to a different scenario than the premise
if floor_hypothesis < floor_premise:
    # check if the hypothesis value contradicts the estimate of the floor in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the floor,
    # any floor less than 'floor_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)