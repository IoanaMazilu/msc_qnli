ratio_ages_premise = 4/3
ratio_ages_hypothesis = 4/3

# the hypothesis discusses the ratio of ages between Sandy and Molly which is also mentioned in the premise
if ratio_ages_hypothesis <= ratio_ages_premise:
    # check if the ratio of ages in hypothesis contradicts the ratio of ages in premise
    label = "contradiction"
else:
    # the premise gives exact ratio of ages
    # any ratio greater than 'ratio_ages_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
