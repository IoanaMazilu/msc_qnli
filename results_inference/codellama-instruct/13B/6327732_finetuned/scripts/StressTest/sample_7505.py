time_premise = 10
time_hypothesis = 60

# the hypothesis refers to a longer time period than the premise
if time_hypothesis <= time_premise:
    # check if the hypothesis value contradicts the estimate of 'time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time period
    # any time period greater than 'time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
