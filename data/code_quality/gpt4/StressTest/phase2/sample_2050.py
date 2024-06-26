ratio_ages_premise = 5/9
ratio_ages_hypothesis = 7/9

# the hypothesis refers to a specific ratio of ages mentioned in the premise
if ratio_ages_hypothesis <= ratio_ages_premise:
    # check if the hypothesis value contradicts the estimate of more than 'ratio_ages_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of ages
    # any ratio greater than 'ratio_ages_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
