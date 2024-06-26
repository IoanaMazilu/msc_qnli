leave_time_premise = 20
leave_time_hypothesis = 90

# the hypothesis talks about the time Dan leaves City A after Cara, referenced also in the premise
if leave_time_hypothesis <= leave_time_premise:
    # check if the hypothesis value contradicts the estimate of more than 'leave_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time Dan leaves after Cara
    # any time greater than 'leave_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
