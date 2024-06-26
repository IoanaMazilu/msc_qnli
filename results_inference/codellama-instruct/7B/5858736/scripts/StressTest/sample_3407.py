jill_wage_premise = 4.00
jill_wage_hypothesis = 65.00

# the hypothesis talks about the hourly wage and standard tip rate of Jill, referenced also in the premise
if jill_wage_hypothesis <= jill_wage_premise:
    # check if the hypothesis value contradicts the estimate of $4.00 per hour
    label = "contradiction"
else:
    # the premise gives only an estimate for the hourly wage and standard tip rate of Jill
    # any number greater than $4.00 per hour and 65% of the cost of the orders she serves is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
