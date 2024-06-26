butter_mixed_premise = 27
butter_mixed_hypothesis = 77

# the hypothesis refers to the weight of butter mixed by Raman, which is also mentioned in the premise
if butter_mixed_hypothesis <= butter_mixed_premise:
    # check if the estimate of 'butter_mixed_hypothesis' contradicts the weight of butter mixed in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the weight of butter mixed
    # any weight of butter greater than 'butter_mixed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
