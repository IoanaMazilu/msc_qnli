butter_weight_premise = 44
butter_weight_hypothesis = 44

# the hypothesis talks about the weight of butter mixed, which is also mentioned in the premise
if butter_weight_hypothesis <= butter_weight_premise:
    # check if the hypothesis value contradicts the estimate of more than 'butter_weight_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the weight of butter
    # any weight greater than 'butter_weight_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
