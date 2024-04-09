pay_per_hour_premise = 100
pay_per_hour_hypothesis = 80

# the hypothesis talks about the pay per hour for Harry, referenced also in the premise
if pay_per_hour_hypothesis <= pay_per_hour_premise:
    # check if the hypothesis value contradicts the estimate of less than 'pay_per_hour_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the pay per hour, and the hypothesis value is consistent with it
    label = "entailment"

print(label)
