premise_time = 82
hypothesis_time = 12

# the hypothesis refers to the exact time of departure, while the premise mentions an estimate
if hypothesis_time < premise_time:
    # check if the hypothesis value contradicts the estimate of less than 'premise_time'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time of departure
    # any time of departure greater than or equal to 'premise_time' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
