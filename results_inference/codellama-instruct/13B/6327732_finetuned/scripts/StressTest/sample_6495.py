premise_time = 44
premise_speed = 50
hypothesis_time = 24
hypothesis_speed = 50

# the hypothesis refers to the time taken for the bus to reach Pune
if hypothesis_time <= premise_time:
    # check if the estimate of 'hypothesis_time' contradicts the time taken in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the time taken
    # any time greater than 'premise_time' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
