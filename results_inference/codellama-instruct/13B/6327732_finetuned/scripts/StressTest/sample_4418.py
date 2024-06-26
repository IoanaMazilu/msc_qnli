premise_score = 2
hypothesis_score = 5

# the hypothesis refers to a different score than the premise
if hypothesis_score!= premise_score:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the hypothesis value is the same as the premise value
    # any score greater than or equal to the premise value is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
