rainfall_premise = 25
rainfall_hypothesis = 65

# the hypothesis refers to the total rainfall in the premise
if rainfall_hypothesis <= rainfall_premise:
    # check if the hypothesis value contradicts the total rainfall reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the total rainfall
    # any total rainfall greater than 'rainfall_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)