premise_time = 12
hypothesis_time = 62

# the hypothesis refers to the time of departure of the train, which is mentioned in the premise
if hypothesis_time <= premise_time:
    # check if the estimate of 'hypothesis_time' contradicts the time of departure in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the time of departure
    # any time greater than 'premise_time' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
