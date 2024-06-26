leave_days_premise = 1
leave_days_hypothesis = 7

# the hypothesis talks about the number of days Indu leaves before the work is finished, referenced also in the premise
if leave_days_hypothesis <= leave_days_premise:
    # check if the hypothesis value contradicts the estimate of more than 'leave_days_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days
    # any number of days greater than 'leave_days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
