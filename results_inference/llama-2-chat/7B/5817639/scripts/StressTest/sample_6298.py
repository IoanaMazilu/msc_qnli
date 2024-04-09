pay_per_hour_premise = 82
pay_per_hour_hypothesis = 12

# the hypothesis refers to the number of hours worked in a week, which is also mentioned in the premise
if pay_per_hour_hypothesis <= pay_per_hour_premise:
    # check if the estimate of 'pay_per_hour_hypothesis' contradicts the number of hours worked in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours worked,
    # any number of hours worked that is consistent with the premise is neutral and cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
