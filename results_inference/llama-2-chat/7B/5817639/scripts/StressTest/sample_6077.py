time_premise = 30
time_hypothesis = 60

# the hypothesis talks about the time taken by John and Todd to rake a lawn, which is also referred to in the premise
if time_hypothesis <= time_premise:
    # check if the hypothesis value contradicts the estimate of 'time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time taken, any time greater than 'time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
