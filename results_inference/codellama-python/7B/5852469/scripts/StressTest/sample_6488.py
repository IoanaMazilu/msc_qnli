rainfall_springdale_premise = 25

# the hypothesis refers to the same event as the premise
if rainfall_springdale_premise <= 25:
    # check if the estimate of 'rainfall_springdale_premise' contradicts the number of 25 inches
    label = "contradiction"
else:
    # the premise gives only an estimate for the total rainfall in Springdale
    # any number of inches greater than 'rainfall_springdale_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
