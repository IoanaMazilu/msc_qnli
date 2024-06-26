premise_value = 2
hypothesis_value = 7

# the hypothesis refers to the same equation mentioned in the premise, with a different coefficient for (AE + FC)
if premise_value >= hypothesis_value:
    # check if the coefficient in the premise contradicts the coefficient in the hypothesis
    label = "contradiction"
else:
    # the premise gives a specific coefficient for (AE + FC)
    # any coefficient greater than the one in the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
