running_time_premise = 7
running_time_hypothesis = 6

# the hypothesis talks about the time it takes Henry to run the second leg of the course, referenced also in the premise
if running_time_hypothesis <= running_time_premise:
    # check if the hypothesis value contradicts the estimate of 'running_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time it takes Henry to run the second leg
    # any time faster than 'running_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
