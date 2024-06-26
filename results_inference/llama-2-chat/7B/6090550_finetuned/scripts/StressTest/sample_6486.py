rainfall_premise = 25
rainfall_hypothesis = 65

# the hypothesis refers to the total rainfall in Springdale during the first two weeks of March
if rainfall_hypothesis <= rainfall_premise:
    # check if the hypothesis value contradicts the premise value
    label = "entailment"
else:
    # if the hypothesis value is greater than the premise value, it contradicts
    label = "contradiction"

print(label)
