rainfall_premise = 20
rainfall_hypothesis = 40

# the hypothesis refers to the amount of rainfall in Springdale during the first two weeks of June, which is also mentioned in the premise
if rainfall_hypothesis <= rainfall_premise:
    # check if the reported rainfall in the hypothesis contradicts the premise estimate of more than 'rainfall_premise' inches
    label = "contradiction"
else:
    # the premise provides only an estimate for the rainfall
    # any amount of rainfall greater than 'rainfall_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
