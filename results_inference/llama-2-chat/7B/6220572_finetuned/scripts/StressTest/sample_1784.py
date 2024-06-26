old_ratio_premise = 5/3
old_ratio_hypothesis = 5/3

# the hypothesis refers to the ratio of ages between the two mentioned individuals in the premise
if old_ratio_hypothesis <= old_ratio_premise:
    # check if the hypothesis value contradicts the ratio of ages in the premise
    label = "contradiction"
else:
    # the premise gives a specific ratio of ages
    # any ratio greater than 'old_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
