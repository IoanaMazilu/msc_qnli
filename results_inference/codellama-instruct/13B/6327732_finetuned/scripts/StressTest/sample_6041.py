xavier_speed_premise = 90
xavier_speed_hypothesis = 90

# the hypothesis refers to the speed of Xavier mentioned in the premise
if xavier_speed_hypothesis <= xavier_speed_premise:
    # check if the estimate of 'xavier_speed_hypothesis' contradicts the speed of Xavier in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed of Xavier
    # any speed greater than 'xavier_speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
