ratio_sheep_horses_premise = 1/7
ratio_sheep_horses_hypothesis = 6/7

# the hypothesis refers to the ratio of sheep to horses at the Stewart farm mentioned in the premise
if ratio_sheep_horses_hypothesis <= ratio_sheep_horses_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of sheep to horses
    # any ratio greater than 'ratio_sheep_horses_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
