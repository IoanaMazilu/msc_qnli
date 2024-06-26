butter_mixed_premise = 27
butter_mixed_hypothesis = 47

# the hypothesis refers to the quantity of butter mixed, which is less than the quantity mentioned in the premise
if butter_mixed_hypothesis >= butter_mixed_premise:
    # check if the hypothesis value contradicts the quantity of butter mixed in the premise
    label = "contradiction"
else:
    # the premise gives an exact quantity of butter mixed, but the hypothesis gives a lesser quantity
    # any quantity of butter mixed less than 'butter_mixed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
