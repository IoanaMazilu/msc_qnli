premise_ratio = 4/2
hypothesis_ratio = 1/2

# the hypothesis mentions a ratio greater than the one in the premise
if hypothesis_ratio > premise_ratio:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives an estimate for the ratio, but any ratio greater than the premise value is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
