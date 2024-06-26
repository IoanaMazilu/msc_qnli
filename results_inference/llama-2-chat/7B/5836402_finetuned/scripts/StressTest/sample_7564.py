hourly_wage_premise = 8.0
tip_rate_premise = 70
tip_rate_hypothesis = 30

# the hypothesis talks about the tip rate of Jill, referenced also in the premise
if tip_rate_hypothesis > tip_rate_premise:
    # check if the hypothesis value contradicts the estimate of less than 'tip_rate_premise'
    label = "contradiction"
elif tip_rate_hypothesis < tip_rate_premise:
    # the premise gives only an estimate for the tip rate
    # any tip rate between 'tip_rate_premise' and 'tip_rate_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis value is equal to the premise value, we can infer entailment
    label = "entailment"

print(label)
