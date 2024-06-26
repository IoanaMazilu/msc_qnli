average_raise_premise = 2
average_raise_hypothesis = 6

# the hypothesis refers to the average raise in the premise
if average_raise_hypothesis <= average_raise_premise:
    # check if the estimate of 'average_raise_hypothesis' contradicts the average raise in the premise
    label = "contradiction"
else:
    # any average raise greater than 'average_raise_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
