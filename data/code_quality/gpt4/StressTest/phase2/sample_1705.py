hourly_wage_premise = 5.00
hourly_wage_hypothesis = 5.00
tip_rate_premise = 65
tip_rate_hypothesis = 25

# the hypothesis talks about Jill's hourly wage and tip rate, both also referenced in the premise
if hourly_wage_hypothesis != hourly_wage_premise:
    # check if the hourly wage in the hypothesis contradicts the hourly wage mentioned in the premise
    label = "contradiction"
elif tip_rate_hypothesis > tip_rate_premise:
    # check if the tip rate in the hypothesis contradicts the estimate of less than 'tip_rate_premise'
    label = "contradiction"
else:
    # the hourly wage is the same in both the premise and the hypothesis, and the tip rate in the hypothesis is less than the one in the premise
    # therefore, the hypothesis does not contradict the premise, but it can be fully and explicitly entailed from the premise
    label = "entailment"

print(label)
