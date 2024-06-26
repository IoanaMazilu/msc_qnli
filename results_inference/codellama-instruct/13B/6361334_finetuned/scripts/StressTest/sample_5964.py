hours_premise = 4
hours_hypothesis = 8

# the hypothesis refers to the time it took to drive from City A to City B
if hours_hypothesis <= hours_premise:
    # check if the estimate of 'hours_hypothesis' contradicts the time in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the time it took to drive from City A to City B
    # any time greater than 'hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
