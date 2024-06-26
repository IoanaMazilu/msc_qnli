steps_premise = 60
steps_hypothesis = 80

# the hypothesis refers to the number of steps climbed in a certain time, mentioned in the premise
if steps_hypothesis <= steps_premise:
    # check if the hypothesis value contradicts the estimate of'steps_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the number of steps climbed, and the hypothesis value cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
