ratio_ages_premise = 2/3
ratio_ages_hypothesis = 7/3

# the hypothesis refers to the age ratio of Anil and his son mentioned in the premise
if ratio_ages_hypothesis <= ratio_ages_premise:
    # check if the ratio in the hypothesis contradicts the estimate of more than 'ratio_ages_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the age ratio
    # any ratio greater than 'ratio_ages_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
