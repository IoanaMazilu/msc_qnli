hourly_wage_premise = 4.00
hourly_wage_hypothesis = 4.00
tip_rate_premise = 55
tip_rate_hypothesis = 15

# the hypothesis talks about the hourly wage and tip rate of Jill, referenced also in the premise
if hourly_wage_hypothesis != hourly_wage_premise:
    # check if the hypothesized hourly wage contradicts the hourly wage mentioned in the premise
    label = "contradiction"
elif tip_rate_hypothesis >= tip_rate_premise:
    # check if the hypothesized tip rate contradicts the estimate of less than 'tip_rate_premise' percent
    label = "contradiction"
else:
    # the premise gives only an upper limit for the tip rate
    # a tip rate of 'tip_rate_hypothesis' percent is consistent with the premise, but it cannot be explicitly entailed from the premise
    # the hourly wage is the same in the hypothesis and the premise
    label = "entailment"

print(label)
