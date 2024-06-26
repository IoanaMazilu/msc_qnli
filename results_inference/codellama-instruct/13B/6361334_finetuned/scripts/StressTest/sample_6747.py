butter_mixed_premise = 44
butter_mixed_hypothesis = 84

# the hypothesis refers to the quantity of butter mixed, which is also mentioned in the premise
if butter_mixed_hypothesis >= butter_mixed_premise:
    # check if the hypothesis value contradicts the quantity of butter mixed in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the quantity of butter mixed
    # any quantity of butter mixed less than 'butter_mixed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
