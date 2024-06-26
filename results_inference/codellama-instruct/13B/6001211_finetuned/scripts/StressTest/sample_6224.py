share_difference_premise = 200
share_difference_hypothesis = 200

# the hypothesis refers to the difference between Mani and Rani's share mentioned in the premise
if share_difference_hypothesis <= share_difference_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives an exact number for the share difference
    # any number greater than'share_difference_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
