rainfall_premise = 25
rainfall_hypothesis = 65

# the hypothesis talks about the total rainfall in Springdale during the first two weeks of March
# the premise gives an estimate for the total rainfall in Springdale during the first two weeks of March
if rainfall_premise <= rainfall_hypothesis:
    # check if the estimate of 'rainfall_hypothesis' contradicts the number of inches in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the total rainfall in Springdale during the first two weeks of March
    # any number of inches greater than 'rainfall_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
