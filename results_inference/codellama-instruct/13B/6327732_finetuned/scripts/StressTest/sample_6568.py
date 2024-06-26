# extract the numerical entities from the premise and hypothesis
premise_time = 7/2
hypothesis_time = 1/2

# compare the time estimates
if premise_time <= hypothesis_time:
    # check if the hypothesis value contradicts the estimate of less than 'premise_time'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time
    # any time greater than 'premise_time' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
