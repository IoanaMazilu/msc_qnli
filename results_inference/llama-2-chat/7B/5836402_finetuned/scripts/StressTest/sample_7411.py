butter_weight_premise = 47
butter_weight_hypothesis = 27

# the hypothesis talks about the weight of butter mixed, referenced also in the premise
if butter_weight_hypothesis >= butter_weight_premise:
    # check if the hypothesis value contradicts the estimate of less than 'butter_weight_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the weight of butter
    # any weight less than 'butter_weight_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
