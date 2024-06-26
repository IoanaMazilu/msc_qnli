ratio_premise = 4 / 3
ratio_hypothesis = 4 / 3

# the hypothesis refers to the ratio of ages between Sandy and Molly mentioned in the premise
if ratio_hypothesis <= ratio_premise:
    # check if the hypothesis value contradicts the ratio of ages in the premise
    label = "contradiction"
else:
    # the premise gives the exact ratio of ages
    # any ratio greater than 'ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
