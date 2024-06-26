minutes_dan_leaves_premise = 120
minutes_dan_leaves_hypothesis = 120

# the hypothesis refers to the time Dan leaves City A, also mentioned in the premise
if minutes_dan_leaves_hypothesis <= minutes_dan_leaves_premise:
    # check if the hypothesis value contradicts the estimate of more than'minutes_dan_leaves_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time Dan leaves
    # any time greater than'minutes_dan_leaves_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
