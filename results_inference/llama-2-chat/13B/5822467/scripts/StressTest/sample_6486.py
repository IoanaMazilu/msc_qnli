rainfall_premise = 25
rainfall_hypothesis = 65

# the hypothesis refers to the total rainfall in Springdale during the first two weeks of March
if rainfall_premise <= rainfall_hypothesis:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives a specific value for the total rainfall, while the hypothesis gives a less specific value
    # any value less than 65 inches is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
