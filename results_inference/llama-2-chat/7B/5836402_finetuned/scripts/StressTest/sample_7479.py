pay_per_hour_premise = 1
pay_per_hour_hypothesis = 1
hours_worked_premise = 84
hours_worked_hypothesis = 84

# the hypothesis talks about the number of hours worked and the pay per hour, referenced also in the premise
if pay_per_hour_hypothesis <= pay_per_hour_premise:
    # check if the hypothesis value contradicts the estimate of 'pay_per_hour_premise'
    label = "contradiction"
elif hours_worked_hypothesis < hours_worked_premise:
    # check if the number of hours worked in the hypothesis contradicts the number of hours worked reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the pay per hour
    # any pay per hour greater than 'pay_per_hour_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
