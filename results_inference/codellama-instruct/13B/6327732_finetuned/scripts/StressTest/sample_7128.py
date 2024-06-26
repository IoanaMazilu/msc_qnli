premise_value = 7/12
hypothesis_value = 4/12

# the hypothesis refers to a value greater than the premise value
if hypothesis_value <= premise_value:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives an estimate for the value of a sum of money
    # any value greater than 'premise_value' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
