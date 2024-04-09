ratio_premise = 3
ratio_hypothesis = 4

# the hypothesis refers to a different ratio than the premise
if ratio_hypothesis <= ratio_premise:
    # check if the hypothesis ratio contradicts the premise ratio
    label = "contradiction"
else:
    # the premise ratio is not explicitly entailed from the hypothesis ratio
    label = "neutral"

print(label)
