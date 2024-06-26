butter_weight_premise = 24
butter_weight_hypothesis = 44

# the hypothesis mentions the weight of the butter mixed by Raman, also addressed in the premise
if butter_weight_hypothesis <= butter_weight_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif butter_weight_premise >= butter_weight_hypothesis:
    # check if the premise value contradicts the hypothesis value
    label = "contradiction"
else:
    # the premise gives an exact quantity for the butter weight
    # any weight less than 'butter_weight_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
