help_pavan_premise = 8
help_pavan_hypothesis = "more than 8 days"

# the hypothesis talks about the time taken to complete the work and the amount earned, referenced also in the premise
if help_pavan_hypothesis <= help_pavan_premise:
    # check if the hypothesis value contradicts the estimate of 'help_pavan_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time taken and the amount earned
    # any time taken or amount earned greater than 'help_pavan_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
