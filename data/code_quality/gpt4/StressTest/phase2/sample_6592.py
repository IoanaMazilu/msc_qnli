floor_premise = 51
floor_hypothesis = 71
rate_premise = 93
rate_hypothesis = 93

# the hypothesis gives a specific floor number and the rate of ride down, both referenced in the premise
if floor_hypothesis <= floor_premise:
    # check if 'floor_hypothesis' contradicts the premise's estimate of more than 'floor_premise' 
    label = "contradiction"
elif rate_hypothesis != rate_premise:
    # check if the rate of ride down in the hypothesis contradicts the rate mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the floor number
    # any floor number greater than 'floor_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
