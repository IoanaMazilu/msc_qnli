premise_time = 18
hypothesis_time = 78

# the hypothesis refers to the time it takes Jim to stretch and the time it takes Cara to run
if hypothesis_time <= premise_time:
    # check if the hypothesis value contradicts the estimate of 'premise_time'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time it takes Jim to stretch
    # any time greater than 'premise_time' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
