ratio_ages_premise = 8 / 2
ratio_ages_hypothesis = 3 / 2

# the hypothesis mentions the ratio of ages of the same persons as in the premise
if ratio_ages_hypothesis >= ratio_ages_premise:
    # check if the ratio of ages in the hypothesis contradicts the premise estimate
    label = "contradiction"
elif ratio_ages_hypothesis == ratio_ages_premise:
    # check if the ratio of ages in the hypothesis equals the premise estimate
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of ages
    # any ratio less than 'ratio_ages_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
