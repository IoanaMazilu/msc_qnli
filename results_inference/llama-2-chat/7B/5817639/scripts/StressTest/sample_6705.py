ratio_premise = 4/3
ratio_hypothesis = 8/3

# check if the hypothesis ratio contradicts the premise ratio
if ratio_hypothesis > ratio_premise:
    label = "contradiction"
elif ratio_hypothesis < ratio_premise:
    # check if the hypothesis ratio is consistent with the premise ratio
    label = "entailment"
else:
    # the premise ratio is an estimate, and any ratio greater than or equal to it is consistent with the premise
    label = "neutral"

print(label)
