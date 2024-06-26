jill_wage_premise = 4.00
jill_wage_hypothesis = 4.00
jill_tip_rate_premise = 0.15
jill_tip_rate_hypothesis = 0.45

# the hypothesis talks about the hourly wage and tip rate of Jill, referenced also in the premise
if jill_wage_hypothesis <= jill_wage_premise:
    # check if the hypothesis value contradicts the estimate of $4.00 per hour
    label = "contradiction"
elif jill_tip_rate_hypothesis <= jill_tip_rate_premise:
    # check if the hypothesis value contradicts the estimate of 15% of the cost of the orders she serves
    label = "contradiction"
else:
    # the premise gives only an estimate for the hourly wage and tip rate of Jill
    # any number of hours greater than $4.00 per hour and any tip rate greater than 15% of the cost of the orders she serves is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
