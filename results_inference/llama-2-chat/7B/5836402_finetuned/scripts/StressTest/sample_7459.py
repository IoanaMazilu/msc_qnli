ratio_premise = 2/4
ratio_hypothesis = 1/4

# the hypothesis refers to the ratio of movie lists that must be considered for'movie of the year', mentioned in the premise
if ratio_hypothesis >= ratio_premise:
    # check if the hypothesis value contradicts the estimate of less than 'ratio_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio
    # any ratio less than 'ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
