stop_time_premise = 10
stop_time_hypothesis = 60

# the hypothesis talks about the time when Pat stops, referenced also in the premise
if stop_time_hypothesis >= stop_time_premise:
    # check if the hypothesis value contradicts the estimate of'stop_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time when Pat stops
    # any time greater than'stop_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
