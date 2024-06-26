premise_time = 7*24*60 + 1
hypothesis_time = 6*24*60 + 1

# the hypothesis refers to the time required by a train to cover the distance between Chennai and Jammu
if hypothesis_time <= premise_time:
    # check if the estimate of 'hypothesis_time' contradicts the time in the premise
    label = "contradiction"
else:
    # the premise gives an exact time, but the hypothesis gives an estimate
    # any time greater than 'premise_time' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
