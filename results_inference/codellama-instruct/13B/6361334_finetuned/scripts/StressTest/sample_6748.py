butter_mixed_premise = 84
butter_mixed_hypothesis = 44

# the hypothesis refers to the quantity of butter mixed, which is also mentioned in the premise
if butter_mixed_hypothesis >= butter_mixed_premise:
    # check if the hypothesis value contradicts the estimate of less than 'butter_mixed_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the quantity of butter mixed
    # any quantity of butter less than 'butter_mixed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
