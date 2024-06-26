required_ratio_premise = 2/4
required_ratio_hypothesis = 1/4

# the hypothesis refers to the same requirement for a film to be considered for "movie of the year"
# as mentioned in the premise
if required_ratio_hypothesis >= required_ratio_premise:
    # check if the required ratio in the hypothesis contradicts the requirement in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the required ratio
    # any ratio less than'required_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
