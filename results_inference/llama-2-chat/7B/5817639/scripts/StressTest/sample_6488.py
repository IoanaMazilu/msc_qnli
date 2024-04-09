rainfall_premise = 25
rainfall_hypothesis = 25

# the hypothesis refers to the same quantity as the premise
if rainfall_hypothesis <= rainfall_premise:
    # check if the hypothesis value contradicts the estimate of 'rainfall_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of roses
    # any number of roses greater than 'roses_vase_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
