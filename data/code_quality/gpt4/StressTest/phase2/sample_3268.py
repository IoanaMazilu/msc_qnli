floor_premise = 11
floor_hypothesis = 41
rate_premise = 63
rate_hypothesis = 63

# the hypothesis talks about the floor Joyce is on and the rate of the elevator, both referenced also in the premise
if floor_hypothesis <= floor_premise:
    # check if the floor number in the hypothesis contradicts the estimate of more than 'floor_premise'
    label = "contradiction"
elif rate_hypothesis != rate_premise:
    # check if the rate in the hypothesis contradicts the rate mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the floor number
    # any floor number greater than 'floor_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
