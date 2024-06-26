premise_average_raise = 2
hypothesis_average_raise = 6

# the hypothesis refers to the average raise mentioned in the premise
if hypothesis_average_raise < premise_average_raise:
    # check if the hypothesis value contradicts the average raise in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the average raise
    # any average raise greater than 'premise_average_raise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
