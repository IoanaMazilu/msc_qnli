rainfall_premise = 25
rainfall_hypothesis = 25

# the hypothesis refers to the total rainfall in the first two weeks of March mentioned in the premise
if rainfall_hypothesis <= rainfall_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives the exact amount of rainfall
    # any amount of rainfall greater than 'rainfall_premise' cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
