pay_per_hour_premise = 100
pay_per_hour_hypothesis = 50

# the hypothesis talks about the pay per hour, referenced also in the premise
if pay_per_hour_hypothesis <= pay_per_hour_premise:
    # check if the hypothesis value contradicts the estimate of pay per hour in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the pay per hour
    # any pay per hour greater than 'pay_per_hour_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
