required_ratio_premise = 1/4
required_ratio_hypothesis = 6/4

# the hypothesis refers to the same requirement for a film to be considered for "movie of the year"
if required_ratio_hypothesis <= required_ratio_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives only an estimate for the required ratio
    # any ratio greater than'required_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
