rainfall_premise = 25
rainfall_hypothesis = 25

# the hypothesis refers to the number of rainfall inches in the premise
if rainfall_hypothesis <= rainfall_premise:
    # check if the hypothesis value contradicts the number of rainfall inches in the premise
    label = "contradiction"
else:
    # any number of rainfall inches greater than 'rainfall_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
