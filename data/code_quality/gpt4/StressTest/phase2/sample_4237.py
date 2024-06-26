windows_washing_time_premise = 1
windows_washing_time_hypothesis = 6

# the hypothesis talks about the time it takes for Carl to wash all the windows in his house, also mentioned in the premise
if windows_washing_time_hypothesis <= windows_washing_time_premise:
    # check if the time in the hypothesis contradicts the estimate of more than 'windows_washing_time_premise' hours
    label = "contradiction"
else:
    # the premise gives only an estimate for the washing time
    # any washing time greater than 'windows_washing_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
