jill_wage_premise = 10.00
jill_wage_hypothesis = 8.00
jill_tip_rate_premise = 0.4
jill_tip_rate_hypothesis = 0.6

# the hypothesis talks about the tip rate, which is also mentioned in the premise
if jill_tip_rate_hypothesis <= jill_tip_rate_premise:
    # check if the hypothesis value contradicts the estimate of less than 'jill_tip_rate_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the tip rate
    # any tip rate less than 'jill_tip_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
