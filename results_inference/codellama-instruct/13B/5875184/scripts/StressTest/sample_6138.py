premise_time = 7
hypothesis_time = 4

# the hypothesis mentions a time more than the premise time
if hypothesis_time <= premise_time:
    # check if the hypothesis value contradicts the premise time
    label = "contradiction"
else:
    # the premise gives an estimate for the time
    # any time greater than 'premise_time' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
