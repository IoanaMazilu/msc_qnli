repayment_rate_premise = 3
repayment_rate_hypothesis = 7

# the hypothesis refers to the repayment rate, also mentioned in the premise
if repayment_rate_hypothesis <= repayment_rate_premise:
    # check if the 'repayment_rate_hypothesis' contradicts the repayment rate mentioned in the premise
    label = "contradiction"
else:
    # the premise gives an exact repayment rate
    # any repayment rate greater than 'repayment_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
