time_jim_stretches_premise = 18
time_jim_stretches_hypothesis = 78

# the hypothesis refers to the time it takes Jim to stretch and the time it takes for Cara to run
if time_jim_stretches_hypothesis <= time_jim_stretches_premise:
    # check if the hypothesis value contradicts the estimate of more than 'time_jim_stretches_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time it takes Jim to stretch
    # any time it takes Jim to stretch less than 'time_jim_stretches_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
