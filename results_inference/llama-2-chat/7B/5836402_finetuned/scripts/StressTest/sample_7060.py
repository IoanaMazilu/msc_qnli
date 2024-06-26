time_difference_premise = 20
time_difference_hypothesis = 90

# the hypothesis talks about the time difference between Dan's departure from City A and Cara's departure, referenced also in the premise
if time_difference_hypothesis <= time_difference_premise:
    # check if the hypothesis value contradicts the estimate of more than 'time_difference_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time difference
    # any time difference greater than 'time_difference_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
