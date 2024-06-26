ratio_premise = 6 / 9
ratio_hypothesis = 7 / 9

# the hypothesis refers to a ratio of ages, also mentioned in the premise
if ratio_hypothesis <= ratio_premise:
    # check if the ratio in the hypothesis contradicts the 'more than' estimate in the premise
    label = "contradiction"
elif ratio_hypothesis > ratio_premise:
    # any ratio greater than 'ratio_premise' is consistent with the premise but cannot be explicitly entailed from it
    label = "neutral"

print(label)
