time_difference_premise = 5
time_difference_hypothesis = 1

# the hypothesis talks about the time difference between Abhay and Sammer if Abhay doubles his speed, which is also mentioned in the premise
if time_difference_hypothesis >= time_difference_premise:
    # check if the hypothesis time difference contradicts the premise estimate of less than 'time_difference_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time difference
    # any time difference less than 'time_difference_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
