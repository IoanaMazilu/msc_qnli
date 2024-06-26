steps_premise = 60
steps_hypothesis = 80

# the hypothesis refers to the number of steps climbed in a given time, which is also mentioned in the premise
if steps_hypothesis <= steps_premise:
    # check if the estimate of'steps_hypothesis' contradicts the number of steps climbed in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of steps climbed
    # any number of steps greater than'steps_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
