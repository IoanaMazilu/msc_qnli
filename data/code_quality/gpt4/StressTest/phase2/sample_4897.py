drum_make_time_premise = 7
drum_make_time_hypothesis = 6

# the hypothesis talks about the time Zane needs to make a drum, referenced also in the premise
if drum_make_time_hypothesis >= drum_make_time_premise:
    # check if the hypothesis value contradicts the estimate of less than 'drum_make_time_premise'
    label = "contradiction"
else:
    # the premise provides an estimate for the making time 
    # any time less than 'drum_make_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
