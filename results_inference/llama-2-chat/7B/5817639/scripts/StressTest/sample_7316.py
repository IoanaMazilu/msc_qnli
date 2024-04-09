stop_time_premise = 30
stop_time_hypothesis = 80

# the hypothesis talks about the time when Jim stops, referenced also in the premise
if stop_time_hypothesis >= stop_time_premise:
    # check if the hypothesis value contradicts the estimate of less than'stop_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time when Jim stops
    # any time greater than'stop_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
